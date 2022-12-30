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
#    @Time : 2022/12/27 15:33
#    @FIle： demo10.py
#    @Software: PyCharm
from datetime import datetime, timedelta, time
from typing import Union
from uuid import UUID

import uvicorn
from fastapi import FastAPI, Body

app = FastAPI()


@app.put('/items/{item_id}')
async def read_items(item_id: UUID, start_datetime: Union[datetime, None] = Body(default=None),
                     end_datetime: Union[datetime, None] = Body(default=None),
                     repeat_at: Union[time, None] = Body(default=None),
                     process_after: Union[timedelta, None] = Body(default=None)):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


if __name__ == '__main__':
    uvicorn.run('demo10:app', host='127.0.0.1', port=8000, reload=True)
