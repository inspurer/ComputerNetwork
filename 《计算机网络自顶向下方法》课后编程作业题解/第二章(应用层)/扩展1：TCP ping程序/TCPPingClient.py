import time
from socket import *
serverName = '127.0.0.1' # 主机
serverPort = 12000
# 创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
# SOCK_DGRAM指定了这个Socket的类型是UDP
# SOCK_STREAM指定使用面向流的TCP协议
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.settimeout(1) # 设置超时时间为1s
for i in range(0, 10):
    oldTime = time.time()
    sendTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(oldTime))
    # encode()把str转成bytes
    message = ('package %d,client_local_time:%s' % (i + 1, sendTime)).encode()
    try:
        # 发送数据
        clientSocket.send(message)
        # UDP的 recvfrom() 和 TCP 的recv()不一样,具体可以看 TCP Ping项目
        modifiedMessage = clientSocket.recv(1024)
        # 计算往返时间
        rtt = time.time() - oldTime
        # decode 把bytes转成str
        modifiedMessage = modifiedMessage.decode("utf-8")
        print('报文 %d 收到来自 %s 的应答: %s,往返时延(RTT) = %fs' % (i+1, serverName,modifiedMessage, rtt))
    except Exception as e:
        print('报文 %d: 的请求超时' % (i+1)) # 处理异常

