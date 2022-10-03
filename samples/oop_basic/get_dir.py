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
#    @Time : 2020/9/2 19:09
#    @FIle： get_dir.py
#    @Software: PyCharm

"""
dir() 获得一个对象的所有属性和方法，返回值是一个包含字符串的list
"""

# eg:
print(dir("ADC"))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

# 判断 该对象中有没有属性x
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))

# 获取属性‘z’,获取不到，返回默认值404
print(getattr(obj, 'z', 404))

