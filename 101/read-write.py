f = open('/home/gaurav/Downloads/ssh_passwd.txt')
print(f)

f = open('/home/gaurav/Downloads/ssh_passwd.txt','rt')
print(f)

print(f.readlines())
print(f.readlines())

f.seek(0)
print(f.readlines())

f.seek(0)
for line in f:
    print(line.strip())

f.close()

f = open("test.txt","a")
f.write("test line two!")
f.close()

print(f.name)
print(f.closed)
print(f.mode)

with open('/home/gaurav/Downloads/rockyou.txt',encoding= 'latin-1') as f :
    for line in f :
        pass
