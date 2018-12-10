import socket
HOST = "time.nist.gov"
PORT = 13
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    client.connect((HOST,PORT))
    data = client.recv(1024)
    #字节转字符串
    time = str(data,encoding='utf-8')
    print("the server's time is:",time)
except Exception as e:
    print('Error!')