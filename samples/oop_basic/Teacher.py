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
#    @Time : 2022/10/4 21:01
#    @FIle： Teacher.py
#    @Software: PyCharm

class Teacher(object):
    # 定义基本属性
    mame = None
    age = None
    sex = None
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = None

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def __str__(self):
        return self.name + " " + str(self.age) + " " + str(self.__weight)


if __name__ == '__main__':
    teacher = Teacher('ALex', 28, '男')
    print(teacher.__str__())
