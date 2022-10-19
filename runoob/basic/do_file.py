#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    @Author : Alex
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#    @Time : 2022/10/19 9:41
#    @FIle： do_file.py
#    @Software: PyCharm
import os

with open(os.path.join(os.path.dirname(__file__), 'file.txt'), mode='w+') as f:
    f.write('test file write')
    f.flush()
    f.close()

with open(os.path.join(os.path.dirname(__file__), 'file.txt'), mode='w+') as f1:
    print(f1.readlines())
    f1.close()
