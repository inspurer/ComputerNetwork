import random
from socket import *
#AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
#SOCK_DGRAM指定了这个Socket的类型是UDP
serverSocket = socket(AF_INET, SOCK_STREAM)
#用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址
serverSocket.bind(('127.0.0.1',12000))

#最多连接一个客户端
serverSocket.listen(1)
# Tcp server需要两个套接字,比UDP Server多了一个用来连接的套接字
connectionSocket, address = serverSocket.accept()

while True:
    #产生一个0到10之间的随机数
    rand = random.randint(0, 10)


    #从已连接的套接口上读取数据，参数为缓冲区大小
    message= connectionSocket.recv(1024)
    # TCP的recv()和UDP的recvfrom()的一个区别是recv()读不到数据会立即返回null，不报错
    # 还有就是如果数据报大于缓冲区,也不会报错，而是会读完
    if not message:
        break

    print("收到来自 %s 的报文: (%s)" % (address,message))
    # 把接收到的信息全部转为大写
    print("随机数是: %d" % rand)
    message = message.upper()
    #如果随机数小于4，服务端无应答,客户端就会超时
    if rand < 4:
        continue
    connectionSocket.send(message)

#参考链接:
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004977916a212e2168e21449981ad65cd16e71201000

#https://blog.csdn.net/rebelqsp/article/details/22109925