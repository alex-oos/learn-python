#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

# reduce 的高级使用使用：
"""
    reduce 第一个参数是函数，并且不需要写括号，并且必须接收两个参数
            第二个参数是一个迭代器函数，比如list，会将结果与下一个函数做累积计算
    reduce 将一个函数作用在一个序列上[x1,x2,x3,x4,x5]，这个函数必须接收两个参数,reduce 把结果和序列的下一个元素做累积计算

"""

# eg1: 累积求和
# 方式一：
print('sum is ', sum(list(range(0, 100, 5))))


# 方式二：
def add(x, y):
    return x + y


# reduce 第一个参数是函数传参的时候不需要有括号
tmp = reduce(add, list(range(0, 100, 5)))
print(tmp == sum(list(range(0, 100, 5))))

# eg2:遍历所有元素

# eg2:将列表转化为整数


# 将Str转化为int
CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    print(ints)
    return reduce(lambda x, y: x * 10 + y, ints)


print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


#  eg:
def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        # nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)


print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


# eg:
def str2float1(s):
    def fn(x, y):
        return x * 10 + y

    # 得到字符串中.的索引
    n = s.index('.')
    # 根据.的位置将字符串切片为两段
    s1 = list(map(int, [x for x in s[: n]]))
    s2 = list(map(int, [x for x in s[n + 1:]]))
    # m ** n表示m的n次方
    return reduce(fn, s1) + reduce(fn, s2) / 10 ** len(s2)


# 测试结果是否正确
print('str2float(\'123.456\')=', str2float('123.456'))


# eg:Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L1):
    return reduce(lambda x, y: x * y, L)


L = [1, 3, 4, 5, 6]
L1 = prod(L)
print(L1)
