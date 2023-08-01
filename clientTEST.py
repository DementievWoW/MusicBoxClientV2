import socket

client = socket.socket()  # создаем сокет клиента
HOST = ("127.0.0.1", 8000)
client.connect(HOST)  # подключаемся к серверу
# message = input("Input a text: ")
message = "fjkdfdf"
client.send(message.encode())  # отправляем сообщение серверу
data = client.recv(1024)  # получаем данные с сервера
print("Server sent: ", data.decode())
client.close()  # закрываем подключение



# HEADER_LENGTH = 10
# HOST = (socket.gethostname(), 10000)
# username = "werewq".encode('UTF-8')
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(HOST)
# print("Connected to", HOST)
# client.setblocking(False)
# header = f"{len(username):<{HEADER_LENGTH}}".encode('UTF-8') #выравнивание
# client.send(header+username)
# # sent = 0
# # request = b'GET / HTTP/1.1\r\nHost:localhost:10000\r\n\r\n'
# # while sent < len(request):
# #     sent = sent + client.send(request[sent:])
# # print('msg')
