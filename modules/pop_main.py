from ui_Master import *
from ui_Pop_up import *
from modules.orders import queryDB
import sys
import datetime
from modules import ui_settings
from modules import ui_functions
from PySide6.QtCore import *
from PySide6.QtGui import *
from modules.lines import localLine
import main



"""class PopWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.closeSplash.clicked.connect(lambda: self.close())
        self.ui.canselButton.clicked.connect(lambda: self.close())
        self.ui.confirmButton.clicked.connect(lambda: PopWindow.send(self))"""




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = PopWindow()
    sys.exit(app.exec())