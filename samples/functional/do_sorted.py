#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

'''
    sorted()函数就是进行排序
'''

# eg1：d对L排序
L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
# 按照小写a,b,c排序
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 通过某个关键字排序一个字典列表
# 通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。 假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：


print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
# 对她进行反向排序
print(sorted(students, key=itemgetter(1), reverse=True))

