import socket
import keyboard  # 导入keyboard库
import threading  # 导入threading库

HOST = '192.168.246.202'
PORT = 8088

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 请求连接
s.connect((HOST, PORT))

def send_message():
    while True:
        if keyboard.is_pressed('enter'):  # 检查是否按下enter键
            continue  # 如果按下enter键，则继续检查
        cmd = keyboard.read_event()  # 读取键盘事件
        # 只在按下字符键时发送消息
        if cmd.event_type == keyboard.KEY_DOWN and cmd.name not in ['enter', 'shift', 'ctrl', 'alt']:
            # 发送字符到服务端
            s.send(cmd.name.encode('utf-8'))
            print("Sent:", cmd.name)  # 打印发送的消息

# 启动发送消息的线程
threading.Thread(target=send_message, daemon=True).start()

while True:
    data = s.recv(1024)
    # 解码并打印服务端返回的消息
    print("Received:", data.decode('utf-8'))

# 关闭连接
s.close()
