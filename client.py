import socket
import argparse
import time
import random

def client_main(host, port, file_name):
    # 创建一个 TCP/IP 套接字
    start_time=time.time()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接到服务器
    client_socket.connect((host, port))

    # 发送请求的文件名
    client_socket.send(file_name.encode())

    # 接收文件内容并保存
    flag=random.randint(0,100000000)
    with open(f"received/{flag}_{file_name}", "wb") as file:
        while True:
            bytes_read = client_socket.recv(1024)
            if not bytes_read:
                # 文件传输完成
                break
            file.write(bytes_read)

    # 关闭套接字
    client_socket.close()
    print(f"File {file_name} received successfully")
    end_time=time.time()
    period=end_time-start_time
    print(f"Use {period}s totally.")

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("ip")
    parser.add_argument("fname")
    args=parser.parse_args()
    ip=args.ip
    port = 2680        # 与服务器相同的端口
    FILE_NAME = args.fname
    client_main(ip, port, FILE_NAME)