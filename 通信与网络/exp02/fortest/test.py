# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/8
# file_name:        test.py
# description:      月小水长，热血未凉

a = "1000"

b = "0011"


d = bytes("这是第0001帧",encoding="utf-8")

print(len(d),d)

e = {
    'f':1
}
f = e

f['f'] = 2

print(e['f'],f['f'])