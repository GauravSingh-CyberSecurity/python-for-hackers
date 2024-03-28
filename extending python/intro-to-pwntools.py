'''
pip install pwntools
https://pypi.org/project/pwntools/
https://docs.pwntools.com/en/stable/globals.html
https://docs.pwntools.com/en/stable/index.html
'''


from pwn import *

print(cyclic(50))
print(cyclic_find("laaa"))

print(shellcraft.sh())
print(hexdump(asm(shellcraft.sh())))

'''
p = process("/bin/sh")
p.sendline("echo hello;")
p.interactive()
'''

'''
#click Run button then split the terminal
# in second terminal execute nc -lp 1234
#in first terminal click Run button again 'voila you are connected'

r = remote("127.0.0.1",1234)
r.sendline("hello!")
r.interactive()
r.close()

'''

print("-----------------")
print(p32(0x13371337))
print("-----------------")
print(hex(u32(p32(0x13371337))))

l = ELF('/bin/bash')

print(hex(l.address))
print(hex(l.entry))

print(hex(l.got['write']))
print(hex(l.plt['write']))

for address in l.search(b'/bin/bash\x00'):
    print(hex(address))

print(hex(next(l.search(asm('jmp esp')))))

r = ROP(l)
print(r.rbx)

print(xor(xor("A","B"),"A"))
print(b64e(b"test"))
print(b64d(b"dGVzdA=="))
print(md5sumhex(b"hello"))
print(sha1sumhex(b"hello"))

print(bits(b'a'))
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))
