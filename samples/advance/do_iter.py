#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Iterable, Iterator

# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()
a = [1, 2, 3, 4]
it = iter(a)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素

# for 循环遍历迭代器
tmp_list = list(range(10))
tmp_iter = iter(tmp_list)  # 创建迭代器对象
for i in tmp_iter:
    print(i)


# 使用next 遍历迭代器中的元素
# tmp_list_1 = list(range(10, 20))
# tmp_iter_1 = iter(tmp_list_1)  # 创建迭代器
# while True:
#     try:
#         print(next(tmp_iter_1))  # 输出迭代器对象从集合的第一个元素开始访�
#     except StopIteration:
#         sys.exit()


# 手写一个迭代器，一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
# 如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
#
# 更多内容查阅：Python3 面向对象
#
# __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
#
# __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
# StopIteration
# StsopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

class Mynumbers():

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myClass = Mynumbers()
myiter = iter(myClass)
print('next(myIter)is ', next(myiter))
print('next(myIter)is ', next(myiter))
print('next(myIter)is ', next(myiter))
print('next(myIter)is ', next(myiter))


def g():
    yield 1
    yield 2
    yield 3


"""
    迭代器Iterator，是否是可迭代对象Iterable
"""
print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))
