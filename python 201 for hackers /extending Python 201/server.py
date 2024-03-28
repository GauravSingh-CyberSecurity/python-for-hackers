import socket

'''
run server script before client script by executing  " python3 server.py " in 1st terminal(split terminal)



run in terminal if port or address are busy:

sudo netstat -tulpn | grep :8080
sudo kill PID

'''

import socket

def server():
    host = "127.0.0.1"
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = s.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received from client: {data.decode()}")
        message = input("Enter your response: ")
        conn.sendall(message.encode())

    conn.close()

if __name__ == "__main__":
    server()
