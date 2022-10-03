#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])

print('d[\'Tracy\'] =', d['Tracy'])
# 取出里面的值，如果没有默认返回-1
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

ddict = {'Hello': 10}

# 取出里面的值
print('ddict[\'Hello\'] =', ddict['Hello'])

print(ddict.get('Hello'))

# 判断值是否存在在字典里面，如果存在返回True，否则返回False
tmp = 'Hello' in ddict
print(tmp)

# 删除一个值
ddict.pop('Hello')
print(ddict)
