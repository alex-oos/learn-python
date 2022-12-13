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
#    @Time : 2020/9/2 16:36
#    @FIle： anonymous_function.py
#    @Software: PyCharm

"""
匿名函数，匿名函数很简单，lambda 代表匿名函数
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
"""


# eg1: 正常函数与匿名函数对比
def f(x):
    return x * x


# 匿名函数
c = lambda x: x * x
print(f(2) == c(2))


# eg2: 将以下正常函数修改为匿名函数
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)

tmp_L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L, tmp_L, L == tmp_L)

# 实际应用
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

'''
(lambda x: x * x  等价于
def f(x):
    return x * x
    使用的时候可以一起使用，
'''
