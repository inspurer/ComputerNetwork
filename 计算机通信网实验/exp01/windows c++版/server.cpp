#include <iostream>
#include <winsock2.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#pragma comment (lib, "ws2_32.lib")  //加载静态库ws2_32.dll
/**
CRT中的一组函数如果使用不当，可能会产生诸如内存泄露、缓冲区溢出、非法访问等安全问题。这些函数如：strcpy、strcat等。
对于这些问题，VC2005建议使用这些函数的更高级的安全版本，即在这些函数名后面加了一个_s的函数。
这些安全版本函数使用起来更有效，也便于识别，如：strcpy_s,calloc_s等。
当然，如果执意使用老版本、非安全版本函数,在程序开头添加, 
#pragma  warning(disable:4996)	 //全部关掉     
#pragma  warning(once:4996)      //仅显示一个
*/      
#pragma warning(disable:4996)
using namespace std;
int main()
{
    WSADATA wsaData;
	int i = 0;
	/**
	socket编程要调用各种socket函数，但是需要库Ws2_32.lib和头文件Winsock2.h，
	这里的WSAStartup就是为了向操作系统说明，我们要用哪个库文件，让该库文件与当前的应用程序绑定，从而就可以调用该版本的socket的各种函数了。
	*/
	/** 头文件 header： 　Winsock2.h
	库library：      Ws2_32.lib
	原型：int   PASCAL   FAR  WSAStartup ( WORD  wVersionRequested, LPWSADATA   lpWSAData );
	参数：wVersionRequested是Windows Sockets API提供的调用方可使用的最高版本号。高位字节指出副版本(修正)号，低位字节指明主版本号。
    lpWSAData 是指向WSADATA数据结构的指针，用来接收Windows Sockets实现的细节。
	*/
    WSAStartup(MAKEWORD(2, 2), &wsaData);
	/**
	声明调用不同的Winsock版本。例如MAKEWORD(2,2)就是调用2.2版，MAKEWORD(1,1)就是调用1.1版。
	不同版本是有区别的，例如1.1版只支持TCP/IP协议，而2.0版可以支持多协议。
	2.0版有良好的向后兼容性，任何使用1.1版的源代码、二进制文件、应用程序都可以不加修改地在2.0规范下使用。
	此外winsock 2.0支持异步 1.1不支持异步.
	*/
    SOCKET array_servSock[10] =	{0};
    //创建套接字,最后一个参数就是指定协议。套接口所用的协议。如调用者不想指定，可用0
    SOCKET servSock = socket(AF_INET, SOCK_STREAM, 0);  
    //绑定套接字
    sockaddr_in sockAddr;
    memset(&sockAddr, 0, sizeof(sockAddr));  //每个字节都用0填充
    sockAddr.sin_family = PF_INET;  //使用IPv4地址
    sockAddr.sin_addr.s_addr = inet_addr("127.0.0.1");  //具体的IP地址
    sockAddr.sin_port = htons(18000);  //端口
    bind(servSock, (SOCKADDR*)&sockAddr, sizeof(SOCKADDR));
    //进入监听状态
    listen(servSock, 20);
    //接收客户端请求
    SOCKADDR clntAddr;
    int nSize = sizeof(SOCKADDR);
  
   
	char str[20] = {0};
	char *str1 = "数字";
	char str2[5] = {0};
    SOCKET clntSock = accept(servSock, (SOCKADDR*)&clntAddr, &nSize);
    while (1)   // 循环发送数据
    {
		for(i=1;i<101;i++)
		{
			//printf("%s1",str);
			strcpy(str,str1);
			itoa(i,str2,10);
			strcat(str,str2);
			//printf("22");
			//printf("%s2",str);
			printf("%s\n",str);
			send(clntSock, str, strlen(str) + sizeof(char), NULL);
			Sleep(100);
			memset(str, 0, strlen(str));  //重置缓冲区
		}

    }
    closesocket(clntSock);  //关闭套接字
    //关闭套接字
    closesocket(servSock);
    //终止 DLL 的使用
    WSACleanup();
    return 0;
}
