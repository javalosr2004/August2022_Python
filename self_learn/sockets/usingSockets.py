from re import S
import socket, json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))

server.listen()

client, addr = server.accept()

while True:
    list = json.loads(client.recv(1024).decode('utf-8'))
    print(f'Type: {type(list)}  | {list}')

