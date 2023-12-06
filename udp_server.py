
import socket

PORT = 8080
MAXLINE = 1024
ADDR = ("", PORT)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDR)

while True:
    data, addr = sock.recvfrom(MAXLINE)
    print("Client:", data.decode())
    sock.sendto(b"Hello from server", addr)
