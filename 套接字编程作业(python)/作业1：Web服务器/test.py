from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("127.0.0.1",9999))
serverSocket.listen(1)
while True:
    print(6)
    connectionSocket, addr = serverSocket.accept()
    print(8)
    try:
        print(10)
        data = connectionSocket.recv(1024)
        print(12)
        print(data)
        filename = data.split()[1] #filename = /HelloWorld.html
        print(15)
        f = open(filename[1:]) #f = HelloWorld.html
        outputdata = f.read()
        print(18)
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(header.encode())
        print(21)
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
        print(25)
    except IOError:
        print("error")
        header = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
        connectionSocket.send(header.encode())
        connectionSocket.close()
        #serverSocket.close()
# 这份代码的缺陷在于,当在浏览器输入 localhost:10000/index.html 并回车后,
# 就会建立起一条链接,然后服务器在套接字读数据,
# 由于链接是keep:alive的,如果不出错误这条链接一直会存在
# 服务器端的while循环一直尝试从套接字接口读数据,
# 然而当请求处理完后，再从缓冲区读数据就会使len(data)==0,
# 从而出现IO异常,serverSocket.close(),pycharm出错：OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。
# 事实上浏览器还默认请求的了网站的图标 favicon.ico，把最后一行代码去掉才会出现上述的情况

