import base64
from pwn import *

s = "8RfZxh9BKr0="
p = process('/challenge/runme')
ans = base64.b64decode(s)
p.send(ans)
res = p.recvall()
print(res)
