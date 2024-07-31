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
#    @Time : 2023/4/1 20:07
#    @FIle： database.py
#    @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
数据库的一些配置 这里默认使用的是mysql数据库
"""
# 为 SQLAlchemy 定义数据库 URL地址¶
# 配置数据库地址：数据库类型+数据库驱动名称://用户名:密码@机器地址:端口号/数据库名
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/fastapi"
# 创建 SQLAlchemy 引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'charset': 'utf8'})
# 创建一个SessionLocal类
# 每个实例SessionLocal都会是一个数据库会话。当然该类本身还不是数据库会话。
# 但是一旦我们创建了一个SessionLocal类的实例，这个实例将是实际的数据库会话。
# 我们命名它是SessionLocal为了将它与我们从 SQLAlchemy 导入的Session区别开来。
# 稍后我们将使用Session（从 SQLAlchemy 导入的那个）
# 要创建SessionLocal类，请使用函数sessionmaker：
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 创建一个Base类
# # 现在我们将使用declarative_base()返回一个类
# # 稍后我们将用这个类继承，来创建每个数据库模型或类（ORM 模型）：
Base = declarative_base()
