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
#    @Time : 2022/8/25 23:32
#    @FIle： bubbleSort.py
#    @Software: PyCharm
from typing import List


def bubbleSort(arr: List[int]) -> List[int]:
    """
    冒泡排序
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


if __name__ == '__main__':
    tmp = [5, 1, 3, 9]
    print(bubbleSort(tmp))
