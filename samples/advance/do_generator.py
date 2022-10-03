#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器  使用了 yield 的函数被称为生成器
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
#
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
#
# 调用一个生成器函数，返回的是一个迭代器对象。

# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(10)  # f 是一个迭代器，由生成器返回生成
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
