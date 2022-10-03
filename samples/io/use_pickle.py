#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
#
#序列化：变量从内存中变成可存储或传输的过程称之为序列化
# pickling  序列化
#
d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)
