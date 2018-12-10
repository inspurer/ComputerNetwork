# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/9
# file_name:        server.py
# description:      月小水长，热血未凉

from socket import *
import select

def echoHandler(connectionSocket,rList):
    try:
        echoMessage = connectionSocket.recv(1024)
        connectionSocket.send(echoMessage)
        if echoMessage.decode("utf-8").upper() == "BYE":
            print("客户端",connectionSocket.getsockname(),"已断开连接")
            rList.remove(connectionSocket)
            connectionSocket.close()
    except:
        pass
if __name__ == "__main__":
    # 创建服务套接字
    # AF_INE指明是ipv4,如果指明要ipv6需要使用AF_INET
    # SOCK_STREAM指明是基于TCP,如果基于UDP需要使用SOCK_DGRAM
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 将服务套接字绑定到本机的12000号端口
    serverSocket.bind(('127.0.0.1', 13000))


    # 最大连接数为10
    serverSocket.listen(10)
    #服务套接字接收客户端的连接请求,并返回连接套接字和地址
    # windows下python禁用fork(),所以我采用select

    rList = [serverSocket]   # 可读描述符列表
    wList = []               # 可写描述符列表
    eList = []               # 错误描述符列表

    print("等待客户端连接......")
    while True:
        """
        select()，有4个参数，前三个必须也就是感兴趣的描述符，第四个是超时时间
        第一个参数：可读描述符列表
        第二个参数：可写描述符列表
        第三个参数：错误信息描述符列表
        对于自己的套接字来说，输入表示可以读取，输出表示可以写入，套接字就相当于一个管道，对方的写入代表你的读取，你的写入代表对方的读取

        select函数返回什么呢？你把感兴趣的描述符加入到列表中并交给select后，当有可读或者有可写或者错误这些描述符就绪后，select就会返回
        哪些就绪的描述符，你需要做的就是遍历这些描述符逐一进行处理。
        """
        readSet, writeSet, errorSet = select.select(rList, wList, eList)

        # 处理描述符可读
        for readAbledSockFD in readSet:
            if readAbledSockFD is serverSocket:
                try:
                    # 因为 select的机理,这里的accept永远不会阻塞，因为是客户端有请求链接，severSocket才会进可读列表
                    connFd, remAddr = serverSocket.accept()
                except Exception as err:
                    """
                    这里处理当三次握手完成后，客户端意外发送了一个RST，这将导致一个服务器错误
                    """
                    print("RST错误")
                    continue
                print("新连接：", connFd.getpeername())
                # 把新连接加入可读列表中
                rList.append(connFd)
            else:
                echoHandler(readAbledSockFD, rList)

        # 处理描述符可写
        for writeAbledSockFd in writeSet:
            pass

        # 处理错误描述符
        for errAbled in errorSet:
            pass
    pass