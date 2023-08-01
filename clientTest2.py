import socket

client = socket.socket()  # создаем сокет клиента
HOST = ("127.0.0.1", 8000)
client.connect(HOST)  # подключаемся к серверу
# message = input("Input a text: ")
message = "sfsffs"
# while 1:
client.send(message.encode())  # отправляем сообщение серверу
data = client.recv(1024)  # получаем данные с сервера
print("Server sent: ", data.decode())
client.close()  # закрываем подключение

