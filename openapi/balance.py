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
#    @Time : 2023/8/3 上午11:07
#    @FIle： balance.py
#    @Software: PyCharm
import requests


def check_api_key_balance(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get("https://api.openai.com/v1/account", headers=headers)
        response.raise_for_status()
        data = response.json()
        balance = data['data'][0]['attributes']['balance']
        print(f"Your API key balance is: {balance}")
    except requests.exceptions.RequestException as e:
        print("Error occurred while querying the API:", e)

# 替换 YOUR_API_KEY 为你自己的 OpenAI API key
your_api_key = "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"
check_api_key_balance(your_api_key)