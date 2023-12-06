
import socket

PORT = 5000
ADDR = ("", PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADDR)
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print("Connected to Client", addr)
    data = conn.recv(1024)
    print("Message from Client:", data.decode())
    conn.send(data)
    conn.close()
