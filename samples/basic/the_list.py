#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 下午 11:12
# @Author  : 李将
# @Site    :
# @File    : learn4.py
# @Software: PyCharm

# 关于list
classmates = ['Me', 'Ab', 'Bc']
print(classmates)

# 获取他的长度
print(len(classmates))

# 取值，用索引值取
print(classmates[0])

# 取最后一个值
print(classmates[len(classmates) - 1])

print(classmates[-1])

# list 是一个可变的的有序表，所以，list中可以追加元素到末尾
classmates.append('Ass')
print(classmates)

# list 插入元素到指定的位置
classmates.insert(1, 'Jack')
print(classmates)
# list 删除指定的元素
classmates.pop(0)
print(classmates)
# list 替换元素
classmates[0] = 'Search'
print(classmates)

# list里面的元素的数据类型也可以不同
alist = ['a', 'c', 1, 11.11]
print(alist)

# list元素也可以是另一个list，比如：
blist = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
print(len(blist))
print(blist)

# 遍历list中的每个元素
clist = [1, 3, 8, 6, 7]
clist.sort()
print(clist)
for iterm in clist:
    print(iterm)

elist = [9, 1, 3, 4, [5, 8]]

for element in elist:
    if isinstance(element, list):
        for i in element:
            print(i)
    else:
        continue
    print(iterm)

# list进行排序
dlist = ['a', 'c', 'b']
dlist.sort()
print(dlist)


# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
print(L[1][1])
print(L[2][2])
print(L[-1][-1])

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.pop()
print('classmates =', classmates)
