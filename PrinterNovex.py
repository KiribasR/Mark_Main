import socket
import time
import os
import json
from enum import Enum
from modules import configFile
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules.lines import localLine
#import main

# T4.5#J14.5
# IDM/3R22S22/6/0/1/~1{datamatrix}#G
# T8#J15
# YN100/0B/30///{counter}
stopPrint = False

class EP(bytes, Enum):
    Activate = '#!A1'.encode()
    Status = '#!X0'.encode()
    Start = '#!SR'.encode()
    Stop = '#!SP'.encode()
    Erase = '#!CF'.encode()
    Clear = '#!CA'.encode()
    Jobs = '#!XM1007#G'.encode()
    Errors = '#!XM1010#G'.encode()
    Feed = '#FF'.encode()

class Novex(QObject):
    """def __init__(self, parent = None):
        super(TestThread, self).__init__(parent)"""
    returnCode = Signal(list)
    stopSignal = Signal(bool)


    def __init__(self, idTemplate, data, datetime, name, configPrinter):
        super(Novex, self).__init__()
        printerIP = configFile.Config().configParser.get(configPrinter, 'IP')
        printerPort = configFile.Config().configParser.get(configPrinter, 'Port')

        self._isRuning = True
        self.stopPrinting = False

        #self.stopSignal = False

        self.date = datetime
        self.name = name
        self.code = []
        self.id = idTemplate
        updateList = []
        count = 0
        # Обработка КМ для печати
        for line in data:
            self.code.append(line.strip().replace('\x1d', '~d029'))

        print(self.code)
        # Выбор шаблона для работы
        with open(f'{os.path.dirname(os.path.abspath(__file__))}\\template\\Novex\\{self.id}.json', 'r', encoding='utf-8') as file:
            self.content = json.load(file)

        self.template = ''
        for key in self.content:
            dataDict = self.content.get(key)
            for k in dataDict:
                if k == 'Template':
                    self.template = self.template + dataDict.get(k)
                if k == 'SizeX':
                    self.template = self.template.replace('{SizeX}', dataDict.get(k))
                if k == 'SizeY':
                    self.template = self.template.replace('{SizeY}', dataDict.get(k))
            if key == 'Дата':
               self.template = self.template.replace('{date}', self.date)

            if key == 'Продукт':
               self.template = self.template.replace('{product}', self.name)
        print(self.template)

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((printerIP, int(printerPort)))
            self.sock.settimeout(10)

        except socket.error as err:
            #logging.error(f'Ошибка подключения к серверу {err}')
            print('Ошибка подключения к принтеру')

        else:
            print("Есть подключение к принтеру")

    def run(self):
        print('Запускаем печать')
        self.sock.send(EP.Activate)
        self.sock.send(EP.Stop)
        self.sock.send(EP.Erase)
        self.sock.send(EP.Status)
        res = self.sock.recv(255)
        print(res)
        self.sock.send(EP.Errors)
        res = self.sock.recv(255)
        print(res)
        count = 0
        if res.decode().strip() == '0':
            print('errors')
            exit(2)
        else:
            print('oki')

        while True: #self._isRuning
            #if self._isRuning:
                while len(self.code):
                    if len(self.code) == 0 or self.stopPrinting:
                        #Novex.status(self)
                        break
                    self.sock.send(EP.Jobs)
                    time.sleep(0.5)
                    res = self.sock.recv(255)
                    inqueue_temp = res.decode().strip()

                    inqueue = int(res.decode().strip())
                    # print(inqueue)
                    sent = 0


                    if inqueue < 20:
                        while sent < 20 - inqueue:
                            try:
                                code = self.code.pop(0)
                                count += 1
                                """updateList.append(code)
                                if len(updateList) > 20:
                                    self.returnCode.emit(updateList)
                                    updateList.clear()"""
                            except:
                                break
                            else:
                                # print(count)
                                self.sock.send(self.template.replace('{datamatrix}', code).replace('{counter}',
                                                                                            f'{count:05}').replace('{date}',
                                                                                            f'{self.date}').replace('{prod}',
                                                                                            f'{self.name}').encode())
                                sent += 1
                    self.sock.send(EP.Errors)
                    res = self.sock.recv(255)
                    print(len(self.code))
                    print('ответ от принтера ' + res.decode())
                self.sock.send(EP.Jobs)
                time.sleep(0.5)
                res = self.sock.recv(255)
                if int(res.decode().strip()) == 0:
                    for i in range(2):
                        self.sock.send(EP.Feed)
                        time.sleep(0.5)
                    print('Печать завершена')
                    self.sock.close()
                    self.stopSignal.emit(True)
                    break

    def start(self):
        #self._isRunning = True
        self.sock.send(EP.Start)
        #self.stopPrinting = False

    def stop(self):
        #self._isRunning = False
        self.sock.send(EP.Stop)
        #self.stopPrinting = True

    def clear(self):
        self._isRunning = False
        self.sock.send(EP.Clear)
        self.code.clear()
        #self.sock.send(EP.Erase)

    def status(self):
        self.sock.send(EP.Status)
        res = self.sock.recv(255)
        print('Ответ при остановке ' + res.decode().strip())

    def stopPrint(self):
        self.stopik = True

