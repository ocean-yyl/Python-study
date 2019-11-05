#encoding=utf-8
#tcp-server 多线程

from socket import *
import threading
import time

NUM_TO_LISTEN = 10
BUFSIZ = 1024
CODING = 'utf-8'

class Server(threading.Thread):
    class __ServerSingleton():

        def set_host(self,host="127.0.0.1"):
            self._serv_host=host

        def set_port(self,port=21566):
            if type(port) is not int:
                port = int(port)
            self._serv_port = port

        def __init__(self, host='127.0.0.1', port=21566):
            """
            :param host: ip of server
            :param port: port of the server
            """
            super().__init__()
            self._serv_host = host
            self._serv_port = port

        def deal_client(self,conn, addr):
            while True:
                try:
                    data = conn.recv(BUFSIZ)  # 读取已链接客户的发送的消息
                except Exception:
                    print("接受client信息过程中出错,客户端->", addr,"断开连接")
                    break
                print("receive from",addr,":\n>"+data.decode(CODING))
                if not data:
                    break
                msg = time.strftime("%Y-%m-%d %X")  # 获取结构化事件戳
                msg1 = '[%s]server receive context:\n>%s' % (msg, data.decode(CODING))
                conn.send(msg1.encode(CODING))  # 发送消息给已链接客户端
            conn.close()  # 关闭客户端链接

        def run(self):
            self.tcpS = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
            self.tcpS.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 加入socket配置，重用ip和端口
            self.tcpS.bind((self._serv_host, self._serv_port))  # 绑定ip端口号
            self.tcpS.listen(NUM_TO_LISTEN)  # 设置最大链接数
            print("服务器启动成功，listening...")
            while True:
                conn, addr = self.tcpS.accept()
                print("客户端->", addr,"链接成功!")
                client = threading.Thread(target=self.deal_client, args=(conn, addr))
                client.start()

    instance = None

    def __new__(cls, *args, **kwargs):
        if not Server.instance:
            Server.instance = Server.__ServerSingleton()

        return Server.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)


if __name__ == '__main__':
    serv = Server()
    serv.set_host("127.0.0.1")
    serv.set_port(21566)
    serv.run()
