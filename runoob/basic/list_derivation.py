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
#    @Time : 2022/9/17 11:14
#    @FIle： list_derivation.py
#    @Software: PyCharm

# 一、列表推导式
# 【表达式 for 变量 in 列表 if 条件】
# 【out_exp_res for out_exp in input_list if condition】
# ● out_exp_res :列表生成元素表达式，可以由返回值的函数
# ● for out_exp in input_list :迭代input_list 将out_exp 传入到out_exp_res 表达式中
# ● if condition ：条件语句，可以过滤列表中不符合条件的值
# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
name_a = [name.upper() for name in names if len(name) > 3]
print(name_a)
# { key_expr: value_expr for value in collection }

# 二、字典推导式
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
listdemo = ['Google', 'Runoob', 'Taobao']

tmp_dict = {element: len(element) for element in listdemo}
print(tmp_dict)

# 将列表转化为字典,用键为key，索引值为value
tmp_dict_1 = {element: index for index, element in enumerate(listdemo)}
print(tmp_dict_1)

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
tmp_dict_2 = {x: x ** 2 for x in (1, 2, 3)}
print(tmp_dict_2)

# 三、集合推导式

set_new = {x ** 2 for x in (1, 2, 3)}
print(set_new)

# 判断不是 abc 的字母并输出：
# {x for x in 'abracadabra' if x not in 'abc'}
set_new_1 = {x for x in 'abracadabra' if x not in 'abc'}
print(set_new_1)

# 四、元祖推导式

tuple_new = (x ** 2 for x in range(10) if x > 1)
print(tuple_new)
print(tuple(tuple_new))
