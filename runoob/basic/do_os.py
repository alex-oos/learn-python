#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    @Author : Alex
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#    @Time : 2022/10/19 10:00
#    @FIle： do_os.py
#    @Software: PyCharm
import os
import time

print(os.getcwd())  # 返回当前命令
os.mkdir('1')  # 新建文件夹
print(os.path.exists(os.getcwd().join('1')))  # 判断是否存在
os.rmdir('1')  # 删除文件夹
os.system('python --version')  # 调用系统命令
print(os.path.join(os.path.dirname(__file__), 'do_os.py'))
os.chdir(os.path.join(os.path.dirname(__file__)))  # 切换目录

# 常见的路径方法 使用的是os.path模块
"""path
"""
print(__file__)  # 当前文件名
print(os.path.abspath(__file__))  # 绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  # 返回文件目录路径
print(os.path.basename(__file__))  # 返回文件名
print(os.path.dirname(__file__))  # 返回目录路径
print(os.path.split(__file__))  # 分割文件名与路径
print(os.path.join(os.path.dirname(__file__), 'do_os.py'))  # 将目录和文件合并成一个路径

print(os.path.getatime(__file__))  # 输出最近访问时间
print(os.path.getctime(__file__))  # 输出文件创建时间
print(os.path.getmtime(__file__))  # 输出最近修改时间
print(time.gmtime(os.path.getmtime(__file__)))  # 以struct_time形式输出最近修改时间
print(os.path.getsize(__file__))  # 输出文件大小（字节为单位）
print(os.path.abspath(__file__), type(os.path.abspath))  # 输出绝对路径
print(os.path.normpath(__file__), type(os.path.normpath(__file__)))  # 规范path字符串形式
