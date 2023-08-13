from socket import socket, AF_INET, SOCK_STREAM

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 4444))
server.listen(0)

client, _ = server.accept()
response = client.recv(1024)
print(response)