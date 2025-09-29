.intel_syntax noprefix
mov rax, 0x1337
mov rsp, 0x31337
mov r12, 0xCAFED00D1337BEEF ; 先设置rsp寄存器的值，再设置r12寄存器的值，因为pwncollege自带检查机制，因此需要先设置防止程序崩溃
