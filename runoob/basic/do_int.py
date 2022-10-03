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
#    @Time : 2022/6/18 21:36
#    @FIle： do_int.py
#    @Software: PyCharm

#  数字类型

"""
整型(int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。
 浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
 复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
 """
import random

#  int 类型
counter = 100
# float 类型
miles = 1000.0
name = 'runoob'

print(counter)
print(miles)
print(name)

a, b, c = 1, 3, 4

print(a, b, c)

d, e, f, g, = 20, 5, 5, True
print(d, e, f, g)

print(type(d))
print(type(g))
print(4 + 5)

# Python 数字类型转换

tmp_int = 1
print(type(tmp_int))
tmp_float = 10.0
print(type(tmp_float))
tmp_bool = True
print(type(tmp_bool))

#
# print(int(tmp1))  # 强制转化为int类型
# print(float(tmp))  # 强制转化为浮点数

################################################################################################

"""
    随机数
"""
print(random.random())

print(round(10.11))  # 向上取整
print(random.choice(range(10)))  # 随机选择一个函数
tmp = range(10)
print('tmp', tmp)
print('随机一个变量值：', random.randint(0, 100))  # 0->100 内随机值

print('随机一个变量值：', random.choice(range(1000, 3000)))  # 1000->3000 随机值

print('round(random.random() * 100 is ', round(random.random() * 100))
