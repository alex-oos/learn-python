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
#    @Time : 2022/12/15 14:02
#    @FIle： phone.py.py
#    @Software: PyCharm
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Richard
# 导入phone_pb2模块
from grpc.pb2.phone_pb2 import *

# 创建user实例
user = User()
# 填入user信息
user.index = 1
user.name = "User1"
# 1、当 message 嵌套写入数据时，使用 add()
phone = user.content.add()

pt = PhoneType
# 2、enum 字段类型，使用 .Name(<int>)类型进行查看
# print(pt.Name(0))
phone.phoneType = pt.Name(0)
phone.number = 10000

# 3、repeated 字段类型,查看转义源码 default_value=[] 可知为 list 类型，可使用 append()添加字段
user.content.append(phone)

info = Remark()
info.note = "中国电信"
# info.note = "中国电信".encode('raw_unicode_escape')
# info.note = "中国电信".encode('unicode-escape')
mark = user.Value
# 4、Any 字段类型类似于泛型，使用 .Pack() 进行添加，使用 .Unpack() 类型进行解析
mark.Pack(info)

# 生成二进制文件
out_b = user.SerializeToString()
print(out_b)
user_out = User()
# 解析二进制文件
user_out.ParseFromString(out_b)
print(user_out)
