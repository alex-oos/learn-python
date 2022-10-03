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
#    @Time : 2022/6/19 22:00
#    @FIle： person.py
#    @Software: PyCharm


class people(object):
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问

    __weight = 0

    def __init__(self, name, age, __weight) -> None:
        self.name = name
        self.age = age
        self.__weight = __weight

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


class student(people):
    grade = ''

    def __init__(self, name, age, __weight, grade) -> None:
        super().__init__(name, age, __weight)
        self.grade = grade

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


if __name__ == '__main__':
    pep = people("alex", 28, 10)
    pep.speak()
    stu = student("alex", 28, 10, 10)
    stu.speak()

    test = sample("Tim", 25, 80, 4, "Python")
    test.speak()  # 方法名同，默认调用的是在括号中参数位置排前父类的方法
