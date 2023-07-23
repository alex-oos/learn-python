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
#    @Time : 2023/7/23 12:58
#    @FIle： google-code.py
#    @Software: PyCharm
import onetimepass

secret_key = 'WPXCGKUGJPVTRUK5'

# 生成 TOTP 验证码
otp = onetimepass.get_totp(secret_key)

# 输出验证码
print("Google Authenticator Code:", otp)
