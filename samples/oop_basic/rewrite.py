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
#    @Time : 2022/10/17 20:27
#    @FIle： rewrite.py
#    @Software: PyCharm

# 重写

class Parent(object):

    def myMothod(self):
        print('parent myMothod')


class Child(Parent):
    def myMothod(self):
        print('child myMothod')


if __name__ == '__main__':
    child = Child()
    child.myMothod()
    super(Child, child).myMothod()
