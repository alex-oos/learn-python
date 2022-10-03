#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# map（） 函数可以接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到每个元素，并把结果作为新的Iterator 返回
# map函数的应用一：将list中的每个元素返回元素的平方
def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# map函数应用二：将list中的所有数字转化为字符串
print(list(map(str,[1,2,3,4,55,6,7,7])))

# eg2:利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    name = name[0].upper()+name[1:].lower()
    return  name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

