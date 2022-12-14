#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    @Author : 李将
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#    @Time : 2022/9/14 18:06
#    @FIle： use_time.py
#    @Software: PyCharm

import time

# 返回当前时间的时间戳，语法:time.time()
timestamp = time.time()
print('时间戳', timestamp)
print('时间戳秒级别', int(timestamp))
print('时间戳毫秒级别', round(time.time() * 1000))
# 接收时间戳，返回当地时间下的时间元组，语法:time.localtime(timestamp)
print(time.localtime(time.time()))
# time.strftime 时间格式化
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
