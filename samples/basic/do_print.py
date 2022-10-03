#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('The quick brown fox', 'jumps over', 'the lazy dog')
print(300)
print(100 + 200)
print('100 + 200 =', 100 + 200)

# 常见的占位符输出
#  %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
a = 1
print('%2d' % a)
b = 11.2
print('%f' % b)
c = 'c'
print('%c' % c)

print('%d %f %c' % (a, b, c))
