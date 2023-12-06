import socket
import threading

def handle_client(conn, addr, clients):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(1024).decode("utf-8")
        if msg:
            print(f"[{addr}] {msg}")
            broadcast_message(msg, conn, clients)
    conn.close()

def broadcast_message(message, sender_conn, clients):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message.encode("utf-8"))
            except:
                pass  # Handle client disconnection

def start_server(host='127.0.0.1', port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[LISTENING] Server is listening on {host}:{port}")

    clients = []
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr, clients))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    start_server()
