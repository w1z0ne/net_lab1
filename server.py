import socket
import threading
import os
import argparse
import time
import sys
total_time=0
running=True
def handle_client(client_socket, addr):
    print(f"TCP server: request from {addr}")

    # 接收客户端请求的文件名
    file_name = client_socket.recv(1024).decode()
    
    # 检查文件是否存在
    if not os.path.exists(file_name):
        client_socket.send(b"File not found")
    else:
        # 发送文件内容
        print(f"Start to send {file_name} to {addr}")
        with open(file_name, 'rb') as file:
            while True:
                bytes_read = file.read(1024)
                if not bytes_read:
                    break
                client_socket.sendall(bytes_read)
        
        print(f"Successfully send {file_name} to {addr}")

    # 关闭连接
    client_socket.close()

def server_main(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(20)
    print(f"I am a file server, enter q to quit")
    global running
    while running:
        try:
            client_socket, addr = server_socket.accept()
            if running:  # 检查是否仍然需要运行
                client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
                client_thread.start()
            else:
                break
        except socket.error:
            break

def user_input_thread(ip,port):
    global running
    while True:
        user_input = input()
        if user_input == 'q':
            running=False
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, port))
            break

if __name__ == "__main__": 
    ip = '0.0.0.0'  # 监听所有可用的接口
    port = 2680      # 服务器端口
    input_thread = threading.Thread(target=user_input_thread,args=(ip,port))
    input_thread.start()
    server_main(ip, port)
