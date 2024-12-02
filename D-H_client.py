from socket import *
if __name__ == '__main__':
    print('------客户端------')
    p = int(input("请输入公开的质数p:"))
    g = int(input(f"请输入{p}的原根g:"))
    privateKey = input("输入你的私钥：")
    privateKey = int(privateKey)
    publicKey = pow(g, privateKey) % p
    print(f'客户端公钥计算过程为：\n{publicKey}={g}^{privateKey}%{p}')
    # 连接到服务端
    host = '192.168.130.213'
    conn = socket(AF_INET, SOCK_STREAM)
    conn.connect((host, 54321))
    print('连接到：', host)
    # 发送公钥给服务端
    print(f"发送公钥：{publicKey}")
    conn.send(str(publicKey).encode())
    # 接收服务端消息并打印
    counter_publicKey = conn.recv(1024)
    print(f"对方公钥: {counter_publicKey.decode()}")
    Ks = pow(int(counter_publicKey), privateKey) % p
    print(f'会话密钥计算过程为\n {Ks}={int(counter_publicKey)}^{privateKey}%{p}')
    print(f"会话密钥：{Ks}")
