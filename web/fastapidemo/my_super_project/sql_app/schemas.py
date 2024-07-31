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
#    @Time : 2023/4/1 20:08
#    @FIle： schemas.py
#    @Software: PyCharm

from pydantic import BaseModel

"""
    创建 Pydantic 模型¶
    建初始 Pydantic模型/模式
    创建一个ItemBase和UserBasePydantic模型（或者我们说“schema”）以及在创建或读取数据时具有共同的属性。
    ItemCreate为 创建一个UserCreate继承自它们的所有属性（因此它们将具有相同的属性），以及创建所需的任何其他数据（属性）。
    因此在创建时也应当有一个password属性。
    但是为了安全起见，password不会出现在其他同类 Pydantic模型中，例如用户请求时不应该从 API 返回响应中包含它。
"""


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str = 'demo@email.com'


class UserCreate(UserBase):
    password: str = "123456"


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    """
        使用 Pydantic 的orm_mode
        现在，在用于查询的 Pydantic模型Item中User，添加一个内部Config类。此类Config用于为 Pydantic 提供配置。
        在Config类中，设置属性orm_mode = True
        Pydantic orm_mode将告诉 Pydantic模型读取数据，即它不是一个dict，而是一个 ORM 模型（或任何其他具有属性的任意对象）
    """

    class Config:
        orm_mode = True
