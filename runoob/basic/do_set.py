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
#    @Time : 2022/6/19 21:08
#    @FIle： do_set.py
#    @Software: PyCharm


#  定义一个set，推荐使用方式一
# 方式一：
tmp_set1 = set('1,3,4,545')
print('tmp_set1的类型是：', type(tmp_set1))
# 方式二：
tmp_set = {1, 3, 4, 5, 6}
print('tmp_set的类型是：', type(tmp_set))

# set 无法进行切片

# set 的内置函数
tmp_set.add('alex')  # 增加一个元素
print(tmp_set)
tmp_set.remove(1)  # 移除指定元素
print(tmp_set)
tmp_set.clear()  # 清空元素
print(tmp_set)

#  set 列表生成式
tmp = {x for x in 'abracadabra' if x not in 'abc'}
print(tmp)
