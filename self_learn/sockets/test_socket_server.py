import socket, time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2222))

server.listen()

client, addr = server.accept()

while True:
    try:
        message = client.recv(1024).decode()
        print(f'Message recieved: {message}     |     {time.time()}')
    except:
        server.close()
    
