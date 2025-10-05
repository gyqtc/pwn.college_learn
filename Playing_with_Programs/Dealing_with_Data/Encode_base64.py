import base64
from pwn import *

p = process('/challenge/runme')
s = b"\x84\x1b\xeb\xf4\x19\x92lt"
ans =base64.b64encode(s)
p.send(ans)
res = p.recvall()
print(res)
