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
#    @Time : 2023/8/14 上午10:01
#    @FIle： res_diff.py
#    @Software: PyCharm


def res_diff(src_data, dst_data, path='', result=dict) -> dict:
    """
    比较两个字典的差异
    :param src_data: 源数据
    :param dst_data: 目标数据
    :param path: 路径
    :param result: 结果
    :return: 返回差异数据
    """
    if isinstance(src_data, dict):
        for key in src_data:
            new_path = path + '.' + key
            if dst_data is not None and key in dst_data:
                result = res_diff(src_data[key], dst_data[key], new_path, result)
    elif isinstance(src_data, list):
        if len(src_data) == len(dst_data):
            tmp = zip(src_data, dst_data)
            for k, v in enumerate(tmp):
                result = res_diff(v[0], v[1], path + '.' + str(k), result)
            else:
                result[path] = [src_data, dst_data]
    else:
        if src_data != dst_data:
            result[path] = [src_data, dst_data]

    return result


if __name__ == "__main__":
    xx = {'kkk0': 'vvv0', 'kkkk1': [{'c': 'd', 'k2': [{'kk2': 'vv2'}, {'kk3': 'vv3'}]}, {'k3': 'v3'}], 'kkkk2': 'vvvv2'}
    yy = {'kkk0': 'vvvv0', 'kkkk1': [{'c': 'd', 'k2': [{'kk2': 'diffvv2'}, {'kk3': 'vv3'}]}, {'k3': None}]}
    diff = res_diff(xx, yy)
    for k, v in diff.items():
        print('key is {} -> value is {}'.format(k, v))
