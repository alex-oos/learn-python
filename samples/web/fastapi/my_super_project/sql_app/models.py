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
#    @FIle： models.py
#    @Software: PyCharm


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

"""
    创建数据库模型
    用Base类来创建 SQLAlchemy 模型
    
    注意mysql 中的str需要加入长度，即是：String（20）
"""


class User(Base):
    """
    __tablename__表名
    创建模型属性/列¶
    现在创建所有模型（类）属性。
    这些属性中的每一个都代表其相应数据库表中的一列。
    我们使用Column来表示 SQLAlchemy 中的默认值
    我们传递一个 SQLAlchemy “类型”，如Integer、String和Boolean，它定义了数据库中的类型，作为参数。
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(40))
    is_active = Column(Boolean, default=True)
    # 创建关系
    # 我们使用SQLAlchemy  ORM提供的relationship。这将或多或少会成为一种“神奇”属性，其中表示该表与其他相关的表中的值
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20), index=True)
    description = Column(String(20), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
