import time
from socket import *
serverName = '127.0.0.1' # 主机
serverPort = 12000
# 创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
# SOCK_DGRAM指定了这个Socket的类型是UDP
# SOCK_STREAM指定使用面向流的TCP协议
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1) # 设置超时时间为1s
for i in range(0, 10):
    oldTime = time.time()
    sendTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(oldTime))
    # encode()把str转成bytes,传输格式要求
    message = ('package %d,client_local_time:%s' % (i + 1, sendTime)).encode()
    try:
        # 发送数据
        clientSocket.sendto(message, (serverName, serverPort))
        # 1024指定要接收的最大数据量为1kb = 1024 bytes
        # recvfrom是一个系统调用，由用户态转向系统态，从套接口上接收数据，并捕获数据发送源的地址。
        # 如果数据报大于缓冲区，那么缓冲区中只有数据报的前面部分，其他的数据都丢失了，并且recvfrom()函数返回WSAEMSGSIZE错误
        # 如果没有数据待读，那么除非是非阻塞模式，不然的话套接口将一直等待数据的到来，果没有在Timeout = 1s内接收到数据，此时将返回SOCKET_ERROR错误，错误代码是WSAEWOULDBLOCK。用select()或WSAAsynSelect()可以获知何时数据到达
        # UDP的 recvfrom() 和 TCP 的recv()不一样,具体可以看 TCP Ping项目
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        # 计算往返时间
        rtt = time.time() - oldTime
        # decode 把bytes转成str
        modifiedMessage = modifiedMessage.decode("utf-8")
        print('报文 %d 收到来自 %s 的应答: %s,往返时延(RTT) = %fs' % (i+1, serverName,modifiedMessage, rtt))
    except Exception as e:
        print('报文 %d: 的请求超时' % (i+1)) # 处理异常
