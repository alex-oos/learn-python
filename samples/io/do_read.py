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
#    @Time : 2020/9/8 12:57
#    @FIle： do_read.py
#    @Software: PyCharm

# read() 方法
# read() 方法从一个文件中读取一个字符串，需要重点注意的是，Python 字符串可以是二进制数据，而不仅仅是文字
# 语法： fileObject.read([count])
# readLine() 可以直接读取每一行内容
# readLines() 一次性读取所有内容，并且返回list
# read(size)

fo = open("foo.txt","r+")
str = fo.read()
print("读取的字符是：",str)
fo.close()