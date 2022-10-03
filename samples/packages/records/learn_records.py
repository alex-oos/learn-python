#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    @Author : 李将
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#    @Time : 2020/11/27 16:32
#    @FIle： learn_records.py
#    @Software: PyCharm
import records


def update():
    # 连接数据库
    db = records.Database('mysql+pymysql://test:test123@rm-2zeyoxjy4n606sm1l4o.mysql.rds.aliyuncs.com:3306/lol_crm')
    couseid = input("couseid=")
    print(couseid)
    # 执行的sql
    sql_update = "update lol_mall.product_sku set sale_price = '0.01', b_sale_price = '0.01', price = '0,01' , price2 = '0.01',price3 = '0.01'    , sale_price2 = '0.01' , sale_price3 = '0.01'  where id = (select sku_id from lol_mall.sku_course_relation where course_id={});".format(couseid)
    print(sql_update)
    res_update = db.query(sql_update)
    sql_query = "select * from lol_mall.product_sku where id = (select sku_id from lol_mall.sku_course_relation where course_id= {});".format(couseid)
    res_query = db.query(sql_query).all(as_dict=True)
    print(res_query)
    # res = res[0]
    # print(res['id'])

# 入口
if __name__ == '__main__':
    update()
    # print(result[0])

    # print(res['id'])
    #
    # print(type(result))
    #
    # print(result.all())
    # # 得到所有数据
    # print(result.all())
    # # 字典形式展示
    # print(result.all(as_dict=True))
    # # 获取第一个
    # print(result.first())
    # # 以字典形式获取第一个
    # print(result.first(as_dict=True))
    # # 排序字典
    # print(result.first(as_ordereddict=True))
    # # 查询唯一的一个
    # print(result.one())