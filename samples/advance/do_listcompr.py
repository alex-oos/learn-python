#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成器
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
import os

print([x * x for x in range(1, 11)])

a = []
for x in range(1, 11):
    a.append(x * x)
print(a)
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

# 使用列表生成式，直接遍历中key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

f = {'key': 1, 'key1': 2}

print([k + ':' + str(v) for k, v in f.items() if k == 'key'])

# 使用列表生成式，将大小写进行转换
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 使用列表生成器，显示所有当前目录下的文件和目录名

print([d for d in os.listdir('.')])

l1 = ['Hello', 'World', 18, 'Apple', None]

for i in l1:
    if isinstance(i, str):
        print(i.lower())
    else:
        continue

print([i.lower() for i in l1 if isinstance(i, str)])
