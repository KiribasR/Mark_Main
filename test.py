from __future__ import annotations

from PySide6 import QtCore, QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)

        self.dialog = QtWidgets.QFileDialog(self)

        self.dialog.setFileMode(QtWidgets.QFileDialog.open())
        self.dialog.setWindowTitle('Open folder...')

    @QtCore.Slot()
    def on_finished(self) -> None:
        for path in self.dialog.selectedFiles():
            print(path)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MyWindow()
    window.show()

    window.dialog.open(window, QtCore.SLOT('on_finished()'))

    app.exec()
