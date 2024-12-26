#coding=utf-8
import paho.mqtt.client as mqtt
import time
import sys
import importlib
importlib.reload(sys)

Topic=100
xiaoxi=100
Topic=input("请输入机器编号：")
HOST = "xxx.xxx.xxx.xxx"
PORT = 1883
def client_loop():
    client_id = "0bd981c5-a055-4196-8b7f-efb9f7a4d6ac"
    client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
    client.username_pw_set("xxx", "xxxxxxx")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    client.subscribe(Topic)

def on_message(client, userdata, msg):
    xiaoxi = msg.payload.decode("utf-8")
    #print(xiaoxi)
    if xiaoxi=="11":
        print("主人，已打开第一路开关")
        client.publish(Topic, 1, 2)
    if xiaoxi=="10":
        print("主人，已关闭第一路开关")
        client.publish(Topic, 0, 2)
    
while True:
    client_loop()
    