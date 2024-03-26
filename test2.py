import socket
from enum import Enum


class EP(bytes, Enum):
    Activate = '#!A1'.encode()
    Status = '#!X0'.encode()
    Start = '#!SR'.encode()
    Stop = '#!SP'.encode()
    Erase = '#!CF'.encode()
    Jobs = '#!XM1007#G'.encode()
    Errors = '#!XM1010#G'.encode()


template_DM = f"""
                SIZE 20 mm,20 mm
                GAP 3 mm,0
                CLS
                DIRECTION 1
                {DM_template}
                {text_1_template}
                {text_2_template}
                PRINT 1
                """

codes = []
with open('sample.txt', encoding='utf-8') as file:
    for line in file:
        codes.append(line.strip().replace('\x1d', '~d029'))

codes = codes[:10]

with socket.create_connection(('192.168.1.97', 9100)) as con:
    con.send(EP.Activate)
    con.send(EP.Stop)
    con.send(EP.Erase)
    con.send(EP.Status)
    res = con.recv(255)
    print(res)
    con.send(EP.Errors)
    res = con.recv(255)
    print(res)
    if res.decode().strip() == '0':
        print('errors')
        exit(2)
    while len(codes):
        con.send(EP.Jobs)
        res = con.recv(255)
        print(f'какая-то хрень {res}')
        inqueue = int(res.decode().strip())
        print(inqueue)
        sent = 0
        if inqueue < 50:
            while sent < 50 - inqueue:
                try:
                    code = codes.pop(0)
                except:
                    break
                else:
                    con.send(template.replace('{datamatrix}', code).encode())
                    sent += 1
        con.send(EP.Errors)
        res = con.recv(255)
        if res.decode().strip() != '1':
            print('errors')
            break
