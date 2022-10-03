#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)
# 需要定义日志的级别，可以输出
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
