#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    @Author : 李将
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#    @Time : 2020/9/8 13:53
#    @FIle： do_tell.py
#    @Software: PyCharm
# tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。
# seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。

# 如果from被设为0，这意味着这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。

# eg:
fo = open("foo.txt","r+")
str = fo.read(100)
print("读取出来的字符串是：", str)

position = fo.tell()
print("当前的位置是：", position)

position = fo.seek(0,0)
str = fo.read(100)
print("重新读取字符串", str)

fo.close()