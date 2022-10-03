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
#    @Time : 2020/9/8 12:45
#    @FIle： do_write.py
#    @Software: PyCharm

# write 方法
# write() 方法将任何字符串写入一个打开的文件，需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
# write()方法不会在字符串的结尾添加换行符('\n')：
fo = open("foo.txt", "w")
fo.write("你好")
fo.close()
