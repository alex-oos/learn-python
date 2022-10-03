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
#    @Time : 2020/9/2 18:30
#    @FIle： animals_learn.py
#    @Software: PyCharm


class Animals(object):

    def run(self):
        print("动物来了")





class Pig(Animals):

    def run(self):
        print('猪来了')


def run_twice(animals):
    animals.run()
    animals.run()

run_twice(Animals())
run_twice(Pig())