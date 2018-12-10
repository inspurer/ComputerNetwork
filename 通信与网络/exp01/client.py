# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/6
# file_name:        client.py
# description:      月小水长，热血未凉

from socket import *

from logger import logger

clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect(("10.10.16.154",12001))

while True:
    # python3 utf-8编码一个中文居然是三个字节，gbk是两个
    receiveMessage = clientSocket.recv(1024)
    #print(receiveMessage)
    if not receiveMessage:
        clientSocket.close()
        break
    receiveMessage = receiveMessage.decode("utf-8")
    logger.info("已收到"+receiveMessage)
    print(receiveMessage)