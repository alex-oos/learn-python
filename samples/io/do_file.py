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
#    @Time : 2020/9/8 10:41
#    @FIle： do_file.py
#    @Software: PyCharm

fo = open("foo.txt","w")
print("文件名", fo.name)
print("是否关闭", fo.closed)
print("访问模式", fo.mode)
# close()方法
# 当一个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件。用 close（）方法关闭文件是一个很好的习惯。
fo.close()

