import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from {client_socket.getpeername()}: {data.decode()}")
        response = input("Enter response: ")
        client_socket.send(response.encode())
    client_socket.close()

def server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[*] Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def main():
    servers = [("127.0.0.1", 8080), ("127.0.0.1", 8081)]
    clients = [("127.0.0.1", 8080), ("127.0.0.1", 8081), ("127.0.0.1", 8081)]

    # Start server threads
    for server_host, server_port in servers:
        server_thread = threading.Thread(target=server, args=(server_host, server_port))
        server_thread.start()

    # Start client threads
    for client_host, client_port in clients:
        client_thread = threading.Thread(target=client, args=(client_host, client_port))
        client_thread.start()

def client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode())
        response = client_socket.recv(1024)
        print(f"Server response: {response.decode()}")

if __name__ == "__main__":
    main()
