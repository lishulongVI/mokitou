# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/25 上午11:25
"""
import os

base_path = os.path.dirname(os.getcwd())

options = {
    'port': 9000,
    'address': '0.0.0.0'
}

setting = {
    # 生产模式下 修改为false，当文件发生修改后可以自动重启
    """
    取消缓存编译的模板
    取消缓存静态文件的hash值
    提供追踪信息
    """
    "debug": True,
    'static_path': os.path.join(base_path, 'static'),
    'template_path': os.path.join(base_path, 'template'),
    'autoreload': True,
}
