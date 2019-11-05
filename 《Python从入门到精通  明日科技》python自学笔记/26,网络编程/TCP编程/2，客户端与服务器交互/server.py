import socket

# 创建一个socket
server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定ip端口
server.bind(('127.0.0.1',8888))

# 监听
server.listen(5)

print("服务器启动...")
"""
while True:
    # 等待连接
    clientSocket,clientAddr = server.accept()
    # 启动一个线程，将当前连接的socket借给线程
"""

# 等待连接
clientSocket,clientAddr = server.accept()
try:
    while True:
        # 接收客户端的数据
        data  = clientSocket.recv(1024).decode("utf-8")
        print("接收到来自%s的数据：%s" % (clientAddr,data))
        clientSocket.send(("接收到来自%s的数据：%s" % (clientAddr,data)).encode("utf-8"))
except ConnectionResetError:
    print("断开连接，客户端关闭连接")
