#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

filter（）函数属于过滤序列
filter() 传一个函数和一个序列，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False 决定保留还是丢弃该元素

'''


# eg: 在一个列表中，删掉偶然，保存奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list(filter(is_odd, L))
print(a)


# eg2:将一个字符串中的空字符删掉
def not_empty(s):
    return  s and s.strip()

L2 = ['A',' ','C']
a_list = list(filter(not_empty,L2))
print(a_list)

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def  is_palindprome(n):
    nn = str(n)
    return  nn ==nn[::-1]  # 反向取数
print(list(filter(is_palindprome,['sb','aa'])))

