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
#    @Time : 2020/9/2 17:30
#    @FIle： person.py
#    @Software: PyCharm


class Person(object):
    # 定义基本属性
    name = None
    age = None
    sex = None
    # 定义私有属性,私有属性在类外部无法访问
    __weight = None

    # 定义构造方法
    def __init__(self, n, a, s, w):
        self.name = n
        self.age = a
        self.sex = s
        self.__weight = w

    def add(self):
        a = self.age + 1
        return self.age + 1

    def __str__(self):
        return 'name: ' + str(self.name) + ' age:' + str(self.age) + ' sex: ' + str(self.sex) + ' __weight: ' + str(
            self.__weight) + ' '


# 单继承示范
class Student(Person):
    grade = None

    def __init__(self, n, a, s, w, g):
        super().__init__(n, a, s, w)
        self.grade = g

    def __str__(self):
        return super().__str__() + 'grade: ' + str(self.grade)


class Speaker(object):
    topic = None
    name = None

    def __int__(self, n, t):
        self.name = n
        self.topic = t

    def __str__(self):
        return 'name: ' + str(self.name) + ' topic:' + str(self.topic)


# 多继承示范
class Sample(Speaker, Student):

    def __int__(self, n, a, s, w, g, t):
        Student.__init__(self, n, a, s, w, g)
        Speaker.__init__(self, n, t)


if __name__ == '__main__':
    person = Person('Alex', 20, '男', 100)
    print(person.__str__())
    a = person.add()
    print('年龄是：', a)
    student = Student('Alex', 20, '男', 120, 100)
    print(student.__str__())

    sample = Sample('Alex', 20, '男', 120, 'python', 'python')
    print(sample.__str__())
