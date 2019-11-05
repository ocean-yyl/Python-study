#encoding=utf-8
#tcp-server 多线程

from socket import *
import threading
import time

MAX_TO_CONN = 3
BUFSIZ = 1024
CODING = 'utf-8'
HOST='0.0.0.0'
PORT=21566

class Server(threading.Thread):

    def __init__(self, host=HOST, port=PORT):
        """
        :param host: ip of server
        :param port: port of the server
        """
        super().__init__()
        self.serv_host = host
        self.serv_port = port
        self.tcpS = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
        self.tcpS.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 加入socket配置，重用ip和端口
        self.tcpS.bind((host,port))  # 绑定ip端口号
        self.tcpS.listen(MAX_TO_CONN)  # 设置最大链接数

    def deal_client(self,conn, addr):

        def send_client_msg(send_msg):
            conn.send(str(len('{}'.format(send_msg).encode(CODING))).encode(CODING))  # 发送msg的字节长度给已链接客户端
            conn.send(send_msg.encode(CODING))  # 发送消息给已链接客户端

        while True:
            data = ""
            try:
                data_size = conn.recv(BUFSIZ).decode(CODING)  # 获取接收数据的字节长度
                while len(data.encode(CODING)) < int(data_size):  # 持续接收数据
                    data += conn.recv(BUFSIZ).decode(CODING)  # msg form server
            except Exception:
                print("error while receive from client {},close the socket\n".format(addr))
                break
            else:
                if data == "exit()":
                    print("receive exit() form {},close the socket\n".format(addr))
                    break
                msg = '{} server receive context form {}:>{}'.format(time.strftime("%Y-%m-%d %X"),addr, data)
                print(msg)
                send_msg = "s" * 2048 + "拥有了"
                send_client_msg(send_msg)
        conn.close()  # 关闭客户端链接

    def run(self):
        print("server strat success，listening...")
        while True:
            conn, addr = self.tcpS.accept()
            print("add client->", addr)
            client = threading.Thread(target=self.deal_client, args=(conn, addr))
            client.start()



if __name__ == '__main__':
    serv = Server()
    serv.run()
