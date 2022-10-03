#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
# 请注意，写入的不是str，而是经过UTF-8编码的bytes。
# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())
