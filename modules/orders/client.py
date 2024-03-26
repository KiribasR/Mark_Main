import socket
import time

from modules import configFile
import logging
import datetime

class Client:
    """Класс для отправки запросов на сервер"""
    serverIP = configFile.Config().configParser.get('SERVER', "ServerSocket")
    logDirect = configFile.Config().configParser.get('LOGS', "logDirect")

    logging.basicConfig(
        filename=logDirect + datetime.date.today().strftime('%d.%m.%Y') + '.log',
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    def __init__(self, server=serverIP, port=5000):
        """Инициализация атрибутов класса"""
        self.server = server  # 'localhost'  # localhost 192.168.250.100
        self.database = port  # 'marking_db'
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((server, 5000))
            self.sock.settimeout(60)
        except socket.error as err:
            logging.error(f'Ошибка подключения к серверу {err}')
            print('Ошибка подключения к серверу')
        else:
            print("Есть подключение к серверу")


    def reciveClient(self, query):
        try:
            #for item in query:
            query = str(query)
            sms = query.encode('utf-8')
            logging.info(f'Сформирован запрос на сервер: {sms}')
            data = 'пока ничего не пришло'
            print(datetime.datetime.now())

            while data != 'oki':
                print(data)
                self.sock.sendall(sms)
                data = self.sock.recv(1024).decode('utf-8')
                #print('Received', repr(data))
            print(datetime.datetime.now())
            print('Закрываем подключение')
            self.sock.close()
            logging.info(f'Отправлен запрос: {repr(sms)}')
            print('Received', repr(sms))
        except Exception as err:
            print(err)
            logging.error(f'Ошибка соединения с сервером: {err}')