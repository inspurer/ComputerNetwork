# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/6
# file_name:        server.py
# description:      月小水长，热血未凉

from socket import *
from logger import logger

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('10.10.21.222',12000))

serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()
    print("已与:",addr,"建立连接")
    while True:
        for i in range(100):
            sendMessage = "数字" + str(i+1)
            connectionSocket.send(sendMessage.encode("utf-8"))
            logger.info('已发送'+sendMessage)


    connectionSocket.close()
# send()是阻塞的，发送完数据才返回
# https://www.cnblogs.com/wanzaiyimeng/p/4105937.html
# https://bbs.csdn.net/wap/topics/220012702