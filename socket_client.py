import socket

def start_client(server_host='127.0.0.1', server_port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server_host, server_port))
        client.sendall(b'Hello, server!')
        data = client.recv(1024)
        print(f'Received from server: {data.decode()}')

if __name__ == "__main__":
    start_client()
