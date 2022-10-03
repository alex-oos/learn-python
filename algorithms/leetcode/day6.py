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
#    @Time : 2022/7/25 19:48
#    @FIle： day6.py
#    @Software: PyCharm
import collections


# 第一次只出现一次的字符
# https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-by-3zqv5/
class Solution:
    def firstUniqChar(self, s: str) -> str:
        frequency = collections.Counter(s)
        # print(frequency)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return ch
        return ''


if __name__ == '__main__':
    tmp = Solution()
    print(tmp.firstUniqChar('abaccdeff'))
