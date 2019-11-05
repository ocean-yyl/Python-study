#!/usr/bin/python3
# -*-coding:utf-8 -*-
from socket import *

CODING = "utf-8"
HOST = '192.168.30.211' #服务端ip
PORT = 21566 # 服务端端口号
BUFSIZ = 1024

class Client(object):
    def __init__(self, host=HOST, port=PORT):
        """
        :param host: ip of server
        :param port: port of the server
        """
        self.tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
        self.tcpCliSock.connect((HOST, PORT))  # 连接服务器
        self.payload = "" # 获取的消息暂时为空

    def send_msg(self,msg):
        self.tcpCliSock.send(str(len('{}'.format(msg).encode(CODING))).encode(CODING))  # 发送msg的字节长度给server
        self.tcpCliSock.send(msg.encode(CODING))  # send to server

    def recv_serv_msg(self):
        # 判断一下，一个命令执行后，它返回的数据到底有没有完全传输完毕，如果没有，那么就继续传输，直到传完为止
        data_size = self.tcpCliSock.recv(BUFSIZ).decode(CODING) # 获取接收数据的字节长度
        while len(self.payload.encode(CODING)) < int(data_size): # 持续接收数据
            self.payload += self.tcpCliSock.recv(BUFSIZ).decode(CODING)  # msg form server
        return self.payload

    def ask_server(self,msg):
        self.send_msg(msg)
        return self.recv_serv_msg()

    def __del__(self):
        self.tcpCliSock.send("exit()".encode(CODING))  # tell server to close the socket
        self.tcpCliSock.close()  # close Socket


if __name__ == '__main__':
    data = "y"*1024+"尹业立"
    client = Client()
    print(client.ask_server(data))
