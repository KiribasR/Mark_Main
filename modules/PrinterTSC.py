import socket
import time
from enum import Enum
from modules import configFile
import main
from modules.orders import queryDB

from PySide6.QtCore import *

class TSC(QObject):
    """def __init__(self, parent = None):
        super(TestThread, self).__init__(parent)"""
    returnCode = Signal(list)
    stopSignal = Signal(bool)

    DM = 'DMATRIX 50,80,100,100,c126,x6,20,20, "~1{datamatrix}"'
    template_DM = f"""
        SIZE 20 mm,20 mm
        GAP 3 mm,0
        CLS
        DIRECTION 0
        {DM}
        PRINT 1,1"""


    def __init__(self, listcod):
        super(TSC, self).__init__()
        self.listCodes = []
        for line in listcod:
            self.listCodes.append(line.strip().replace('\x1d', '~d029'))

        print(self.listCodes)

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('192.168.1.106', 9100))
            self.sock.settimeout(10)

        except socket.error as err:
            # logging.error(f'Ошибка подключения к серверу {err}')
            print('Ошибка подключения к принтеру')
        else:
            print("Есть подключение к принтеру")
            try:
                self.sock.send(('\x1B!?'.encode('utf-8')))
                response = self.sock.recv(256)
            except:

                print('Timed out')
                self.sock.close()
            else:

                print(response)
    def run(self):
        print('to print')
        sent = 0
        self.sock.send(('CLS'.encode('utf-8')))
        lenghKM = len(self.listCodes)
        while lenghKM:
            sent_cnt = str(sent)
            if sent < 20:
                try:

                    code = self.listCodes.pop(0)
                    """else:
                        code = ''"""

                except:
                    break
                else:

                    new_template = self.template_DM.replace('{datamatrix}', code)
                    print(new_template)
                    self.sock.send(new_template.encode())
                    #self.sock.send('PRINT 1'.encode())
                    """try:
                        self.sock.send(('\x1B!?'.encode('utf-8')))
        
                    except:
        
                        print('Timed out')
                        self.sock.close()
                    else:
                        response = self.sock.recv(256)
                        print("ответ", response)"""
                    sent += 1
                    sent_cnt = str(sent)
                    print(sent_cnt)
                    lenghKM -= 1
            else:
                break

    def stop(self):
        print('Закрываю поток')

    def clear(self):
        print('Очищаю')
        self.sock.send('CLS'.encode('utf-8'))
        #print(self.sock.recv(255))