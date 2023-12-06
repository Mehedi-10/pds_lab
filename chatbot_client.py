import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        print("Connected to chatbot. Type 'bye' to exit.")

        while True:
            message = input("You: ")
            client.sendall(message.encode('utf-8'))
            if message.lower() == 'bye':
                break
            response = client.recv(1024).decode('utf-8')
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_client()
