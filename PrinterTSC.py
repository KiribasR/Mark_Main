import socket
import time
from enum import Enum
from modules import configFile
import os
import json

from PySide6.QtCore import *


class EP(bytes, Enum):
    Status = '\x1B!?'.encode('utf-8')
    Start = '#!SR'.encode()
    Stop = '#!SP'.encode()
    Erase = '#!CF'.encode()
    Clear = '#!CA'.encode()


class TSC(QObject):
    """def __init__(self, parent = None):
        super(TestThread, self).__init__(parent)"""
    returnCode = Signal(list)
    stopSignal = Signal(bool)

    text_2_X = 100
    text_2_Y = 7
    text_2_angle = 0
    txt = f'TEXT {text_2_X},{text_2_Y},"3",{text_2_angle},1,1,1,"datamatrix"'
    #txt = f'TEXT "100", "7", "3", "0", "1", "1", "count"'
    DM = 'DMATRIX 50,80,100,100,c126,x6,20,20, "~1{datamatrix}"'
    template_DM_tst = f'''
        SIZE 20 mm,20 mm
        GAP 3 mm,0
        CLS
        DIRECTION 0
        {txt}
        {DM}
        PRINT 1,1
        END'''


    def __init__(self, idTemplate, data, datetime, name, configPrinter):
        super(TSC, self).__init__()
        printerIP = configFile.Config().configParser.get(configPrinter, 'IP')
        printerPort = configFile.Config().configParser.get(configPrinter, 'Port')

        self._isRuning = True
        self.stopPrinting = False

        # self.stopSignal = False

        self.date = datetime
        self.name = name
        self.code = []
        self.id = idTemplate
        updateList = []
        #count = 0
        # Обработка КМ для печати
        for line in data:
            self.code.append(line.strip().replace('\x1d', '~d029').replace('"', '~d34~'))

        print(self.code)
        # Выбор шаблона для работы
        with open(f'{os.path.dirname(os.path.abspath(__file__))}\\template\\TSC\\{self.id}.json', 'r',
                  encoding='utf-8') as file:
            self.content = json.load(file)

        text_content = ''
        self.template = ''

        for key in self.content:
            dataDict = self.content.get(key)
            if key == 'Этикетка':
                for k in dataDict:
                    if k == 'Template':
                        self.template = dataDict.get(k)
                    if k == 'SizeX':
                        self.template = self.template.replace('{SizeX}', dataDict.get(k))
                    if k == 'SizeY':
                        self.template = self.template.replace('{SizeY}', dataDict.get(k))
            if key == 'Проруб':
                for k in dataDict:
                    if k == 'Template':
                        self.template = self.template + '\n' + dataDict.get(k)
                    if k == 'SizeX':
                        self.template = self.template.replace('{SizeX}', dataDict.get(k))
                    if k == 'SizeY':
                        self.template = self.template.replace('{SizeY}', dataDict.get(k))
            if key == 'Направление':
                for k in dataDict:
                    if k == 'Template':
                        self.template = self.template + '\n' + dataDict.get(k)
                    if k == 'SizeX':
                        self.template = self.template.replace('{SizeX}', dataDict.get(k))
            if key == 'Очистка':
                for k in dataDict:
                    self.template = self.template + '\n' + dataDict.get(k)
            if key == 'Счетчик':
                for k in dataDict:
                    if k == 'Template':
                        self.template = self.template + '\n' + (str(dataDict.get(k))).replace('counter', '"counter"')
                    if k == 'PositionX':
                        self.template = self.template.replace('{PositionX}', dataDict.get(k))
                    if k == 'PositionY':
                        self.template = self.template.replace('{PositionY}', dataDict.get(k))
                    if k == 'Font':
                        self.template = self.template.replace('{Font}', '"Font"')
                        self.template = self.template.replace('Font', dataDict.get(k))
                    if k == 'Rotation':
                        self.template = self.template.replace('{Rotation}', dataDict.get(k))
                    if k == 'MulX':
                        self.template = self.template.replace('{MulX}', dataDict.get(k))
                    if k == 'MulY':
                        self.template = self.template.replace('{MulY}', dataDict.get(k))

                '''#text_content = 'Кета'
                #self.text = f'TEXT {int(PositionX)},{int(PositionY)},{int(Font)},{int(Rotation)},1,1,text_content'
                #self.text = f'TEXT 100, 7, "3", 0, 1, 2, "text_content"'
                #self.template = self.template + '\n' + f'{self.text}'
                #print(self.text)
                #self.counter = tuple(str(item) for item in self.text.split(", "))
                #print(self.counter)
                #self.template = self.template + '\n' +  f"{self.counter}"'''
            if key == 'DM':
                for k in dataDict:
                    if k == 'Template':
                        self.template = self.template + '\n' + dataDict.get(k)
                        self.template = self.template.replace('~1{datamatrix}', '"~1{datamatrix}"')
                    if k == 'PositionX':
                        self.template = self.template.replace('{PositionX}', dataDict.get(k))
                    if k == 'PositionY':
                        self.template = self.template.replace('{PositionY}', dataDict.get(k))
                    if k == 'SizeX':
                        self.template = self.template.replace('{SizeX}', dataDict.get(k))
                    if k == 'SizeY':
                        self.template = self.template.replace('{SizeY}', dataDict.get(k))
            if key == 'Дата':
                for k in dataDict:
                    if k == 'Template':
                        self.template = self.template + '\n' + (str(dataDict.get(k))).replace('date', '"date"')
                    if k == 'PositionX':
                        self.template = self.template.replace('{PositionX}', dataDict.get(k))
                    if k == 'PositionY':
                        self.template = self.template.replace('{PositionY}', dataDict.get(k))
                    if k == 'Font':
                        self.template = self.template.replace('{Font}', '"Font"')
                        self.template = self.template.replace('Font', dataDict.get(k))
                    if k == 'Rotation':
                        self.template = self.template.replace('{Rotation}', dataDict.get(k))
                    if k == 'MulX':
                        self.template = self.template.replace('{MulX}', dataDict.get(k))
                    if k == 'MulY':
                        self.template = self.template.replace('{MulY}', dataDict.get(k))
            if key == 'Продукт':
                for k in dataDict:
                    if k == 'Template':
                        self.template = self.template + '\n' + (str(dataDict.get(k))).replace('prod', '"prod"')
                    if k == 'PositionX':
                        self.template = self.template.replace('{PositionX}', dataDict.get(k))
                    if k == 'PositionY':
                        self.template = self.template.replace('{PositionY}', dataDict.get(k))
                    if k == 'Font':
                        self.template = self.template.replace('{Font}', '"Font"')
                        self.template = self.template.replace('Font', dataDict.get(k))
                    if k == 'Rotation':
                        self.template = self.template.replace('{Rotation}', dataDict.get(k))
                    if k == 'MulX':
                        self.template = self.template.replace('{MulX}', dataDict.get(k))
                    if k == 'MulY':
                        self.template = self.template.replace('{MulY}', dataDict.get(k))
            if key == 'Печать':
                for k in dataDict:
                    self.template = self.template + '\n' + dataDict.get(k)
            if key == 'Конец':
                for k in dataDict:
                    self.template = self.template + '\n' + dataDict.get(k)

        print(self.template)

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((printerIP, int(printerPort)))
            self.sock.settimeout(10)
        except socket.error as err:
            # logging.error(f'Ошибка подключения к серверу {err}')
            print('Ошибка подключения к принтеру')
        else:
            print("Есть подключение к принтеру")
            try:

                #self.sock.send(('CODEPAGE 866'.encode('utf-8')))
                self.sock.send(('\x1B!?'.encode('utf-8')))
                response = self.sock.recv(256)
            except:

                print('Timed out')
                self.sock.close()
            else:

                print(response)

    def run(self):
        print('to print')

        count = 0
        #self.sock.send(('CLS'.encode('utf-8')))
        lenghKM = len(self.code)
        inqueue = 0
        while True:
            sent = 0
            sent_cnt = str(sent)

            if sent < 5:
                while sent < 15:
                    try:
                        code = self.code.pop(0)
                        count += 1
                    except:
                        break
                    else:
                        new_template = self.template.replace('{datamatrix}', code).replace('counter', f'{count:05}').replace('date', self.date).replace('prod', self.name)
                        print(new_template)
                        self.sock.send(new_template.encode())
                        sent += 1
                        print(sent)
            print(sent)
            self.sock.send(EP.Status)
            res = self.sock.recv(255)

            if res.decode() == '\x00':
                print('Zakonchil')
                time.sleep(2)
                self.sock.close()
                self.stopSignal.emit(True)
                break

            if res.decode() == '\x20':
                print('Printing')
            time.sleep(2)
            print(f'ответ от принтера: {res.strip()}')


    def stop(self):
        print('Закрываю поток')

    def clear(self):
        print('Очищаю')
        self.sock.send('CLS'.encode('utf-8'))
        #print(self.sock.recv(255))
