# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/9
# file_name:        client.py
# description:      月小水长，热血未凉

from socket import *

if __name__ == "__main__":
    serverName = '127.0.0.1'
    serverPort = 13000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    while True:
        echoMessage = input("请输入:")
        clientSocket.send(echoMessage.encode("utf-8"))
        print("来自服务端的应答",clientSocket.recv(1024).decode("utf-8"))
        #发出关闭连接命令,服务端收到并回复后立即关闭
        if echoMessage.upper() == "BYE":
            break