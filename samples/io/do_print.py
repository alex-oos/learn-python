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
#    @Time : 2020/9/8 10:29
#    @FIle： do_print.py
#    @Software: PyCharm

"""
读取键盘输入：
1、使用raw_input 函数
eg: raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：

2、input函数
input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。


"""

# eg
from pip._vendor.distlib.compat import raw_input

str = raw_input("请输入：")
print("您输入的内容是", str)

str1 = input("请输入：")
print("您输入的是：", str1)