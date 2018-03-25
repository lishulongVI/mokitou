# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/24 下午8:01
"""

# 定义常量来 加载配置文件的属性
from tornado import options

# options.parse_config_file()
# options.parse_command_line()
"""
以上语句会默认调用logging

"""

options.options.logging = None
