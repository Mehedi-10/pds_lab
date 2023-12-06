
import socket

SERVER_ADDR = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(SERVER_ADDR)

message = input("Enter the Message: ")
sock.send(message.encode())
response = sock.recv(1024)
print("Message from Server:", response.decode())

sock.close()
