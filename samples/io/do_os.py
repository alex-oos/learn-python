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
#    @Time : 2020/9/8 14:01
#    @FIle： do_os.py
#    @Software: PyCharm

"""
os 模块里面有两个方法：
rename()方法：
rename()方法需要两个参数，当前的文件名和新文件名。
语法：os.rename(current_file_name, new_file_name)

"""

import  os
# 重命名testv1 为test2
f = open("test.txt","w")
f.close()
os.rename("test.txt","11.txt")

# remove()方法
# 你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。
#
# 语法：
#
# os.remove(file_name)

# 删除一个已经存在的文件test2.txt
os.remove("11.txt")

# mkdir()方法
# 可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
#
# 语法：
#
# os.mkdir("newdir")

os.mkdir("test")

# chdir()方法
# 可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
#
# 语法：
#
# os.chdir("newdir")

# os.chdir("data/newdir")

"""
getcwd()方法：

getcwd()方法显示当前的工作目录。

语法：
"""

print(os.getcwd())

"""
rmdir()方法
rmdir()方法删除目录，目录名称以参数传递。

在删除这个目录之前，它的所有内容应该先被清除。
语法：

os.rmdir('dirname')
"""

os.rmdir("test")

# 打印出环境变量
# print(os.environ)
print(os.path)