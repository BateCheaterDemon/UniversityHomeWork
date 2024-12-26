# coding:utf-8
# 功能：服务端实现
# 时间：2023-03-07
import socket

# 设置IP和端口
HOST = '192.168.246.202'
PORT = 8088
# 创建TCP套接字，绑定IP，建立连接池
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
# 打印IP
print('Server start at: %s:%s' %(HOST, PORT))
print('wait for connection...')
# 接收客户端请求
while True:
    conn, addr = s.accept()
    # 客户端IP
    print('Connected by ', addr)

    while True:
        data_x = conn.recv(1024)
        data_y = conn.recv(1024)
        data_xa=float(data_x.decode('utf-8'))
        data_ya=float(data_y.decode('utf-8'))
        
        print(f"xa={data_xa},ya={data_ya}")
        # print(type(data_xa))

        # conn.send("server received you message.".encode('utf-8'))





