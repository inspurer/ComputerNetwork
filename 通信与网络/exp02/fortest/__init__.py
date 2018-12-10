# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/8
# file_name:        __init__.py
# description:      月小水长，热血未凉

import json
b = bytes("1101",encoding="utf-8")
#返回该字节对应的数，int类型,48
print(b[2])
a = b.decode("utf-8")
# 0
print(a[2])
#https://segmentfault.com/q/1010000009395651/
print(b[2*4:3*4])

c = json.dumps("111")
print(type(c),c)

d = "00000000"
e = d.encode("utf-8")
print(len(e),e)
