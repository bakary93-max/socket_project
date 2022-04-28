import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connexion on servor {HOST_IP}, port {HOST_PORT}")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERROR: impossible to connect on server. Reconnect...")
        time.sleep(4)
    else:
        print("Connexion established")
        break

while True:
    received_data = s.recv(MAX_DATA_SIZE)
    if not received_data:
        break
    print("Message: ", received_data.decode())
    text_sent = input("You: ")
    s.sendall(text_sent.encode())

s.close()