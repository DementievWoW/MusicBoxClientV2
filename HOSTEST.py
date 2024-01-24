import socket
from _thread import *


# функция для обработки каждого клиента
def client_thread(con):
    data = con.recv(1024)  # получаем данные от клиента
    message = data.decode()  # преобразуем байты в строку
    print(f"Client sent: {message}")
    message = message[::-1]  # инвертируем строку
    con.send(message.encode())  # отправляем сообщение клиенту
    con.close()  # закрываем подключение


server = socket.socket()  # создаем объект сокета сервера
HOST = (socket.gethostname(), 10001)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # что бы по новой юзать порт
server.bind(HOST)  # привязываем сокет сервера к хосту и порту
server.listen()  # начинаем прослушиваение входящих подключений

print("Server running")
while 1:
    client, _ = server.accept()  # принимаем клиента
    start_new_thread(client_thread, (client,))  # запускаем поток клиента

# HEADER_LENGTH = 10  # длинна сообщения для буфера
# HOST = (socket.gethostname(), 10000)
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.bind(HOST)
# server.listen()
# print('Im listening conn')
# socketList = [server]
# clientDictionary = {}
#
#
# def receiveMsg(client: socket.socket):
#     try:
#         msgHeader = client.recv(HEADER_LENGTH)
#         if not len(msgHeader):
#             return False
#
#         msgLength = int(msgHeader.decode('UTF-8').strip())
#
#         return {
#             'header': msgHeader,
#             'data': client.recv(msgLength).decode('UTF-8')
#         }
#     except:
#         return False
#
#
# while 1:
#     rs, _, xs = select.select(socketList, [], socketList)
#     for _socket in rs:
#         if _socket == server:
#             client, addr = server.accept()
#
#             user = receiveMsg(client)
#             if user is False:
#                 continue
#             socketList.append(client)
#             clientDictionary[client] = user
#             data = user['data']
#             print(f'New connection from {addr} with data {user["data"]}')
#             # print(clientDictionary)
#         else:
#             msg = receiveMsg(client)
#             print(msg)
#             if msg is False:
#                 print(f'Connection from {addr} has been interrupted')
#                 socketList.remove(_socket)
#                 del clientDictionary[_socket]
#                 continue
#             user = clientDictionary(_socket)
#             for client in clientDictionary:
#                 if client is not _socket:
#                     client.send(f'New msg from {user["data"]} is {msg["data"]}')
#     for _socket in xs:
#         socketList.remove(_socket)
#         del clientDictionary[_socket]
#     # print(clientDictionary)
