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
#    @Time : 2022/9/2 11:30
#    @FIle： service.py
#    @Software: PyCharm
import hello_billbil_pb2 as pb2


class Bibili(object):
    def HelloDewei(self, request, context):
        name = request.name
        age = request.age

        result = f' my name is {name}, I am {age} years old'
        return pb2.HelloDeweiRsp(result=result)


class request(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    tmp = Bibili()
    tmp_objet = request('lijiang', 19)
    print(tmp.HelloDewei(request=tmp_objet, context=''))
