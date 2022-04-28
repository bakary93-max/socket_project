import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Waiting connexion on {HOST_IP}, port {HOST_PORT}")
connection_socket, client_address = s.accept()
print(f"Connexion established with {client_address}")
while True:
    send_text = input("You: ")
    connection_socket.sendall(send_text.encode())
    received_data = connection_socket.recv(MAX_DATA_SIZE)
    if not received_data:
        break
    print("Message: ", received_data.decode())

s.close()
connection_socket.close()