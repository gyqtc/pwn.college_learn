mov rax, [rax]
mov rdi, [rax]
mov rax, 60
syscall
# 首先读取rax寄存器存储的内容，该内容代表某个地址，再读取这个地址中代表的值，将其传递给rdi寄存器
