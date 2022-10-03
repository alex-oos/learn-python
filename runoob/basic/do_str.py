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
#    @Time : 2022/6/18 21:42
#    @FIle： do_str.py
#    @Software: PyCharm


str = 'runoob'
print(type(str))
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个字符串到倒数第二个的所有的字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出第三个字符到第五个字符
print(str[2:])  # 输输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "test")  # 字符串拼接
#  字符串格式化
print("我叫 %s" % ("小明"))

# 字符串格式化特性python3.6开始新增的,使用f-string
name = 'Runoob'
print(f'Hello {name}')
x = 1
print(f'{x + 1=}')
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')
print("我叫 %s 今年 %d 岁!" % ('小明', 10))
name = 'Alex'
age = 20
print(f'我叫 {name},我今年{age}岁')
