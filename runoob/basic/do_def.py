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
#    @Time : 2022/6/19 21:38
#    @FIle： do_def.py
#    @Software: PyCharm

"""
函数的基本用法:
"""


def function() -> None:
    """
    无参函数
    """
    print("函数")
    return None


def functions(var) -> None:
    """
    指定参数
    """
    print('var', var)
    return None


def function1(name: str, age: int) -> None:
    """
    多个参数
    """
    print('name', name)
    print('age', age)
    return None


def function2(name: str, age=20) -> None:
    """
    多个参数，另外一个是默认值
    """
    print('name', name)
    print('age', age)
    return None


def function3(*var) -> None:
    """
    不定参数，可以传递任何值，任何数量，方便使用
    """
    print(*var)
    return None


if __name__ == '__main__':
    function()
    functions("11")
    function1(name='alex', age=20)
    function2(name='alex')
    function3('1', 2, list(range(5)))
