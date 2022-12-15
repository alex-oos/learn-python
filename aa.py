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
#    @Time : 2022/12/12 22:04
#    @FIle： aa.py
#    @Software: PyCharm
import socket

import bs4
import requests


def get_local_ip():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 连接谷歌的dns服务器
    client.connect(("8.8.8.8", 80))
    ip, _ = client.getsockname()  # 获取套接字自己的地址,返回元组,ip地址和端口号
    client.close()
    return ip


def get_ip():
    res = requests.get('http://ip111.cn')
    res.encoding = 'utf-8'
    get_content(res.text)

def get_content(html_doc):
    soup =bs4.BeautifulSoup(html_doc,'html')
    soup.prettify()
    print(soup)

if __name__ == '__main__':
    get_ip()
