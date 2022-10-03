#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
判断类型

"""
# type()
import types

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

print('type(\'abc\')==str?', type('abc') == str)

# 判断基本数据类型
if type('123') == str:
    print("类型判断正确")
if type(123) == int:
    print("int类型")


# 判断函数类型

def fn():
    pass


if __name__ == '__main__':
    if type(fn()) == types.FunctionType:
        print('相同')
    else:
        print('不相同')
