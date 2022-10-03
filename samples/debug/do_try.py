#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常处理：
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生

"""

# eg:1
"""
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
"""
# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常")
# except IOError:
#     print("error 没有找见文件或读取文件失败")
# else:
#     print("内容写入文件成功")
#     fh.close()
#
#
# # eg2:
# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError:
#         print("参数没有函数数字", var)
#
#
# temp_convert("ss")


try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except ValueError as e:
        print('Error:', e)
    finally:
        print('finally...')


from functools import reduce


def str2num(s):
    return int(s)


def calc(exp):
    ss = exp.split('+')
    try:
        ns = map(str2num, ss)
        return reduce(lambda acc, x: acc + x, ns)
    except ValueError as e:
        print(e)
    finally:
        print("chegn")


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
