#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
__slots__ 用来限制实例的属性，显示class 能够添加的属性，只能添加这两个属性，其余属性不能添加

使用__slots__ 注意，__slots__ 定义的属性仅针对当前类实例起作用，对继承的子类是不起作用的

"""


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple 定义允许绑定的属性名称


class GraduateStudent(Student):
    pass


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
