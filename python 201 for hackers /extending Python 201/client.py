'''
run client script after server script by executing  " python3 client.py " in 2nd terminal(of split terminal)
'''

import socket
import threading

def client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input(f"Enter message for {host}:{port}: ")
        client_socket.send(message.encode())
        response = client_socket.recv(1024)
        print(f"Response from {host}:{port}: {response.decode()}")

def main():
    # List of server addresses and ports
    servers = [("127.0.0.1", 8080), ("127.0.0.1", 8081)]

    # Create a client thread for each server
    for server in servers:
        host, port = server
        client_thread = threading.Thread(target=client, args=(host, port))
        client_thread.start()

if __name__ == "__main__":
    main()

