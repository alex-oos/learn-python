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
#    @Time : 2022/9/2 14:40
#    @FIle： client.py
#    @Software: PyCharm

from google.protobuf import json_format

import hello_billbil_pb2 as pb2

request = pb2.HelloDeWeiReq()
request.name = 'boby'
request.age = 11

res_str = request.SerializeToString()  # 序列化 变成二进制

print('res_str', res_str)

request2 = pb2.HelloDeweiRsp()

request2.ParseFromString(res_str)  # 反序列化，将二进制转化成对象

res_json = json_format.MessageToJson(request2)  # 设置为json
print(res_json)
