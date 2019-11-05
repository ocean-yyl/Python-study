import socket

host = 'www.baidu.com'

# 一，创建一个socket
# 参数1：指定协议AF_INET 或 AF_INET6
# 参数2：SOCK_STREAM指定使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 二，建立连接
# 参数：一个元组，第一个元素是服务器地址，第二个元素为端口
sk.connect((host,80))

# 发送数据
sk.send(b'GET / HTTP/1.1\r\nHost: '+ b'www.baidu.com' +b'\r\nConnection: close\r\n\r\n')

# 接受数据，处理接收到的数据
data = []
while True:
    tmp = sk.recv(1024)
    if tmp:
        data.append(tmp)
    else:
        break

dataStr = str(b''.join(data).decode("utf-8"))
print(dataStr)

# 断开连接
sk.close()