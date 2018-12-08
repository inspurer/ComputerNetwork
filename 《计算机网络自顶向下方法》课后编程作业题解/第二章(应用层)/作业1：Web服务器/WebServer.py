from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("127.0.0.1",9999))
serverSocket.listen(1)
# 没有客户端链接时一直在此阻塞
connectionSocket, addr = serverSocket.accept()
while True:
    print('waiting for connection...')
    try:
        #接收1k数据
        data = connectionSocket.recv(1024)
        print(data)
        if not data:
            continue
        #data是一个get的http请求报文
        filename = data.split()[1] #filename = /HelloWorld.html
        # #print(filename[1:])
        f = open(filename[1:],encoding="utf-8") #f = HelloWorld.html
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        #回复报文
        connectionSocket.send(header.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

    except IOError:
        header = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
        connectionSocket.send(header.encode())
        connectionSocket.close()
# 浏览器键入 localhost:***/index.html会有两个请求
# index.html && favicon.ico(网站的图标)