# coding:utf-8
# 功能：客户端实现
# 时间：2023-03-07
import socket
HOST = '192.168.246.202'
PORT = 8088

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 请求连接
s.connect((HOST, PORT))

while True:
    cmd = input("Please input msg:")
    # 编码
    s.send(cmd.encode('utf-8'))
    data = s.recv(1024)
    # 解码
    print(data.decode('utf-8'))

    #s.close()

