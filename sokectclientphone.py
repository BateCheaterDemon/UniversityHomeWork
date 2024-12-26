import socket

# 手机的IP地址和APP中设置的端口号
HOST = '192.168.246.202'  # 替换为你的手机热点IP
PORT = 4088           # 替换为APP中设置的端口号

# 创建Socket客户端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 连接到手机的Socket服务器
    client_socket.connect((HOST, PORT))
    print("已连接到手机服务器")

    while True:
        # 接收数据
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"接收到的数据: {data}")

except ConnectionRefusedError:
    print("无法连接到手机服务器，请检查IP和端口是否正确")
except Exception as e:
    print(f"发生错误: {e}")
finally:
    # 关闭连接
    client_socket.close()
    print("连接已关闭")
