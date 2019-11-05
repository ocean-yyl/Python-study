import socket

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(('127.0.0.1',8888))

print("服务器启动...")
while True:
    data, addrClient = udpServer.recvfrom(1024)
    logging = "接受来自客户端%s的消息：%s" % (addrClient , data.decode("utf-8"))
    print(logging)
    udpServer.sendto(logging.encode("utf-8"), addrClient)
