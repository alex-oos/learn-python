#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    @Author : tangkaize
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#    @Time : 2022/12/15 13:31
#    @FIle： example.py
#    @Software: PyCharm
from google.protobuf import json_format

from grpc.pb2.example_pb2 import *

# 第一种方式添加BarMsg : Repeated Message
foo = Foo(
    bars=[
        BarMsg(i=7777111, j=92323232)
    ]
)
# 普通属性
foo.foo_name = "safly"

# 列表nums :Repeated Fields
foo.nums.append(15)
foo.nums.extend([32, 47])
foo.nums[0] = 123
foo.nums.insert(0, 34343)

bar = Foo.Bar
bar.bar_name = "bar_anme"
# 列表1Repeated Message Fields
bar_msg = foo.bars.add()
bar_msg.i = 123
bar_msg.j = 1234
# 也可以按着如下的方式添加
foo.bars.add(i=999999, j=42342444)

# 列表2另外的方式
bar_msg_extend = BarMsg()
bar_msg_extend.i = 234
bar_msg_extend.j = 456
foo.bars.extend([bar_msg_extend])
# 序列化
msg = foo.SerializeToString()
print('序列化后的msg：', msg)
# 反序列化
foo.ParseFromString(msg)
msg = json_format.MessageToJson(foo)
print('反序列化后的msg：', msg)
