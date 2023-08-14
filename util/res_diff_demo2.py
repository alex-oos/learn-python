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
#    @Time : 2023/8/14 上午11:21
#    @FIle： res_diff_demo2.py
#    @Software: PyCharm
def res_diff(src_data, dst_data, path='', diff=None):
    if diff is None:
        diff = {}

    if src_data == dst_data:
        return diff

    if isinstance(src_data, (dict, list)):
        for key, src_value in enumerate(src_data) if isinstance(src_data, list) else src_data.items():
            new_path = f"{path}.{key}" if path else str(key)
            if new_path not in diff:
                if isinstance(dst_data, (dict, list)) and key in dst_data:
                    res_diff(src_value, dst_data[key], new_path, diff)
                else:
                    diff[new_path] = [src_value, 'not exist in key']
    else:
        diff[path] = [src_data, dst_data]

    return diff


if __name__ == '__main__':
    xx = {'kkk0': 'vvv0', 'kkkk1': [{'c': 'd', 'k2': [{'kk2': 'vv2'}, {'kk3': 'vv3'}]}, {'k3': 'v3'}], 'kkkk2': 'vvvv2'}
    yy = {'kkk0': 'vvvv0', 'kkkk1': [{'c': 'd', 'k2': [{'kk2': 'diffvv2'}, {'kk3': 'vv3'}]}, {'k3': None}]}
    diff = res_diff(xx, yy)
    for k, v in diff.items():
        print('key is {} -> value is {}'.format(k, v))
