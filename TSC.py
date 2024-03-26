import socket
import time
from enum import Enum

class EP(bytes, Enum):
    Size = 'SIZE 20 mm, 20 mm'.encode()
    Gap = 'GAP 2 mm, 0 mm'.encode()
    Start = 'PRINT 1'.encode()
    Stop = '#!SP'.encode()
    Direction = 'DIRECTION 1'.encode()
    Clear = 'CLS'.encode()
    Type = 'DMATRIX'.encode()
    Code = '100,50,100,100,c126,x6,18,18, "~1241sPn~110sLot~130sQty "'.encode()
    status = '<ESC>!?'.encode()

DM = 'DMATRIX 50,80,100,100,c126,x6,20,20, "~1{datamatrix}"'
template_DM = f"""
        SIZE 20 mm,20 mm
        GAP 3 mm,0
        CLS
        DIRECTION 0
        {DM}
        PRINT 1"""


# template_DM = button()
codes = []
with open('codes.csv', encoding='utf-8') as file:
    for line in file:
        codes.append(line.strip().replace('\x1d', '~d029'))

codes = codes[:5]
print('Open file')
with socket.create_connection(('192.168.251.200', 9100)) as con:
    print('connected')
    try:
        con.send(('\x1B!?'.encode('utf-8')))

    except:

        print('Timed out')
        con.close()
    else:
        response = con.recv(256)
        print("ответ", response)
    sent = 1
    while len(codes):
        sent_cnt = str(sent)
        if sent < 100:
            try:
                code = codes.pop(0)
            except:
                break
            else:

                new_template = template_DM.replace('{datamatrix}', code)
                print(new_template)
                con.send(new_template.encode())
                time.sleep(1)
                #con.send('<ESC>!S'.encode())
                #rcv = con.recv(1024)
                #print(rcv)
                #print(con.recv(255))
                try:
                    con.send(('\x1B!?'.encode('utf-8')))

                except:

                    print('Timed out')
                    con.close()
                else:
                    response = con.recv(256)
                    print("ответ", response)
                sent += 1
                sent_cnt = str(sent)
        else:
            break