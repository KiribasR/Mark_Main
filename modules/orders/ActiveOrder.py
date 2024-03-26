from ui_Master import *
import queryDB
import sys
from modules import ui_settings
from modules import ui_functions
from PySide6.QtCore import *


class MainOrders():
    def __init__(self):

        self.ui = Ui_MainWindow()
        self.ui.ordersButton.clicked.connect(self.refreshOrders(self))

    def refreshOrders(self):
        print(queryDB.DatabaseConn('marking_db').querySelectFetchone('select * from serial.mark_codes where batch = 2145'))


