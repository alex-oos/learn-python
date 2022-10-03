#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)


__cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)
"""


class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __cmp__(self, other):
        if self.name == str(other):
            print("相等")
        else:
            print('不相等')

    # 而是__repr__()，两者的区别是__str__()
    # 返回用户看到的字符串，而__repr__()
    # 返回程序开发者看到的字符串，也就是说，__repr__()
    # 是为调试服务的。
    #
    # 解决办法是再定义一个__repr__()。但是通常__str__()
    # 和__repr__()
    # 代码都是一样的，所以，有个偷懒的写法：
    __repr__ = __str__


print(Student('Michael'))

s = Student("ss")
