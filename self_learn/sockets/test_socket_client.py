import socket

'''Client side'''

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 2222))

while True:
    user_message = input('Enter a message: ')
    if user_message == '!q':
        client.close()
        break
    client.send(f'{user_message}'.encode())

    