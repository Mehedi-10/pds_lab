import socket
import threading

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def start_client(server_host='127.0.0.1', server_port=65432):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input("")
        client.send(message.encode("utf-8"))

if __name__ == "__main__":
    start_client()
