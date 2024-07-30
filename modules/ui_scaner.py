import time
from modules.orders import queryDB
import sys
import datetime
import logging

from modules import configFile
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import serial

class Scaner(QObject):
    """logDirect = configFile.Config().configParser.get('LOGS', "logDirect")
    logging.basicConfig(
        filename=logDirect + datetime.date.today().strftime('%d.%m.%Y') + '.log',
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)"""

    running = False
    scanCodes = Signal(str)
    infoSignal = Signal(str, object)

    def run(self):
        COM = configFile.Config().configParser.get('BASE', "Scaner")
        try:
            self.ser = serial.Serial(COM, 9600, timeout=0.1)
        except Exception as err:
            print(err)
            print('Ошибка подключения')
            logging.error(f"Ошибка подключения сканера")
            self.infoSignal.emit('Ошибка подключения сканера', "red")
        else:
            print("Сканер подключен")
            logging.info(f"Сканер подключен")
            self.infoSignal.emit('Сканер запущен', "grey")
            global Runt
            while True:
                data = self.ser.readline().decode('utf-8').rstrip()
                if len(data) > 0:
                    print(data)
                    self.scanCodes.emit(data)
                    QThread.msleep(100)
                    self.ser.close()
                    break
                """if Runt:
                    self.ser.close()
                    break"""

    def stop(self):
        self._isRunning = False


class SearchScaner(QObject):
    logDirect = configFile.Config().configParser.get('LOGS', "logDirect")
    logging.basicConfig(
        filename=logDirect + datetime.date.today().strftime('%d.%m.%Y') + '.log',
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)


    searchCodes = Signal(str)
    infoSearchSignal = Signal(str, object)

    def __init__(self):
        super(SearchScaner, self).__init__()


        self._isRunning = True

    def run(self):
        COM = configFile.Config().configParser.get('BASE', "Scaner")
        try:
            self.serial = serial.Serial(COM, 9600, timeout=0.1)
        except Exception as err:
            print(err)
            print('Ошибка подключения')
            logging.error(f"Ошибка подключения сканера")
            #self.infoSignal.emit('Ошибка подключения сканера', "red")
        else:
            print("Сканер подключен")
            logging.info(f"Сканер подключен")
            #self.infoSignal.emit('Сканер запущен', "grey")

            while self._isRunning:
                if not self._isRunning:
                    self.serial.close()
                    break
                else:
                    QThread.msleep(100)
                    data = self.serial.readline().decode('utf-8').rstrip()
                    if len(data) > 0:
                        print(data)
                        self.searchCodes.emit(data)


    def stop(self):
        self._isRunning = False
