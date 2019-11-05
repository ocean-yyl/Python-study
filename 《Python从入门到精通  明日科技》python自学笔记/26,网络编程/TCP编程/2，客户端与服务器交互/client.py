import socket

# 创建一个socket
client  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',8888))

while True:
    data = input("输入要发送的数据：")
    client.send(data.encode("utf-8")) # 网络上传输数据不可以是字符串，而只能是字节
    info = client.recv(1024)
    print("接受服务器数据：",info.decode("utf-8"))


