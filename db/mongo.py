# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/8 下午2:22
"""
import atexit
import sys
from signal import *

from pymongo import *

from config import *


def _init_client(mongo_config, **kwargs):
    """
    初始化 Mongo Client 全局针对一个db只需要生成一次就行
    每个 MongoClient 自带线程池
    :return:
    """
    if mongo_config.slave_host is not None:
        client = MongoClient(
            'mongodb://{master_host},{slave_host}/?replicaSet={replicaset}'.format(
                master_host=mongo_config.master_host,
                slave_host=mongo_config.slave_host,
                replicaset=mongo_config.replicaset), **kwargs)
    else:
        client = MongoClient('mongodb://{master_host}'.format(master_host=mongo_config.master_host), **kwargs)
    auth = getattr(client, mongo_config.db_name)
    auth.authenticate(mongo_config.user, mongo_config.passwd)
    db_name = mongo_config.db_name
    return client, getattr(client, db_name)


common_settings = {
    "connect": False,
    "serverSelectionTimeoutMS": 10 * 1000,  # 初次建立连接的时候, 默认连接时长, 如果 mongo挂了 这里就是最大连接时长, ms为单位
    "connectTimeoutMS": 10 * 1000,  # 心跳检测中,最长响应时间
    "socketTimeoutMS": 10 * 1000,  # 已经建立了的连接, 执行一次查询最大等候时间
    "maxPoolSize": 100,
    "minPoolSize": 0,
    "waitQueueMultiple": 10,
}

mongo_config = {

}

client_number_db, number_db = _init_client(mongo_config, **common_settings)


def get_collection(db, collection_name):
    """
    初始化到某一个具体的 Collection，需要每次动态调用
    :param collection_name:
    :return:
    """
    return getattr(db, collection_name)


# -----------------------服务结束后自动关闭 Mongo 连接
def close_db():
    client_number_db.close()


def clean(*args):
    print("closing DB by signals from outside")
    close_db()
    sys.exit(0)


for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM):
    signal(sig, clean)


def exit_handler():
    print('closing Mongo DB after any excuation')
    close_db()


atexit.register(exit_handler)
