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
#    @Time : 2023/8/4 23:32
#    @FIle： dasd.py
#    @Software: PyCharm

from loguru import logger

my_dict = {"name": "John", "age": 30, "city": "New York"}

# logger.debug("ss", my_dict)
logger.debug("The dictionary content is: %s", my_dict)
