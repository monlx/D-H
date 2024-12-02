from socket import *
if __name__ == '__main__':
    print('------服务端------')
    p = int(input("请输入公开的质数p:"))
    g = int(input(f"请输入{p}的原根g:"))
    privateKey = input("输入你的私钥：")
    privateKey = int(privateKey)
    publicKey = pow(g, privateKey) % p
    print(f'服务端公钥计算过程：\n{publicKey}={g}^{privateKey}%{p}')
    # 启动服务端
    server_socket = socket(AF_INET, SOCK_STREAM)
    host = gethostbyname(gethostname())
    print(host)
    server_socket.bind((host, 54321))
    server_socket.listen(1)
    print('等待连接...')
    conn, addr = server_socket.accept()
    print('连接来自：', addr)
    # 发送公钥给客户端
    print(f"发送公钥：{publicKey}")
    conn.send(str(publicKey).encode())
    # 接收客户端消息并打印
    counter_publicKey = conn.recv(1024)
    print(f"客户端公钥: {int(counter_publicKey.decode())}")
    Ks = pow(int(counter_publicKey), privateKey) % p
    print(f'会话密钥计算过程：\n{Ks}={int(counter_publicKey)}^{privateKey}%{p}')
    print(f"会话密钥：{Ks}")
