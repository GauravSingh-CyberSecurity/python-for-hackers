'''
its a bidirectional communication channel
you can send and recive data using sockets 
they can communicate with inner process between process
or between different systems in a network
'''



'''
import socket

ip = socket.gethostbyname('247ctf.com')
print(ip)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("247ctf.com",80))
s.sendall(b"HEAD / HTTP/1.1\r\nHOST: 247ctf.com\r\n\r\n")
print(s.recv(1024).decode())
s.close()


client = False
server = False
port = 8080
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if server:
    s.bind(("127.0.0.1",port))
    s.listen()
    
    while True:
        connect,addr = s.accept()
        connect.send(b"you made it to the socket!")
        connect.close()

if client:
    s.connect(("127.0.0.1",port))
    print(s.recv(1024))
    s.close()

for port in [22, 80, 139, 443, 445, 8080]:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex(("127.0.0.1",port))
    if result == 0:
        print("{} is open".format(port))
    else:
        print("{} is closed!")
    s.close()

#netstat -tulpn
#sudo netstat -tulpn | grep :8080


#we are using putty software to make a connection


'''




import socket

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

def main():
    host = "127.0.0.1"
    ports = [22, 80, 139, 443, 445, 8080]

    for port in ports:
        if check_port(host, port):
            print(f"{port} is open")
        else:
            print(f"{port} is closed")

    ip = socket.gethostbyname('247ctf.com')
    print(ip)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("247ctf.com", 80))
    s.sendall(b"HEAD / HTTP/1.1\r\nHOST: 247ctf.com\r\n\r\n")
    print(s.recv(1024).decode())
    s.close()

if __name__ == "__main__":
    main()
