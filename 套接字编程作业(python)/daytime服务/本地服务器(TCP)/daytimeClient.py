from socket import *
serverName = '127.0.0.1' # 主机
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

print(clientSocket.recv(1024).decode())
