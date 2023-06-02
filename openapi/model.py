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
#    @FIle： model.py
#    @Software: PyCharm
#    @Description: 获取model 模型


import openai

openai.api_key = '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'

# openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())
