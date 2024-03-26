import socket
import time
from enum import Enum
from modules import configFile
from PySide6.QtCore import *
import select

class Camera(QObject):
    readcode = Signal(str)
    conSignal = Signal(bool)

    def __init__(self, configCamera):
        super(Camera, self).__init__()
        self.cameraIP = configFile.Config().configParser.get(configCamera, 'IP')
        self.cameraPort = configFile.Config().configParser.get(configCamera, 'Port')

        self._isRuning = True



    def run(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.cameraIP, int(self.cameraPort)))
            #self.sock.settimeout(10)

        except socket.error as err:
            #logging.error(f'Ошибка подключения к серверу {err}')
            print(f'Ошибка подключения к камере: {err}')
            self.conSignal.emit(False)
            #self.disconnect()

        else:
            print("Есть подключение к камере")
            self.conSignal.emit(True)
            print('Запускаем сканирование')
            #self.conSignal.emit(True)
            while self._isRuning:
                ready = select.select([self.sock], [], [], 1.0)
                if ready[0]:
                    res = self.sock.recv(255).decode()
                    self.readcode.emit(res)
                    #print(res)

    def stop(self):
        self._isRuning = False