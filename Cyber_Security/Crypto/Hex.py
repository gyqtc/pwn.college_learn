from pwn import *

p = process('/challenge/run')
for i in range(10):
    test = p.recvline()
    key = p.recvline()[-5:-1]
    enc = p.recvline()[-5:-1]
    key = int(str(key)[2:-1], 16)
    enc = int(str(enc)[2:-1], 16)
    
    p.sendlineafter(b'Decrypted secret?', hex(key^enc).encode('utf-8'))
    dir = p.recvline()
    print(dir)
    dir1 = p.recvline()
    print(dir1)
    if i == 9:
        flag = p.recvline()
        flag = p.recvline()
        print(flag)
