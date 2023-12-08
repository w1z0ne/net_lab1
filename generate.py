import os
import random
import argparse


def gen(length,fileName):
    with open(f"jntm.txt", "w") as file:
        a=["猪猪侠","超人强","菲菲公主","小呆呆"]
        for j in range(0,length):
            i=random.randint(0,3)
            file.write(a[i])
            if j%10==0:
                file.write('''
''')

if __name__=="__main__":
    len=9999
    #gen(len)
    # 创建解析器
    parser = argparse.ArgumentParser(description="A simple argument parser")
    parser.add_argument()
    # 添加参数
    parser.add_argument("echo", help="echo the string you use here")
    parser.add_argument("name", help="echo the string you use here")
    # 解析参数
    args = parser.parse_args()
    gen(int(args.echo),)