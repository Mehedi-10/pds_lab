
import socket

PORT = 15050
NET_BUF_SIZE = 32
ADDR = ("", PORT)

def cipher(ch):
    return chr(ord(ch) ^ ord('S'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDR)

while True:
    filename, addr = sock.recvfrom(NET_BUF_SIZE)
    filename = filename.decode()
    print("File Name Received:", filename)
    try:
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(NET_BUF_SIZE)
                if not chunk:
                    break
                encrypted_chunk = ''.join(cipher(ch) for ch in chunk.decode())
                sock.sendto(encrypted_chunk.encode(), addr)
            # Send a signal to denote file transmission is complete
            sock.sendto(b'EOF', addr)
    except FileNotFoundError:
        sock.sendto(b"File Not Found!", addr)
