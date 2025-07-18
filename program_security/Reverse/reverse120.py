from pwn import *

# 切换到challenge目录后连接到程序
p = process('./babyrev-level-12-0')  # 或者 remote('host', port)

# 发送正确的6字节
payload = p8(0xC0) + p8(0xB6) + p8(0xF6) + p8(0x20) + p8(0x2C) + p8(0x26)
p.send(payload)

# 接收并打印结果
response = p.recvall()
print(response.decode())
