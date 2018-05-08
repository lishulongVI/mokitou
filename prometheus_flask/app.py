# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/5/8 上午10:18
"""

import os

import prometheus_client
from flask import Flask, Response, request
from flask import jsonify
from prometheus_client import CollectorRegistry, multiprocess
from prometheus_client import Counter
from prometheus_client.multiprocess import MultiProcessCollector

# REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REGISTRY = CollectorRegistry(auto_describe=False)
MultiProcessCollector(REGISTRY)

requests_total = Counter("app:requests_total", "Total count of requests", ["method", "url_rule"], registry=REGISTRY)

app = Flask(__name__)


def record(func):
    """
    func 即为调用该函数的方法
    """
    def req(*args, **kwargs):
        requests_total.labels(method=request.method, url_rule=request.path.lower()).inc()
        print("# Process in {0}".format(os.getpid()))
        return func(*args, **kwargs)
    return req


@app.route('/health', methods=['GET'])
@record
def api_health():
    return jsonify({'status': 'UP'}), 200


@app.route('/test', methods=['GET'])
def api_test():
    return jsonify({'status': 'UP'}), 200


@app.route('/stats', methods=['GET'])
def metrics1():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    return prometheus_client.generate_latest(registry), 200