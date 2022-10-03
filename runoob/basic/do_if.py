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
#    @Time : 2022/6/19 21:14
#    @FIle： do_if.py
#    @Software: PyCharm

"""
    do_if.py 语句
"""
tmp = 100

if tmp:
    print('tmp', tmp)

age = int(input("请输入你的年龄:"))

if age < 18:
    print('您还是未成年人！')
elif age >= 18 and age <= 60:
    print("您是青年人")
elif age > 60:
    print("您已经可以退休了！")

input("您可以退出了")
