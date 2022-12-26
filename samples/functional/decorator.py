#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
装饰器：


"""
import time
from functools import wraps


# 无参装饰器
def outer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('执行前')
        res = func(*args, **kwargs)
        print('执行后')
        return res

    return inner


@outer
def fun1():
    print('我是fun1函数')
    a = 'fun1'
    return a


tmp = fun1()
print(tmp)


# 有参装饰器

def outerp(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(text)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@outerp('test')
def aa():
    print('aaa')


c = aa()


# 练习题

def metric(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        begin_time = time.time()
        result = fn(*args, **kwargs)
        print(f'{fn.__name__} executed in {round(time.time() - begin_time, 4)} ms')
        return result

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
