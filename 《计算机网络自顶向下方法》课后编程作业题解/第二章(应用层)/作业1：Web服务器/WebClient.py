from socket import *
ClientSocket = socket(AF_INET, SOCK_STREAM)
ClientSocket.connect(('localhost',9999))
while True:
    #这里的Connetction: close不同于浏览器常见的keep-alive,
    #close表示要求服务器在发送完被请求的对象后就关闭这条链接
    Head = '''GET /index.html HTTP/1.1\r\nHost: localhost:9999\r\nConnection: close\r\nUser-agent: Mozilla/5.0\r\n\r\n'''
    ClientSocket.send(Head.encode('utf-8'))
    data = ClientSocket.recv(1024)
    print(data)
    with open("response.html","wb") as f:
        f.write(data)


