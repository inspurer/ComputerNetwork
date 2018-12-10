# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/8
# file_name:        server.py
# description:      月小水长，热血未凉

from socket import *
from threading import Thread
from util import fragmentChecker,setFCS
from constant import segmentFlag,segmentUA,segmentSABM,segmentAddr,i2s
import json
import time


# 为简化HDLC协议,所有的帧结构的控制字段(也就是C字节)的P/F位全部置为1
# 规定信息字段为16位

fragmentCounter = 0
def socketHander(connectionSocket,addr):
    global fragmentCounter
    print("已收到{}的请求".format(addr))

    #链路建立阶段
    while True:
        # recv是非阻塞的
        receivedData = connectionSocket.recv(1024)
        if not receivedData:
            print("等待是长情的告白...")
            time.sleep(1)
            continue
        receivedData = receivedData.decode("utf-8")
        print("建链之前:",receivedData)
        receivedData = json.loads(receivedData)
        #如果帧校验不通过，该帧将会被丢失,但是不选择重传,链接建立之后再重传
        if not fragmentChecker(receivedData):
            continue

        #如果收到SABM,建立链路
        if segmentSABM in receivedData.values():
            print("已收到平衡方式帧SABM...\n")
            print("链接已建好...\n")
            data = {
                "Fs": segmentFlag,
                "A": segmentAddr,
                "C": segmentUA,
                "I": "0000000011111111",
                "FCS": "00000000",
                "Fe": segmentFlag
            }
            data = setFCS(data)
            connectionSocket.send(json.dumps(data).encode("utf-8"))
            fragmentCounter = -1
            break

    #进入收发数据的循环
    while True:
        receivedData = connectionSocket.recv(1024)
        if not receivedData:
            print("等待是长情的告白...")
            break
        receivedData = receivedData.decode("utf-8")
        print("建链之后:", receivedData)
        receivedData = json.loads(receivedData)

        # 如果帧校验不通过，该帧将会被丢失,选择重传
        if not fragmentChecker(receivedData):
            print("To do: 发REJ帧")
            #在这里发REJ帧
            continue

        C  = receivedData.get("C")

        #如果是 DISC
        if  C.startswith("1100") and C.endswith("010"):
            #先发送UA
            print("已收到帧DISC...\n")
            print("链接已建好...\n")
            data = {
                "Fs": segmentFlag,
                "A": segmentAddr,
                "C": segmentUA,
                "I": "0000000011111111",
                "FCS": "00000000",
                "Fe": segmentFlag
            }
            data = setFCS(data)
            connectionSocket.send(json.dumps(data).encode("utf-8"))
            break
            #再关闭
            pass

        else:
            # 计数状态器加一
            fragmentCounter += 1
            data = {
                "Fs": segmentFlag,
                "A": segmentAddr,
                "C": "10001"+i2s.get(str(fragmentCounter)),
                "I": "0000000011111111",
                "FCS": "00000000",
                "Fe": segmentFlag
            }
            data = setFCS(data)


            connectionSocket.send(json.dumps(data).encode("utf-8"))
            print("接收到数据:",receivedData.get("I"))

            if fragmentCounter is 7:
                break



if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(("127.0.0.1", 9920))

    #listen()将服务器的连接由主动转成被动
    serverSocket.listen(5)

    while True:
        connectionSocket, addr = serverSocket.accept()
        # 多线程处理并发
        Thread(target=socketHander,args=(connectionSocket,addr)).start()
