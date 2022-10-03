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
#    @Time : 2020/9/4 11:41
#    @FIle： special_init.py
#    @Software: PyCharm

"""
__init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)

"""
class Student(object):

    def __init__(self,name):
        self.name = name

s = Student(name="s")
print(s)