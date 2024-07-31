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
#    @FIle： crud.py
#    @Software: PyCharm
from sqlalchemy.orm import Session

import models
import schemas

"""
    CRUD分别为：增加、查询、更改和删除，即增删改查

"""

"""
     读取数据
     从 sqlalchemy.orm中导入Session，这将允许您声明db参数的类型，并在您的函数中进行更好的类型检查和完成。
     导入之前的models（SQLAlchemy 模型）和schemas（Pydantic模型/模式）
"""


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


"""
    创建数据
    使用您的数据创建一个 SQLAlchemy 模型实例。
    使用add来将该实例对象添加到您的数据库。
    使用commit来对数据库的事务提交（以便保存它们）。
    使用refresh来刷新您的数据库实例（以便它包含来自数据库的任何新数据，例如生成的 ID）。
"""


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    # 然后我们将dict的键值对 作为关键字参数传递给 SQLAlchemy Item
    # 然后我们传递 Pydantic模型未提供的额外关键字参数owner_id：
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
