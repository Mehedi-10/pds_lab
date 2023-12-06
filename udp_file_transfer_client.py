
import socket

SERVER_ADDR = ("127.0.0.1", 15050)
NET_BUF_SIZE = 32

def cipher(ch):
    return chr(ord(ch) ^ ord('S'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Please enter file name to receive: ")
sock.sendto(filename.encode(), SERVER_ADDR)

while True:
    data, _ = sock.recvfrom(NET_BUF_SIZE)
    if data.decode() == 'EOF':
        break
    decrypted_data = ''.join(cipher(ch) for ch in data.decode())
    print(decrypted_data, end='')
