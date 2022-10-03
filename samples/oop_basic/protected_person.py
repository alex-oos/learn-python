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
#    @Time : 2020/9/2 17:58
#    @FIle： protected_person.py
#    @Software: PyCharm

class Person(object):

    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        return self.__age

    def print(self):
        print("%s %d %s " % (self.__name, self.__age, self.__sex))


person = Person('李将', 10, '男')
print(person.get_name())
print(person.get_age())
print(person.set_age(100))
person.print()


class Test(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender
        return self.__gender

test = Test('aa','assa')
test.set_gender('aa')
print(test.get_gender())
