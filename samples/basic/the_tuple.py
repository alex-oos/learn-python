#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
atuple = tuple()
atuple = ('Mic', 'Ca', 'As')

print(atuple)

# 取值
print(atuple[0])  # 取第一个元素
print(atuple[-1])  # 取最后一个元素
print(atuple[1:])  # 取从第二个元素到最后
print(atuple[:-1])  # 从第一个元素 到最后第一个元素

print(atuple[len(atuple) - 1])

classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# cannot modify tuple: 元祖不能赋值
classmates[0] = 'Adam'
