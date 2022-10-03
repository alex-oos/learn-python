#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 针对自动重复的值，进行了自动过滤,set 还对他默认进行了排序
s = set([9, 3, 4, 5, 6, 7, 8, 1])
print(s)

s.add(2)
print(s)

s5 = set(['a', 'd', 'c'])
print(s5)
