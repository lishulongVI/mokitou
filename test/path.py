# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/8 上午11:54
"""
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

print(project_dir)
project_dir = os.path.normpath(os.path.dirname(project_dir))

print(project_dir)
project_name = os.path.basename(project_dir)

print(project_name)


def get_files_under_dir(dir_name):
    """
    显示某一个文件夹下面的所有的文件名称
    :param dir_name:
    :param ouput_as_list: 是否按照list字符串输出
    :return:
    """
    list_dirs = os.walk(dir_name)
    file_list = list()
    for root, dirs, files in list_dirs:
        for d in dirs:
            pass
        for f in files:
            file_list.append(os.path.join(root, f))
    return file_list


print(get_files_under_dir('/Users/lishulong/PycharmProjects/thinking'))
