# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/8
# file_name:        client.py
# description:      月小水长，热血未凉

from socket import *
from util import setFCS,fragmentChecker
from constant import segmentFlag,segmentUA,segmentSABM,segmentAddr,segmentDISC,dataDemo,i2s

import json
import time

def establish(clientSocket,fragmentCounter):
    while True:
        sendData = setFCS(dataDemo)

        clientSocket.send(json.dumps(sendData).encode("utf-8"))
        # sleep的原因是让确保服务端按照一帧一帧的格式来接收数据
        time.sleep(1)
        try:
            receivedData = clientSocket.recv(1024)
            receivedData = receivedData.decode("utf-8")
            receivedData = json.loads(receivedData)
            if not fragmentChecker(receivedData):
                continue
            if segmentUA in receivedData.values():
                fragmentCounter = 0
                print("已收到UA帧")
                print("链接已建立...\n")
                break
        except:
            pass

def getSendData():
    data = []
    for i in range(8):
        data.append({
            "Fs": segmentFlag,  # Flag_start
            "A": segmentAddr,
            "C": "0"+i2s.get(str(i))+"1"+i2s.get(str(fragmentCounter)),
            "I": "这是第"+str(i)+"帧",
            "FCS": "00000000",
            "Fe": segmentFlag  # Flag_end
        })
        data[i] = setFCS(data[i])
    return data



def infoSender(clientSocket,fragmentCounter):
    # 开始发送数据帧,采用停等协议
    sendData = getSendData()
    endFlag = False
    for i, item in enumerate(sendData):
        sendDataItem = json.dumps(item).encode("utf-8")
        clientSocket.send(sendDataItem)
        print("发送了数据帧"+str(i))
        time.sleep(1)

        while True:
            try:
                receivedData = clientSocket.recv(1024)
                receivedData = receivedData.decode("utf-8")
                receivedData = json.loads(receivedData)
                if not fragmentChecker(receivedData):
                    print("从接收端接收到的确认帧验证失败")
                    continue

                C = receivedData.get('C')
                #如果是 RR(接收好)帧
                if C.startswith("1000"):
                    #接收状态计数器加一
                    fragmentCounter += 1
                    if fragmentCounter is 8: # fragment == i + 1
                        endFlag = True
                        break
                    sendData[i+1]["C"] = "0"+i2s.get(str(i+1))+"1"+i2s.get(str(fragmentCounter))
                    sendData[i+1] = setFCS(sendData[i+1])
                    break

                if C.startswith("1100"):
                    endFlag = True
                    break
            except:
                pass

        if endFlag:
            break


if __name__ == "__main__":
    clientSocket = socket()
    clientSocket.connect(("127.0.0.1", 9920))
    fragmentCounter = 0

    establish(clientSocket,fragmentCounter)
    infoSender(clientSocket,fragmentCounter)