import socket
import threading

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    connected = True
    while connected:
        message = conn.recv(1024).decode('utf-8')
        if message:
            print(f"[{addr}] {message}")
            response = chatbot_response(message)
            conn.sendall(response.encode('utf-8'))
    conn.close()

def chatbot_response(message):
    # Simple chatbot logic
    if "hello" in message.lower():
        return "Hello! How can I assist you today?"
    elif "bye" in message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."

def start_server(host='127.0.0.1', port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Chatbot Server is listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.activeCount() - 1}")

if __name__ == "__main__":
    start_server()
