import socket

lang = input('Please enter your language: ')

#creates a client which connects to localhost:5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

#runs client

while True:
    message = input('\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnter message: ')

    if message == '!q':
        break
    else:
        #send the message to the server
        client.send(f'[{lang}]{message}'.encode())
        