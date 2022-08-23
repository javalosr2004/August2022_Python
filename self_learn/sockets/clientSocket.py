import socket, json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

example_list = ['testlist', 5]

data = json.dumps(example_list)
data = bytes(data, encoding='utf-8')

client.sendall(data)