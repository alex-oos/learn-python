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
#    @Time : 2020/9/2 17:30
#    @FIle： person.py
#    @Software: PyCharm
import time


class Person(object):

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print(self):
        print(" % s % d %s " % (self.name,self.age,self.sex))

    def add(self):
        a = self.age+1

        return  self.age+1


person = Person('李将',15,'男')

person.print()
a = person.add()
print(a)

