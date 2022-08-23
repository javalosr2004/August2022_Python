import socket
from googletrans import Translator

translator = Translator()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
#listen to server
server.listen()

#accept values sent to server
client, addr  = server.accept() #retrieves a new socket which is the client and it's address

while True:
    message = client.recv(1024).decode() #recieves and decodes message sent to server via, client socket address
    
    #gets the lang from the message
    lang = message[1:message.index(']')] #goes from after the first square bracket to the end of the square bracket 
    translation = translator.translate(message[message.index(']') + 1:], src = lang) #gets everything after the end of the square bracket

    print(translation.text)