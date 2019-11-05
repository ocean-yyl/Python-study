import socket

udpClient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addr = ('127.0.0.1',8888)

while True:
    data = input("输入要发送的数据：")
    udpClient.sendto(data.encode("utf-8"),addr)
    info = udpClient.recv(1024).decode("utf-8")
    print("接受到服务器返回消息：",info)