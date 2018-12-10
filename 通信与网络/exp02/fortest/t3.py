# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/9
# file_name:        t3.py
# description:      月小水长，热血未凉

a = "肖涛"

b = bytes(a,encoding="utf-8")

print(b,type(b))

c = "肖"

d = ord("9")

print(d,type(d))

e = bin(d)

print(e,type(e),len(e))

#综上，汉字转换成二进制
a='好'
print(format(ord(a),'b')) #101100101111101，或者
#101100101111101
print(bin(ord(a)),type(ord(a)))  #0b101100101111101,转换成八进制和十六进制类似
#0b101100101111101

#打印汉字表

# for ch in range(0x4e00,0x9fa6):
#     print(chr(ch))

#其实只要知道汉字是从0x4e00到0x9fa6就已经足够了。

print(str(0x4e00))
print(str(0x9fa6))
