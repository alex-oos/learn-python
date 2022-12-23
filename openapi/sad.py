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
#    @Time : 2022/12/17 14:58
#    @FIle： sad.py
#    @Software: PyCharm


import openai

openai.api_key = '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'

# openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())
