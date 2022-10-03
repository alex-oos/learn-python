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
#    @Time : 2022/6/18 21:48
#    @FIle： do_list.py
#    @Software: PyCharm


tmp_list = list(range(13))

typelist = [True, 'alex']

print(tmp_list)  # 打印出list 列表
print(tmp_list[0])  # 打印出list列表的第一个元素
print(tmp_list[1:3])  # 打印出list 第二个元素到第三个元素 左闭右开
print(tmp_list[-2])  # 打印出list 倒数第二个元素
print(tmp_list[:-2])  # 打印出从第一个元素到倒数第二个元素
print(tmp_list[0:-2])  # 打印出第一个元素到倒数第二个元素 0 可以省略
print(tmp_list[1:-2])  # 打印出list第二个元素到倒数第二个元素
print(tmp_list[2:])  # 输出第二个元素到最后的元素
print(tmp_list * 2)  # 输出两次
print(tmp_list + typelist)  # 列表拼接

#  列表比较
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]

print('operator.eq(a, b)', operator.eq(a, b))
print('operator.eq(a, b)', operator.eq(b, c))

# 列表中函数和方法
print('list长度为：', len(tmp_list))

print('list中的最大值', max(tmp_list))
print('list中的最小值', min(tmp_list))

# list 的操作 ，增加，修改，删除
tmp_list.append("alex")
print('list元素增加之后:', tmp_list)

print('统计list中某个元素出现的次数：', tmp_list.count(tmp_list[0]))

print('在列表中找出某一个值的匹配的索引值', tmp_list.index(tmp_list[0]))
tmp_list.insert(0, 'aaa')
print('插入一个元素', tmp_list)
tmp_list.reverse()
print('反向输出列表', tmp_list)

tmp_list.remove(tmp_list[0])
print('list列表删除首元素之后', tmp_list)
tmp = tmp_list.copy()
print('copy tmp_list ', tmp)
tmp_list.clear()
print('清除list中的元素之后: ', tmp_list)
print([1, 2, 3] + [4, 5, 6])

# 遍历list的两种方式
list = [1, 213, 3, 4, 5, 6]
#  方式一： 遍历出index, element
for index, element in enumerate(list):
    print(index, element)

# 方式二：遍历出list中的每个元素
for i in list:
    print(i)

# 方式三： 根据list的长度遍历
for j in range(len(list)):
    print(list[j])
