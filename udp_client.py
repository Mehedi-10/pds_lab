
import socket

SERVER_ADDR = ("127.0.0.1", 8080)
MAXLINE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(b"Hello from client", SERVER_ADDR)
data, _ = sock.recvfrom(MAXLINE)
print("Server:", data.decode())
