import socket

def echo_client(host='127.0.0.1', port=65432, message="Hello, Server!"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        client.sendall(message.encode())
        data = client.recv(1024)
        print(f"Received: {data.decode()}")

if __name__ == "__main__":
    echo_client()
