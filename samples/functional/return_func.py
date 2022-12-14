#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    返回函数：顾名思义其实就是在一个函数里面套入一个函数，返回值的类型从一个对象变成了一个函数类型
"""


# demo1
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax

    return sum


f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print('调用f函数', f)
print('调用f函数里面的函数', f())

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
#
f1 = lazy_sum(1, 2, 3, 4, 5, 6)
f2 = lazy_sum(1, 2, 3, 4, 5, 6)
print(f1 == f2)


# 闭包

# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# fix:
def count():
    fs = []

    def f(n):
        def j():
            return n * n

        return j

    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
