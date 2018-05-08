# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/5/8 上午10:17
"""
from prometheus_client import start_http_server

from prometheus_flask.app import app

# Create a metric to track time spent and requests made.


# Decorate function with metric.


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    # start_http_server(8001)
    app.run(host='0.0.0.0', port=8000, threaded=True)
    # Generate some requests.
