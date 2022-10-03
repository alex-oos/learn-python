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
#    @Time : 2022/6/19 20:57
#    @FIle： do_dict.py
#    @Software: PyCharm


tmp_dict = dict()

print(tmp_dict)

print('长度是：', len(tmp_dict))

print('类型是:', type(tmp_dict))
# 给字典中追加元素
tmp_dict['name'] = 'alex'
tmp_dict['age'] = 28
tmp_dict['sex'] = 'man'

print(tmp_dict)
print(tmp_dict.keys())  # 打印所有的keys
print(tmp_dict.values())  # 打印所有的value
# tmp_dict.clear()

# 遍历字典的方法：
# 方法一：遍历key，取到value
for k in tmp_dict.keys():
    print(k, ':', tmp_dict.get(k))
# 方法二：遍历value 值
for v in tmp_dict.values():
    print(v)
# 方法三：直接遍历出key 和value值
for (k, v) in tmp_dict.items():
    print(k, v)
