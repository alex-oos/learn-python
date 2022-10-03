#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

"""
枚举类： 可以通过枚举里面的每个变量
"""


@unique  # 用于变量里唯一值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon

print('day1 =', day1)
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Gender(Enum):
    Male = 0
    Female = 1


@unique
class Gender(Enum):
    male = 0
    female = 1


class Student(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return self.name, self.gender


s = Student('李将', Gender.male)
print(s.gender)
print(Gender.male.value)
print(s.__str__())
