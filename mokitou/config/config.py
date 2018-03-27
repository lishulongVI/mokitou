# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/25 上午11:25
"""
import os

base_path = os.path.dirname(os.path.dirname(__file__))
# base_path = os.path.dirname(os.getcwd())

# print(base_path)

options = {
    'port': 9000,
    'address': '0.0.0.0'
}

"""
   取消缓存编译的模板 complain_template_cache=False
   取消缓存静态文件的hash值 static_hash_cache=False
   提供追踪信息server_traceback=True
"""
# 'autoreload': True,
# 'autoescape': None, 关闭当前项目中的自动转义 自动转义是为了安全考虑 不建议此种方式实现 自动转义

settings = {
    "debug": True,  # 生产模式下 修改为false，当文件发生修改后可以自动重启
    'static_path': os.path.join(base_path, 'statics'),
    'template_path': os.path.join(base_path, 'templates'),

}

# print(settings)
