#from modules.orders import queryDB
import socket


def ping(host, port=1433):
    try:
        socket.setdefaulttimeout(0.2)

        # AF_INET: address family (IPv4)
        # SOCK_STREAM: type for TCP (PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)

        # send connection request to the defined server
        s.connect(server_address)
        #s.close()
    except OSError as error:

        # function returning false after
        # data interruption(no connection)
        print("offline")
        return 'Неактивна'
    else:

        # the connection is closed after
        # machine being connected
        #s.close()
        print("online")
        s.close()
        return 'Активна'

"""def provercaPing(self):
    sock = "192.168.251.200"
    status = os.system("ping -n 1 " + sock)
    #print(status)
    if status == 0:
        print('ok')
    else:
        print("no ok")"""

# ping("192.168.250.101")