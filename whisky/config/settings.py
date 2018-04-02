# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/2 上午10:10
"""
import os

base_path = os.path.dirname(os.path.dirname(__file__))

settings = {
    'debug': True,
    'static_path': os.path.join(base_path, 'statics'),
    'template_path': os.path.join(base_path, 'templates'),
}

options = {
    'address': '0.0.0.0',
    'port': 2000,
}
