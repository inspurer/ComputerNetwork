import time
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1',12000))

serverSocket.listen(1)

while True:

    connectionSocket, address = serverSocket.accept()
    serverTime = time.time()
    sendTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(serverTime))
    message  = "Server time :" + sendTime
    connectionSocket.send(message.encode())
    connectionSocket.close()
