#include <stdlib.h>
#include <WinSock2.h>
#include <stdio.h>
#pragma comment(lib, "ws2_32.lib")  //加载 ws2_32.dll
#pragma warning(disable:4996)
int main()
{
    //初始化DLL
    WSADATA wsaData;
	int re = 0;
    WSAStartup(MAKEWORD(2, 2), &wsaData);//采用的是最新的2.2版本   MAKEWORD（）用以对版本号进行切换，是一个宏函数

    //创建套接字
    SOCKET sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

    //向服务器发起请求
    sockaddr_in sockAddr;
    memset(&sockAddr, 0, sizeof(sockAddr));  //每个字节都用0填充
    sockAddr.sin_family = AF_INET;
    sockAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    sockAddr.sin_port = htons(18000);
    connect(sock, (SOCKADDR*)&sockAddr, sizeof(SOCKADDR));
    //接收服务器传回的数据
    char szBuffer[MAXBYTE] = { 0 };
	while(1){
		    re = recv(sock, szBuffer, MAXBYTE, NULL);
			if(re<0 || re==0)
				break;
			//输出接收到的数据
			printf("Message form server: %s\n", szBuffer);
			memset(szBuffer,0,MAXBYTE);
	}

    system("pause");
    //关闭套接字
    closesocket(sock);
    //终止使用 DLL
    WSACleanup();   
    return 0;
}
