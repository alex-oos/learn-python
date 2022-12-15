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
#    @Time : 2022/12/15 12:07
#    @FIle： addressbook.py
#    @Software: PyCharm
# 这里使用绝对路径，不然会报错
from google.protobuf import json_format

from grpc.pb2.addressbook_pb2 import *

addressBook = AddressBook()
person = addressBook.people.add()
person.name = 'alex'
person.id = 1
person.email = 'alex@qq.com'
person.money = 123.45
person.work_status = True

phone_number = person.phones.add()
phone_number.number = '1234567890123'
phone_number.type = MOBILE
person.phones.append(phone_number)

maps = person.maps
maps.mapfield[1] = 1
maps.mapfield[2] = 2
addressBook.people.append(person)
# 序列化操作
msg = addressBook.SerializeToString()
print('序列化后的值：', msg, type(msg))
# 反序列化
addressBook.ParseFromString(msg)
msg_json = json_format.MessageToJson(addressBook)  # 转化为json类型
print('反序列化后的值是：', msg_json)
