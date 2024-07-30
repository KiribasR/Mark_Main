import treepoem
from PySide6.QtCore import *
from modules import configFile

class ImageThread(QObject):
    """def __init__(self, parent = None):
        super(TestThread, self).__init__(parent)"""
    #returnCode = Signal(str)
    imageSignal = Signal(bool)

    def __init__(self, data):
        super(ImageThread, self).__init__()
        self.code = data

    def run(self):
        address = configFile.Config().configParser.get('BASE', "imageAddress")
        try:
            image = treepoem.generate_barcode(
                barcode_type='datamatrix',  # One of the supported codes.
                data=self.code,
                scale=3)
            image.convert('1').save(f'{address}barcode.png')
            self.imageSignal.emit(True)
        except Exception as error:
            print(error)
            self.imageSignal.emit(True)

    def stop(self):
        self._isRunning = False