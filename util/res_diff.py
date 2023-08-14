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
#    @Time : 2023/8/14 上午11:00
#    @FIle： res_diff.py
#    @Software: PyCharm
# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Alex <alex@gmail.com
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     |MENG|
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#                        2019-09-20  13:46

import re


def res_diff(src_data, dst_data, path='', diff=dict()):

    if isinstance(src_data, dict):
        for key in src_data:
            newpath = path + '.' + key
            if key in dst_data:
                res_diff(src_data[key], dst_data[key], newpath, diff)
            else:
                diff[newpath] = [src_data.get(key), 'not exist is key']
    elif isinstance(src_data, list):
        if len(src_data) == len(dst_data):
            tmp = zip(src_data, dst_data)
            for k, v in enumerate(tmp):
                diff = res_diff(v[0], v[1], path + '.' + str(k), diff)
        else:
            diff[path] = [src_data, dst_data]
    else:
        if src_data != dst_data:
            diff[path] = [src_data, dst_data]

    return diff


if __name__ == "__main__":
    xx = {'kkk0': 'vvv0', 'kkkk1': [{'c': 'd', 'k2': [{'kk2': 'vv2'}, {'kk3': 'vv3'}]}, {'k3': 'v3'}], 'kkkk2': 'vvvv2'}
    yy = {'kkk0': 'vvvv0', 'kkkk1': [{'c': 'd', 'k2': [{'kk2': 'diffvv2'}, {'kk3': 'vv3'}]}, {'k3': None}]}
    diff = res_diff(xx, yy)
    for k, v in diff.items():
        print('key is {} -> value is {}'.format(k, v))
