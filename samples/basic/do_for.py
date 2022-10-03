#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 打印dict
adict = {'Aoole': 100, 'Bannane': 10}
c = {'a': '1', 'b': '2', 'c': '3'}

# 遍历key 和value值
for key in adict:
    print(key + ':' + str(adict[key]))

# 遍历key 和value值
for key in c:
    print(key + ':' + c[key])

for key in c.keys():
    print(key + ':' + c[key])
# 遍历value值
for value in adict.values():
    print(value)

# 遍历字典型
for kv in c.items():
    print(kv)

# 遍历字典健值

for key, value in c.items():
    print(key + ':' + value)

# 遍历tuple
atuple = (1, 2, 3, 4, 5, 6)
for key in atuple:
    print(key)

# 打印数字 0 - 9
for x in range(10):
    print(x)
