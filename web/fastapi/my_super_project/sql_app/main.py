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
#    @FIle： main.py
#    @Software: PyCharm
from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

"""
    创建依赖项¶
    现在使用我们在sql_app/database.py文件中创建的SessionLocal来创建依赖项。
    我们需要每个请求有一个独立的数据库会话/连接（SessionLocal），在所有请求中使用相同的会话，然后在请求完成后关闭它。
    然后将为下一个请求创建一个新会话。
    为此，我们将创建一个新的依赖项yield，正如前面关于Dependencies withyield的部分中所解释的那样。
    我们的依赖项将创建一个新的 SQLAlchemy SessionLocal，它将在单个请求中使用，然后在请求完成后关闭它
"""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
    注意引用依赖的时候是引用函数，在python中函数也是一个对象，所以不需要加括号
"""


@app.post('/add/users', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get('/query/user/{user_id}', response_model=schemas.User)
def query_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='user not found')
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)
