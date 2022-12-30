#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    @Author : tangkaize
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#    @Time : 2022/12/30 21:41
#    @FIle： demo29.py
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class User(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.post('/users/me')
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


if __name__ == '__main__':
    uvicorn.run('demo29:app', host='0.0.0.0', port=8000, reload=True)
