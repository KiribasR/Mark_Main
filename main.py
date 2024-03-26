import time
from ui_Master import *
from modules.orders import queryDB
from modules.orders import client
import sys
import datetime
import logging
from modules import ui_scaner
from modules import configFile
from modules import ui_functions
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules.lines import localLine
import PrinterNovex
from  modules import PrinterTSC
import imageSave
import socketCamera
import threading
from queue import Empty, Queue

stopPrint = False
pauseNovex64 = False
pauseNovex504 = False

# import resources_rc
class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class MainWindow(QMainWindow):
    logDirect = configFile.Config().configParser.get('LOGS', "logDirect")
    logging.basicConfig(
        filename=logDirect + datetime.date.today().strftime('%d.%m.%Y') + '.log',
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        ui_functions.UIFunctions.uiDefinitions(self)

        self.printScanList = []
        ############################################# АНИМАЦИИ #########################################################
        # Смена размера колонок таблицы выбранного заказа
        horizontalHeaderCurrentOrderTab = self.ui.batchData_Tab.horizontalHeader()
        horizontalHeaderCurrentOrderTab.resizeSection(1, 95)
        horizontalHeaderCurrentOrderTab.resizeSection(2, 95)
        horizontalHeaderCurrentOrderTab.resizeSection(3, 95)
        horizontalHeaderCurrentOrderTab.resizeSection(4, 95)
        horizontalHeaderCurrentOrderTab.resizeSection(5, 95)
        horizontalHeaderCurrentOrderTab.resizeSection(6, 95)
        horizontalHeaderCurrentOrderTab.resizeSection(7, 95)

        # Смена размера колонок таблицы поискового заказа
        horizontalHeaderSearchOrderTab = self.ui.batchData_Tab_2.horizontalHeader()
        horizontalHeaderSearchOrderTab.resizeSection(1, 95)
        horizontalHeaderSearchOrderTab.resizeSection(2, 95)
        horizontalHeaderSearchOrderTab.resizeSection(3, 95)
        horizontalHeaderSearchOrderTab.resizeSection(4, 95)
        horizontalHeaderSearchOrderTab.resizeSection(5, 95)
        horizontalHeaderSearchOrderTab.resizeSection(6, 95)
        horizontalHeaderSearchOrderTab.resizeSection(7, 95)

        # Смена размера колонок таблицы Активных заказов
        horizontalHeaderActivOrderTab = self.ui.activOrder_Tab.horizontalHeader()
        horizontalHeaderActivOrderTab.resizeSection(0, 60)
        horizontalHeaderActivOrderTab.resizeSection(1, 80)
        horizontalHeaderActivOrderTab.resizeSection(2, 270)
        horizontalHeaderActivOrderTab.resizeSection(3, 100)

        # Смена размера колонок таблицы КМ выбранного заказа
        horizontalHeaderKMorder = self.ui.orderKM_tab.horizontalHeader()
        horizontalHeaderKMorder.resizeSection(0, 75)
        horizontalHeaderKMorder.resizeSection(3, 270)
        horizontalHeaderKMorder.resizeSection(4, 100)

        # Смена размера колонок таблицы линий для отправки задания
        horizontalHeaderSendLine = self.ui.sendLine_tab.horizontalHeader()
        horizontalHeaderSendLine.resizeSection(0, 60)
        horizontalHeaderSendLine.resizeSection(1, 400)
        horizontalHeaderSendLine.resizeSection(2, 100)

        # Смена размера колонок таблицы КИГУ
        horizontalHeaderKITU = self.ui.orderKITU_tab.horizontalHeader()
        horizontalHeaderKITU.resizeSection(0, 60)
        horizontalHeaderKITU.resizeSection(1, 300)
        horizontalHeaderKITU.resizeSection(2, 150)
        # horizontalHeaderKITU.resizeSection(3, 200)

        # Смена размера колонок таблицы КМ в КИГУ
        horizontalHeaderFromKITU = self.ui.ki_from_KITU_tab.horizontalHeader()
        horizontalHeaderFromKITU.resizeSection(0, 60)
        horizontalHeaderFromKITU.resizeSection(1, 300)
        horizontalHeaderFromKITU.resizeSection(2, 150)

        # Смена размера колонок таблицы создания продукта
        horizontalHeaderNewProduct = self.ui.currentProd_Tab.horizontalHeader()
        horizontalHeaderNewProduct.resizeSection(0, 60)
        horizontalHeaderNewProduct.resizeSection(1, 400)
        horizontalHeaderNewProduct.resizeSection(2, 150)
        horizontalHeaderNewProduct.resizeSection(3, 150)

        # Смена размера колонок таблицы создания продукта
        horizontalHeaderNewLine = self.ui.currentLine_Tab.horizontalHeader()
        horizontalHeaderNewLine.resizeSection(0, 60)
        horizontalHeaderNewLine.resizeSection(1, 300)
        horizontalHeaderNewLine.resizeSection(2, 250)

        # Смена размера колонок таблицы кодов рулона
        horizontalHeaderRollTable = self.ui.rollTable.horizontalHeader()
        horizontalHeaderRollTable.resizeSection(0, 60)
        horizontalHeaderRollTable.resizeSection(1, 350)
        horizontalHeaderRollTable.resizeSection(2, 150)
        horizontalHeaderRollTable.resizeSection(3, 250)

        # Смена размера колонок таблицы выбора принтера
        horizontalPrintTable = self.ui.listPrinter_tab.horizontalHeader()
        horizontalPrintTable.resizeSection(0, 60)
        horizontalPrintTable.resizeSection(1, 250)
        horizontalPrintTable.resizeSection(2, 150)

        # Смена размера колонок таблицы кодов для печати
        horizontalKMPrintedTable = self.ui.kmPrint_tab.horizontalHeader()
        horizontalKMPrintedTable.resizeSection(0, 60)
        horizontalKMPrintedTable.resizeSection(1, 300)
        horizontalKMPrintedTable.resizeSection(2, 150)

        # Кастомный заголов
        # ui_settings.Settings.ENABLE_CUSTOM_TITLE_BAR = True
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.ui.closeButton.clicked.connect(lambda: self.close())
        self.ui.restoreButton.clicked.connect(lambda: ui_functions.UIFunctions.resize_window(self))

        # Вызов функции расширения левого меню
        widgets.toggleButton.clicked.connect(lambda: ui_functions.UIFunctions.toggleMenu(self))

        # Вызов функции отображения меню авторизации
        widgets.advancedSearchBtn.clicked.connect(lambda: ui_functions.UIFunctions.advancedSearchMenu(self))

        ##################################ВКЛАДКА ПОИСК######################################
        # Вызов функции отображения расширенного поиска
        widgets.userButton.clicked.connect(lambda: ui_functions.UIFunctions.userMenu(self))

        ##################################ВКЛАДКА ЛИНИИ######################################
        # Вызов функции отображения меню всех КМ выбранного заказа
        widgets.showKM_btn.clicked.connect(lambda: ui_functions.UIFunctions.dmWindow(self))

        # Вызов функции отображения меню КИТУ выбранного заказа
        widgets.showKITU.clicked.connect(lambda: ui_functions.UIFunctions.kituWindow(self))

        # Вызов функции отображения меню доступных линий
        widgets.sendBatchOnLine_btn.clicked.connect(lambda: ui_functions.UIFunctions.sendLineWindow(self))
        widgets.canselOrder_btn.clicked.connect(lambda: ui_functions.UIFunctions.sendLineWindow(self))
        # widgets.sendOrder_btn.clicked.connect(lambda: ui_functions.UIFunctions.sendLineWindow(self))
        widgets.sendOrder_btn.clicked.connect(lambda: ui_functions.UIFunctions.clickedBatch(self))



        ################################## ВКЛАДКА НАСТРОЙКИ ######################################
        # Вызов функции отображения меню добавления продуктов (настройки)
        widgets.addProductBtn.clicked.connect(lambda: ui_functions.UIFunctions.addProductWindow(self))
        widgets.addProductCanselBtn.clicked.connect(lambda: ui_functions.UIFunctions.addProductWindow(self))

        # Вызов функции отображения меню редактирования продуктов (настройки)
        widgets.editProductBtn.clicked.connect(lambda: ui_functions.UIFunctions.editProductWindow(self))
        widgets.updateProductCanselBtn.clicked.connect(lambda: ui_functions.UIFunctions.editProductWindow(self))

        # Вызов функции отображения меню добавления линии (настройки)
        widgets.addLineBtn.clicked.connect(lambda: ui_functions.UIFunctions.addLineWindow(self))
        widgets.addLineCanselBtn.clicked.connect(lambda: ui_functions.UIFunctions.addLineWindow(self))

        # Вызов функции отображения меню редактирования продуктов (настройки)
        widgets.editLineBtn.clicked.connect(lambda: ui_functions.UIFunctions.editLineWindow(self))
        widgets.editLineCanselBtn.clicked.connect(lambda: ui_functions.UIFunctions.editLineWindow(self))

        # Вызов функции смены цвета строки ввода данных о продукте (настройки)
        self.ui.productNameEdit.textChanged.connect(lambda: MainWindow.clearcolor(self, self.ui.productNameEdit))
        self.ui.productGTINedit.textChanged.connect(lambda: MainWindow.clearcolor(self, self.ui.productGTINedit))
        self.ui.productCountEdit.textChanged.connect(lambda: MainWindow.clearcolor(self, self.ui.productCountEdit))

        # Вызов функции смены цвета строки ввода данных о линии (настройки)
        self.ui.lineIPEdit.textChanged.connect(lambda: MainWindow.clearcolor(self, self.ui.lineIPEdit))
        self.ui.lineNameEdit.textChanged.connect(lambda: MainWindow.clearcolor(self, self.ui.lineNameEdit))

        # Вызов функции скрывания кнопок добавления продуктов (настройки)
        #widgets.addProductBtn.clicked.connect(lambda: ui_functions.UIFunctions.hideProductButton(self))

        # Смена основного окна
        widgets.lineButton.clicked.connect(self.buttonClick)
        widgets.startLineButton.clicked.connect(self.buttonClick)
        widgets.ordersButton.clicked.connect(self.buttonClick)
        widgets.startOrdersButton.clicked.connect(self.buttonClick)
        widgets.settingsButton.clicked.connect(self.buttonClick)
        widgets.startSettingsButton.clicked.connect(self.buttonClick)
        widgets.searchButton.clicked.connect(self.buttonClick)
        widgets.startSearchButton.clicked.connect(self.buttonClick)
        widgets.printFrameButton.clicked.connect(self.buttonClick)
        widgets.rollFrameButton.clicked.connect(self.buttonClick)
        self.show()

        ######################################### ОСНОВНЫЕ ФУНКЦИИ #####################################################
        ##########################Окно линий########################
        # Вызов функции печати
        self.ui.startPrint_btn.clicked.connect(lambda: MainWindow.startPrint(self))

        # Вызов функции обновления линий
        self.ui.lineButton.clicked.connect(lambda: MainWindow.loadLine(self))
        self.ui.startLineButton.clicked.connect(lambda: MainWindow.loadLine(self))
        self.ui.refreshLineButton.clicked.connect(lambda: MainWindow.loadLine(self))

        self.ui.lineButton.clicked.connect(lambda: MainWindow.lineFrame_ini(self))
        self.ui.refreshLineButton.clicked.connect(lambda: MainWindow.lineFrame_ini(self))


        # Получение данных с выбранной линии в таблице доступных линий
        self.ui.lineData_Tab.itemClicked.connect(self.clickLineInTab)

        # Вызов функции обновления доступных заказов
        self.ui.ordersButton.clicked.connect(lambda: MainWindow.loadBatch(self))
        self.ui.startOrdersButton.clicked.connect(lambda: MainWindow.loadBatch(self))
        self.ui.refreshBatch_button.clicked.connect(lambda: MainWindow.loadBatch(self))

        # Заполнение таблицы информацией по выбранному заказу
        self.ui.activOrder_Tab.itemClicked.connect(self.clickedBatch)

        # Отображение всех КМ по заказу
        self.ui.showKM_btn.clicked.connect(lambda: MainWindow.showListKM(self))

        # Получение данных о заказе при выборе в таблице доступных заказов на линии
        self.ui.batchOnLine_Tab.itemClicked.connect(self.clickBatchInTab)

        # Закрытие выбранного заказа
        self.ui.closeOrderButton.clicked.connect(lambda: MainWindow.closeOrderOnLine(self))

        # Удаление выбранного заказа
        self.ui.deleteOrderButton.clicked.connect(lambda: MainWindow.deleteOrderOnLine(self))

        # Экспорт выбранного заказа
        self.ui.exportBatch_btn.clicked.connect(lambda: MainWindow.exportOrder_function(self))

        # Вызов функции добавление линий в таблицу для отправки заказа
        self.ui.sendBatchOnLine_btn.clicked.connect(lambda: MainWindow.loadLine_in_lin_box(self))

        # Вызов функции отоборажения КИТУ для заказа
        self.ui.showKITU.clicked.connect(lambda: MainWindow.loadKITU_in_tab(self))

        # Отображение КМ при выборе нажатие на КИТУ в таблице
        self.ui.orderKITU_tab.itemClicked.connect(self.showKI_in_KITU)

        # Вызов функции закрытия заказа в Базе данных
        self.ui.closeBatch_btn.clicked.connect(lambda: MainWindow.closeOrderInBD(self))

        # Вызов функции удаления заказа в Базе данных
        self.ui.deleteBatch_btn.clicked.connect(lambda: MainWindow.deleteOrderInDB(self))

        # Вызов функции сохранения км в файл для печати
        self.ui.saveCodeInFile_btn.clicked.connect(lambda: MainWindow.saveCodeToPrintFile(self))
        self.ui.printButton.clicked.connect(lambda: MainWindow.transitionToPrinting(self))

        # Выбор линии для отправки заказа
        self.ui.sendLine_tab.itemClicked.connect(self.selectLine_in_send_tab)

        # Вызов окна подверждения отправки на линию
        self.ui.sendOrder_btn.clicked.connect(lambda: MainWindow.sendBatchToLocalStation(self))

        # Выбор кода рулона
        self.ui.rollButton.clicked.connect(lambda: MainWindow.rollNumberSelect(self))

        ##########################Окно настроек########################
        # Выозв функции для добавления продукта в таблицу
        self.ui.addProductConfirmBtn.clicked.connect(lambda: MainWindow.addNewProduct(self))

        # Вызов функции обновления таблицы с продуктами и линиями
        self.ui.settingsButton.clicked.connect(lambda: MainWindow.loadExistentProduct(self))
        self.ui.startSettingsButton.clicked.connect(lambda: MainWindow.loadExistentProduct(self))
        self.ui.settingsButton.clicked.connect(lambda: MainWindow.loadExistentLines(self))

        # Получение данных о продукте в таблице доступных продуктов
        self.ui.currentProd_Tab.itemClicked.connect(self.sendRowProductSettingTable)

        # Вызов функции удаления выбранного продуктами
        self.ui.deleteProductBtn.clicked.connect(lambda: MainWindow.deleteProductInSettings(self))

        # Вызов функции редактирования выбранного продукта
        self.ui.updateProductConfirmBtn.clicked.connect(lambda: MainWindow.updateProductInSetting(self))

        # Выозв функции для добавления линии в таблицу
        self.ui.addLineConfirmBtn.clicked.connect(lambda: MainWindow.addNewLines(self))

        # Получение данных о линии в таблице доступных линий
        self.ui.currentLine_Tab.itemClicked.connect(self.sendRowLineSettingTable)

        # Вызов функции удаления выбранноq линии
        self.ui.deleteLineBtn.clicked.connect(lambda: MainWindow.deleteLineInSettings(self))

        # Вызов функции редактирования выбранной линии
        self.ui.editLineConfirmBtn.clicked.connect(lambda: MainWindow.updateLineInSetting(self))

        ########################## Печать #######################
        self.ui.listPrinter_tab.itemClicked.connect(self.callInfoPrinter)

        ########################## Поиск ########################
        # Вызов функции редактирования выбранной линии
        self.ui.startSearchBtn.clicked.connect(lambda: MainWindow.searchFunction(self))
        self.ui.serchLineEdit.textChanged.connect(self.search)

        # Выбор режима
        self.ui.buttonGroup.buttonClicked.connect(self.loadToFile)

        # Выбор шаблона для печати
        # self.ui.buttonGroup_2.buttonClicked.connect(self.loadModePrint)


        ################################## Управление принтерами ###################################
        # Novex 64-04
        self.ui.pausePrint_btn_1.clicked.connect(lambda: MainWindow.pause_resume_Novex64(self))     # Пуск/пауза
        self.ui.endPrint_btn_1.clicked.connect(lambda: MainWindow.clearPrintNovex64(self))  # Принудительный останов печати

        # Novex 504
        self.ui.pausePrint_btn_2.clicked.connect(lambda: MainWindow.pause_resume_Novex504(self))  # Пуск/пауза
        self.ui.endPrint_btn_2.clicked.connect(lambda: MainWindow.clearPrintNovex504(self))  # Принудительный останов печати

        #self.ui.pushButton_4.clicked.connect(lambda: MainWindow.loadPrint(self)) # Подклюение

        #self.ui.pushButton_2.clicked.connect(lambda: MainWindow.stopPrinting2(self))  # Стоп печати
        #self.ui.pushButton_3.clicked.connect(lambda: MainWindow.clearPrint(self))  # Стоп печати
        #self.ui.pausePrint_btn_1.clicked.connect(lambda: MainWindow.stop_threadPrinter(self))
        #self.ui.pushButton.clicked.connect(lambda: MainWindow.printer_1(self))  # Запуск потока принтера
        #self.ui.pushButton_4.clicked.connect(lambda: MainWindow.sendListToPrint(self))

        ##################################testprint_2###################################


        #self.ui.pushButton_5.clicked.connect(lambda: MainWindow.startPrint(self))  # Запуск потока принтера
        #self.ui.pushButton_8.clicked.connect(lambda: MainWindow.startPrintNovex64(self))

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

########################################################################################################################
################################################### СКАНЕР/РУЛОН #######################################################
    def listInRoll(self, rollNumber):
        """Выгрузка км по введенному коду рулона
            Заполнение таблицы кодами с кодом рулона"""
        listCodeInRoll = queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'Select code, status from serial.mark_codes where group_number = ' + rollNumber)

        index = 0

        while self.ui.rollTable.rowCount() > 0:
            self.ui.rollTable.removeRow(0)

        for data in listCodeInRoll:
            rowcount = self.ui.rollTable.rowCount()
            self.ui.rollTable.insertRow(rowcount)

        for item in listCodeInRoll:
            codeInList = item[0]
            if item[1] == 0:
                statusCode = 'Полный'
            elif item[1] == 2:
                statusCode = 'Брак'
            elif item[1] == 3:
                statusCode = 'Печать'
            elif item[1] == 4:
                statusCode = 'Новый'
            elif item[1] == 5:
                statusCode = 'Напечатан'
            elif item[1] == 6:
                statusCode = 'Экспорт'

            self.ui.rollTable.setItem(index, 0, QTableWidgetItem(str(index+1)))
            self.ui.rollTable.setItem(index, 1, QTableWidgetItem(codeInList))
            self.ui.rollTable.setItem(index, 2, QTableWidgetItem(statusCode))
            self.ui.rollTable.setItem(index, 3, QTableWidgetItem(rollNumber))

            index += 1

    def rollNumberSelect(self):
        """Выбор кода рулона
        Если рулон не задан, то вызываем предупреждение
        Если рулон указан, делаем его поиск по базе"""

        self.curRollCode = self.ui.rollCode_edit.text()
        if self.curRollCode == '':
            print('Код рулона не введен')
            MainWindow.fillingPlainText(self, 'Код рулона не указан', 'red')
        else:
            print('Код рулона: ', self.curRollCode)
            record = f'Код рулона {self.curRollCode}'
            MainWindow.fillingPlainText(self, record, 'grey')
            self.ui.rollCode_edit.clear()
            checkRollNumber = queryDB.DatabaseConn('marking_db').querySelectFetchone(
                'Select code from serial.mark_codes where group_number = ?', self.curRollCode)
            if len(checkRollNumber) > 0:
                MainWindow.listInRoll(self, self.curRollCode)
                self.ui.rollCode_edit.setPlaceholderText('Отсканируйте последний код в рулоне')
                MainWindow.threadScaner(self)
            else:
                MainWindow.fillingPlainText(self, 'Код рулона не найден', 'red')
                self.ui.rollCode_edit.setPlaceholderText('Код рулона')

    @Slot(str)
    def scanCodeInRoll(self, string):
        """Метод отбраковки оставшегося рулона"""
        print(f"Получен код {string}")
        logging.info(f"Отсканирован код с рулона: {string}")
        self.ui.rollCode_edit.setText(string)
        sql = 'select code from serial.mark_codes where updated <= (select updated from serial.mark_codes where code = ?) and group_number = ?'
        listForUpdate = queryDB.DatabaseConn('marking_db').querySelectFetchone(sql, (string, self.curRollCode))
        #print(listForUpdate)
        #print(len(listForUpdate))

        listForSend = []
        kortej = ()

        for codeItem in listForUpdate:
            codeStatus = 2
            kortej = kortej + (codeItem, codeStatus, self.curRollCode)
            listForSend.append(kortej)
            kortej = ()

        value = listForSend
        queryDB.DatabaseConn('marking_db').queryInsertMany('insert into serial.code_scaned (mark_code, status, group_code) values (?,?,?)', value)
        MainWindow.stop_threadScaner(self)
        self.ui.rollCode_edit.clear()
        self.ui.rollCode_edit.setPlaceholderText('Код рулона')

        MainWindow.fillingPlainText(self, string, "green")
        string = f'Отбракован код рулона: {self.curRollCode}'
        MainWindow.fillingPlainText(self, string, "green")

    @Slot(str, object)
    def fillingPlainText(self, record, color):
        """Метод заполняет лог сканирования
            В зависимости от события выбирается цвет текста"""
        color_format = self.ui.listAction.currentCharFormat()
        if color == "grey":
            color = QColor(66, 66, 66)
            color_format.setForeground(color)
            self.ui.listAction.setCurrentCharFormat(color_format)
        elif color == "red":
            color = QColor(255, 75, 75)
            color_format.setForeground(color)
            self.ui.listAction.setCurrentCharFormat(color_format)
            self.ui.rollCode_edit.setPlaceholderText('Код рулона')
            MainWindow.stop_threadScaner(self)
        elif color == "green":
            color = QColor(0, 160, 20)
            color_format.setForeground(color)
            self.ui.listAction.setCurrentCharFormat(color_format)
        self.ui.listAction.appendPlainText(f"{(time.strftime('%H:%M:%S'))} - {record}")

    def threadScaner(self):
        """Создаем поток сканера"""
        self.thread = QThread()
        self.scaner = ui_scaner.Scaner()
        self.scaner.moveToThread(self.thread)
        self.scaner.scanCodes.connect(self.scanCodeInRoll)
        self.scaner.infoSignal.connect(self.fillingPlainText)
        self.thread.started.connect(self.scaner.run)
        self.thread.start()

    def stop_threadScaner(self):
        self.scaner.stop()
        self.thread.quit()
        self.thread.wait()

########################################################################################################################
###################################################### ПЕЧАТЬ ##########################################################
    def saveCodeToPrintFile(self):
        """Метод сохранения КМ в файл"""
        listCode = MainWindow.loadKM_forPrint(self)

        name = (f'{batchItem}.txt')
        save = QFileDialog.getSaveFileName(self, "Save File", name, "Text file (*.txt)")

        if save:
            with open(save[0], "w") as f:
                for code in listCode:
                    value = code.strip('\n\t')
                    f.write(f'{value}\n')
            """queryDB.DatabaseConn('marking_db').queryUpdate(
                '''UPDATE serial.mark_codes SET status = 3 WHERE batch = ''' + batchItem)"""

            logging.info(f'Выгружено на печать {len(listCode)} по заказу {batchItem}')
            MainWindow.loadStatusKM_function(self, self.ui.batchData_Tab, batchItem)

    def loadKM_forPrint(self):
        """Выгрузка КМ в статусе Полный и Печать для отправки на печать"""
        logging.info(f'Выгружаем коды для печати по заказу {batchItem}')
        listCode = queryDB.DatabaseConn('marking_db').querySelectFetchone(
            'Select code from serial.mark_codes where (status = 4 or status = 3) and batch = ?', int(batchItem))
        return listCode

    def transitionToPrinting(self):
        """Функция печати или сохранение кодов в файл"""
        # Заполнение таблицы доступными для работы принтерами
        printerName_1 = configFile.Config().configParser.get('PRINTER1', "Name")
        printerIP_1 = configFile.Config().configParser.get('PRINTER1', "IP")
        printerPort_1 = configFile.Config().configParser.get('PRINTER1', "Port")

        self.ui.listPrinter_tab.setItem(0, 0, QTableWidgetItem(str(1)))
        self.ui.listPrinter_tab.setItem(0, 1, QTableWidgetItem(printerName_1))
        self.ui.listPrinter_tab.setItem(0, 2, QTableWidgetItem(localLine.ping(printerIP_1, int(printerPort_1))))

        printerName_2 = configFile.Config().configParser.get('PRINTER2', "Name")
        printerIP_2 = configFile.Config().configParser.get('PRINTER2', "IP")
        printerPort_2 = configFile.Config().configParser.get('PRINTER2', "Port")

        self.ui.listPrinter_tab.setItem(1, 0, QTableWidgetItem(str(2)))
        self.ui.listPrinter_tab.setItem(1, 1, QTableWidgetItem(printerName_2))
        self.ui.listPrinter_tab.setItem(1, 2, QTableWidgetItem(localLine.ping(printerIP_2, int(printerPort_2))))

        printerName_3 = configFile.Config().configParser.get('PRINTER3', "Name")
        printerIP_3 = configFile.Config().configParser.get('PRINTER3', "IP")
        printerPort_3 = configFile.Config().configParser.get('PRINTER3', "Port")

        self.ui.listPrinter_tab.setItem(2, 0, QTableWidgetItem(str(3)))
        self.ui.listPrinter_tab.setItem(2, 1, QTableWidgetItem(printerName_3))
        self.ui.listPrinter_tab.setItem(2, 2, QTableWidgetItem(localLine.ping(printerIP_3, int(printerPort_3))))

        # Переход на страницу печати
        widgets.stackedWidget.setCurrentWidget(widgets.printPage)
        self.ui.dateEdit_1.setDate(datetime.date.today())

        # Заполнение названия
        printItem = self.ui.activOrder_Tab.selectedItems()
        self.ui.selectedBatchForPrint_label.setText(printItem[1].text())
        self.ui.SelectedNameForPrint_label.setText(printItem[2].text())

        # Очистка таблицы
        while self.ui.kmPrint_tab.rowCount() > 0:
            self.ui.kmPrint_tab.removeRow(0)

        # Заполнение таблицы кодами, предназначеными для печати
        listCodes = MainWindow.loadKM_forPrint(self)
        MainWindow.threadImage(self, listCodes[0])

        # Добавление строк по количеству КМ для печати
        for item in listCodes:
            rowcount = self.ui.kmPrint_tab.rowCount()
            self.ui.kmPrint_tab.insertRow(rowcount)

        # Заполнение таблицы кодами
        index = 0
        for code in listCodes:
            number = QTableWidgetItem(str(index + 1))
            # number.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.kmPrint_tab.setItem(index, 0, QTableWidgetItem(number))
            self.ui.kmPrint_tab.setItem(index, 1, QTableWidgetItem(code))
            index = index + 1

        # Блокировка кнопки окна печати
        # Определение функции печати (принтер или сохранение в файл)
        settingPrint = configFile.Config().configParser.get('BASE', "Mode")
        if settingPrint == 'Printer':
            self.idRadioButton = 0
            self.ui.allPrint_rbtn.setChecked(True)
            #self.ui.withoutDate_btn_1.setChecked(True)
            self.idTemplate = 0
            self.dateForPrint = ''

            self.ui.startPrint_btn.setEnabled(True)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}"
                                                 "QPushButton: hover{background - color: rgb(66, 66, 66);")
            self.ui.saveCodeInFile_btn.setEnabled(False)
            self.ui.saveCodeInFile_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")

        else:
            self.ui.save_rbtn.setChecked(True)
            self.ui.startPrint_btn.setEnabled(False)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            self.ui.saveCodeInFile_btn.setEnabled(True)
            self.ui.saveCodeInFile_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)};"
                                                     "QPushButton: hover{background - color: rgb(66, 66, 66);")

        self.ui.allCountLabel.setText(f'Доступно для печати этикеток: {len(listCodes)}')

        # Проверка доступности принтера
        MainWindow.detectionPage_printer(self)

    def detectionPage_printer(self):
        """Функция определения текущей вкладки принтера
            блокирует кнопки печати если принтер отключен"""
        currentRowPrintTable = self.ui.listPrinter_tab.currentIndex().row()
        if currentRowPrintTable == -1:
            currentRowPrintTable = 0

        item = self.ui.listPrinter_tab.item(currentRowPrintTable, 2).text()

        if item != 'Активна':
            self.ui.startPrint_btn.setEnabled(False)
            self.ui.startPrint_btn.setStyleSheet(("QPushButton {background-color : rgb(119, 119, 119)}"))
        else:
            self.ui.startPrint_btn.setEnabled(True)
            self.ui.startPrint_btn.setStyleSheet(("QPushButton {background-color : rgb(36, 149, 255)}"))

        return item
        #MainWindow.definitionPrintMode(self)

    def callInfoPrinter(self):
        item = self.ui.listPrinter_tab.selectedItems()
        positionPrint = item[0].text()
        print(positionPrint)
        if positionPrint == '1':
            self.ui.toolBox_2.setCurrentWidget(widgets.page_3)
            MainWindow.definitionPrintMode(self)
        elif positionPrint == '2':
            self.ui.toolBox_2.setCurrentWidget(widgets.page_4)
            MainWindow.definitionPrintMode(self)
        elif positionPrint == '3':
            self.ui.toolBox_2.setCurrentWidget(widgets.page)

    def selectedPagePrinter(self):
        """Определение индекса принтера для отправки на печать"""
        currentPrinter = self.ui.toolBox_2.currentIndex()
        return currentPrinter

    def definitionPrintMode(self):
        """Определение режима печати
            - печать + верефикация
            - только печать
            - только верефикация"""
        currentPrinter = MainWindow.selectedPagePrinter(self)
        if currentPrinter == 0:
            selectedPrinter = 'PRINTER1'
            printMode = configFile.Config().configParser.get(selectedPrinter, "PrinteMode")
            state_printer = MainWindow.detectionPage_printer(self)
            if printMode == 'All':
                self.ui.cameraTextEdit_1.clear()
                self.ui.cameraTextEdit_1.appendPlainText('Печать с верификацией')


                if state_printer != 'Активна':
                    self.ui.startPrint_btn.setEnabled(False)
                    self.ui.startPrint_btn.setStyleSheet(("QPushButton {background-color : rgb(119, 119, 119)}"))
                else:
                    self.ui.startPrint_btn.setEnabled(True)
                    self.ui.startPrint_btn.setStyleSheet(("QPushButton {background-color : rgb(36, 149, 255)}"))

            elif printMode == 'Scan':
                self.ui.cameraTextEdit_1.clear()
                self.ui.cameraTextEdit_1.appendPlainText('Режим считывания')

                self.ui.startPrint_btn.setEnabled(True)
                self.ui.startPrint_btn.setStyleSheet(("QPushButton {background-color : rgb(36, 149, 255)}"))
            else:
                self.ui.cameraTextEdit_1.clear()
                self.ui.cameraTextEdit_1.appendPlainText('Режим печати')

                if state_printer != 'Активна':
                    self.ui.startPrint_btn.setEnabled(False)
                    self.ui.startPrint_btn.setStyleSheet(("QPushButton {background-color : rgb(119, 119, 119)}"))
                else:
                    self.ui.startPrint_btn.setEnabled(True)
                    self.ui.startPrint_btn.setStyleSheet(("QPushButton {background-color : rgb(36, 149, 255)}"))

        elif currentPrinter == 1:
            selectedPrinter = 'PRINTER2'
            printMode = configFile.Config().configParser.get(selectedPrinter, "PrinteMode")
            if printMode == 'All':
                self.ui.cameraTextEdit_2.clear()
                self.ui.cameraTextEdit_2.appendPlainText('Печать с верификацией')
            elif printMode == 'Scan':
                self.ui.cameraTextEdit_2.clear()
                self.ui.cameraTextEdit_2.appendPlainText('Режим считывания')

                self.ui.startPrint_btn.setEnabled(True)
                self.ui.startPrint_btn.setStyleSheet(("QPushButton {background-color : rgb(36, 149, 255)}"))
            else:
                self.ui.cameraTextEdit_2.clear()
                self.ui.cameraTextEdit_2.appendPlainText('Режим печати')


        print(printMode)

    def startPrint(self):
        """Вызов потока принтера
            запуск печати на выбранном принтере"""
        currentPrinter = MainWindow.selectedPagePrinter(self)
        print(f'выбранный принтер {currentPrinter}')
        if currentPrinter == 0:
            # MainWindow.printer_1(self)
            MainWindow.thread_camera_1(self)
        elif currentPrinter == 1:
            # MainWindow.printer_2(self)
            MainWindow.thread_camera_2(self)

    # Принтер novex 64-04 (Обращение в поток)
    def printer_1(self):
        """Принтер Novex 64-04"""
        # Выборка и форматирвание даты наносимый на этикетку
        selectedDate = datetime.datetime.strptime(self.ui.dateEdit_1.text(), '%d.%m.%Y').date()
        self.dateForPrint = selectedDate.strftime('%d.%m.%Y')

        # Заполнение данных о печатаемом продукте
        item = self.ui.activOrder_Tab.selectedItems()
        self.ui.batchForPrint_label_1.setText(item[1].text())   # Номер задания
        self.ui.nameForPrint_label_1.setText(item[2].text())    # Наименование
        nameProd = self.ui.SelectedNameForPrint_label.text()    # Наименование наносимое на этикетку

        """if self.idTemplate == 1:
            selectedDate = datetime.datetime.strptime(self.ui.dateEdit_1.text(), '%d.%m.%Y').date()
            self.dateForPrint = selectedDate.strftime('%d.%m.%y')"""
        # Выгрузка КМ для отправки на печать
        listCode = MainWindow.loadKM_forPrint(self)

        # Печать всего заказа
        if self.idRadioButton == 0:
            MainWindow.threadPrinterNovex64(self, listCode, self.dateForPrint, nameProd)

        # Печать части заказа
        elif self.idRadioButton == 1:
            # Печать диапозона от выбранного числа и до конца
            if self.ui.countPrint_line.text() == '0' or self.ui.countPrint_line.text() == '':
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                MainWindow.threadPrinterNovex64(self, listCode[startCode:], self.dateForPrint, nameProd)
            # Печать диапозона от выбранного числа и до указанного ограничения
            elif int(self.ui.countPrint_line.text()) > 0:
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                endCode = (int(self.ui.startLabelPrint_Edit.text()) - 1) + int(self.ui.countPrint_line.text())
                MainWindow.threadPrinterNovex64(self, listCode[startCode:endCode], self.dateForPrint, nameProd)

    @Slot(bool)
    def statusSignal_Novex64(self, signalNovex64):
        """Метод получает сигнал о завершение печати"""
        if signalNovex64:
            MainWindow.terminatePrintNovex64(self)

    def threadPrinterNovex64(self, listForSentPrint, date, name):
        """Создаем поток принтера"""
        self.Novex64_thread = QThread()
        self.printerNovex = PrinterNovex.Novex(listForSentPrint, 0, date, name, 'PRINTER1')  # список кодов, ID шаблона, дата, наименование
        self.printerNovex.moveToThread(self.Novex64_thread)
        #self.printer.scanCodes.connect(self.scanCodeInRoll)

        self.printerNovex.stopSignal.connect(self.statusSignal_Novex64)
        self.Novex64_thread.started.connect(self.printerNovex.run)
        self.Novex64_thread.start()

    def pause_resume_Novex64(self):
        """Метод для постановки печати на паузу и продолжение печати для
            принтера Novex 64-04"""
        global pauseNovex64

        if not pauseNovex64:
            pauseNovex64 = True
            MainWindow.stopPrintNovex64(self)
            self.ui.pausePrint_btn_1.setStyleSheet(("QPushButton {background-color : rgb(0, 160, 20)}"))
        else:
            pauseNovex64 = False
            MainWindow.startPrintNovex64(self)
            self.ui.pausePrint_btn_1.setStyleSheet(("QPushButton {background-color : rgb(36, 149, 255)}"))

    def startPrintNovex64(self):
        """Отправляем список КМ для печати"""
        self.printerNovex.start()

    def stopPrintNovex64(self):
        self.printerNovex.stop()

    def clearPrintNovex64(self):
        printMode = configFile.Config().configParser.get('PRINTER1', "PrinteMode")
        if printMode == 'Scan':
            MainWindow.stopThread_camera_1(self)
        else:
            global pauseNovex64

            self.printerNovex.clear()
            pauseNovex64 = False
            self.ui.pausePrint_btn_1.setStyleSheet(("QPushButton {background-color : rgb(36, 149, 255)}"))
            MainWindow.terminatePrintNovex64(self)

    def terminatePrintNovex64(self):
        print('Останавливаю поток принтера')
        self.ui.batchForPrint_label_1.clear()
        self.ui.nameForPrint_label_1.clear()
        print('Отправляем сигнал на остановку потока камеры')
        MainWindow.stopThread_camera_1(self)
        # self.printerNovex.stop()
        self.Novex64_thread.quit()
        self.Novex64_thread.wait()

    # Принтер novex 504 (Обращение в поток)
    def printer_2(self):
        """Принтер Novex 504"""
        listforprint = []

        item = self.ui.activOrder_Tab.selectedItems()
        self.ui.batchForPrint_label_2.setText(item[1].text())
        self.ui.nameForPrint_label_2.setText(item[2].text())

        if self.idTemplate == 1:
            selectedDate = datetime.datetime.strptime(self.ui.dateEdit_2.text(), '%d.%m.%Y').date()
            self.dateForPrint = selectedDate.strftime('%d.%m.%y')

        listCode = MainWindow.loadKM_forPrint(self)
        if self.idRadioButton == 0:
            print('Печатаем весь заказа')
            MainWindow.threadPrinterNovex504(self, listCode)
            print(self.ui.dateEdit_2.text())
        elif self.idRadioButton == 1:
            print('Печатаем часть заказа')
            # print(listCode)

            # Печать диапозона от выбранного числа и до конца
            if self.ui.countPrint_line.text() == '0' or self.ui.countPrint_line.text() == '':
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                # print(listCode[startCode:])
                MainWindow.threadPrinterNovex504(self, listCode[startCode:])
            # Печать диапозона от выбранного числа и до указанного ограничения
            elif int(self.ui.countPrint_line.text()) > 0:
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                endCode = (int(self.ui.startLabelPrint_Edit.text()) - 1) + int(self.ui.countPrint_line.text())
                MainWindow.threadPrinterNovex504(self, listCode[startCode:endCode])  # , self.idTemplate, self.dateForPrint
        # MainWindow.threadPrinter(self)
        # self.scaner.start()

    @Slot(bool)
    def statusSignal_Novex504(self, signalNovex504):
        """Метод получает сигнал о завершение печати"""
        if signalNovex504:
            MainWindow.terminatePrintNovex504(self)

    def threadPrinterNovex504(self, listForSentPrint):
        """Создаем поток принтера"""
        self.Novex504_thread = QThread()
        self.printerNovex504 = PrinterNovex.Novex(listForSentPrint, 0, '', 'PRINTER2')  # список кодов, ID шаблона, дата
        self.printerNovex504.moveToThread(self.Novex504_thread)
        self.printerNovex504.stopSignal.connect(self.statusSignal_Novex504)
        self.Novex504_thread.started.connect(self.printerNovex504.run)
        self.Novex504_thread.start()

    def pause_resume_Novex504(self):
        """Метод для постановки печати на паузу и продолжение печати для
            принтера Novex 64-04"""
        global pauseNovex504

        if not pauseNovex504:
            pauseNovex504 = True
            MainWindow.stopPrintNovex504(self)
            self.ui.pausePrint_btn_2.setStyleSheet(("QPushButton {background-color : rgb(0, 160, 20)}"))
        else:
            pauseNovex504 = False
            MainWindow.startPrintNovex504(self)
            self.ui.pausePrint_btn_2.setStyleSheet(("QPushButton {background-color : rgb(36, 149, 255)}"))

    def startPrintNovex504(self):
        """Отправляем список КМ для печати"""
        self.printerNovex504.start()

    def stopPrintNovex504(self):
        self.printerNovex504.stop()

    def clearPrintNovex504(self):
        printMode = configFile.Config().configParser.get('PRINTER2', "PrinteMode")
        if printMode == 'Scan':
            MainWindow.stopThread_camera_2(self)
        else:
            global pauseNovex504

            self.printerNovex504.clear()
            pauseNovex504 = False
            self.ui.pausePrint_btn_2.setStyleSheet(("QPushButton {background-color : rgb(36, 149, 255)}"))
            MainWindow.terminatePrintNovex504(self)

    def terminatePrintNovex504(self):
        print('Останавливаю поток принтера')
        self.ui.batchForPrint_label_2.clear()
        self.ui.nameForPrint_label_2.clear()
        # self.printerNovex.stop()
        self.Novex504_thread.quit()
        self.Novex504_thread.wait()

    # Принтер TSC (Обращение в поток)
    def threadPrinter(self, listForSentPrint):
        """Создаем поток принтера"""
        #listForSentPrint = MainWindow.loadKM_forPrint(self)
        self.print_thread = QThread()
        self.printThread = PrinterTSC.TSC(listForSentPrint)
        self.printThread.moveToThread(self.print_thread)
        #self.printer.scanCodes.connect(self.scanCodeInRoll)
        #self.printer.infoSignal.connect(self.fillingPlainText)
        #self.print_thread.started.connect(self.printThread.run)
        self.print_thread.start()

    def sendListToPrint(self):
        """Отправляем список КМ для печати"""
        listForSentPrint = MainWindow.loadKM_forPrint(self)
        #print(listForSentPrint)
        self.printThread.run()

    def clearPrint(self):
        self.printThread.clear()

    def stop_threadPrinter(self):
        self.printThread.stop()
        self.print_thread.quit()
        self.print_thread.wait()

########################################################################################################################
###################################################### КАМЕРЫ ##########################################################
    #Камера для принтера 1 (novex 64-04)
    def thread_camera_1(self):
        printMode = configFile.Config().configParser.get('PRINTER1', "PrinteMode")
        if printMode == 'All' or printMode == 'Scan':
            """Создаем поток камеры"""
            self.camera64_04_thread = QThread()
            self.cameraNovex64_04 = socketCamera.Camera('CAMERA1')
            self.cameraNovex64_04.moveToThread(self.camera64_04_thread)
            # self.printer.scanCodes.connect(self.scanCodeInRoll)
            self.cameraNovex64_04.conSignal.connect(self.connectCameraSignal_1)
            self.cameraNovex64_04.readcode.connect(self.scanCodes)
            self.camera64_04_thread.started.connect(self.cameraNovex64_04.run)
            self.camera64_04_thread.start()
        else:
            MainWindow.printer_1(self)

    def stopThread_camera_1(self):
        self.cameraNovex64_04.stop()
        self.camera64_04_thread.quit()
        self.camera64_04_thread.wait()

    @Slot(bool)
    def connectCameraSignal_1(self, connSignal):
        """Проверка соединения с соккетом камеры"""
        if connSignal:
            self.ui.cameraTextEdit_1.appendPlainText(f"{(time.strftime('%H:%M:%S'))} - Есть подключение к камере")

            # Если включен режим печать с верифекацией, то подключаемся к принтеру
            printMode = configFile.Config().configParser.get('PRINTER1', "PrinteMode")
            if printMode == 'All':
                MainWindow.printer_1(self)
        else:
            self.ui.cameraTextEdit_1.appendPlainText(f"{(time.strftime('%H:%M:%S'))} - Ошибка подключения к камере")
            MainWindow.stopThread_camera_1(self)

    @Slot(str)
    def scanCodes(self, code):
        """Метод получения кодов с камеры и записи в БД"""
        print(code)

        self.printScanList.append(code)
        rollCode = self.ui.rollNumberEdit_1.text()
        queryDB.DatabaseConn('marking_db').queryInsert(
            'INSERT INTO serial.code_scaned(mark_code, group_code, status) VALUES (?,?,?)', (code, rollCode, 5))
        self.ui.cameraTextEdit_1.appendPlainText(f"{(time.strftime('%H:%M:%S'))} - {code}")
        if code == 'NOREAD':
            MainWindow.stopPrintNovex64(self)

        # Камера для принтера 1 (novex 64-04)

    def thread_camera_2(self):
        printMode = configFile.Config().configParser.get('PRINTER2', "PrinteMode")
        if printMode == 'All' or printMode == 'Scan':
            """Создаем поток камеры"""
            self.camera64_06_thread = QThread()
            self.cameraNovex64_06 = socketCamera.Camera('CAMERA2')
            self.cameraNovex64_06.moveToThread(self.camera64_06_thread)
            # self.printer.scanCodes.connect(self.scanCodeInRoll)
            self.cameraNovex64_06.conSignal.connect(self.connectCameraSignal_2)
            self.cameraNovex64_06.readcode.connect(self.scanCodes_2)
            self.camera64_06_thread.started.connect(self.cameraNovex64_06.run)
            self.camera64_06_thread.start()
        else:
            MainWindow.printer_2(self)

    def stopThread_camera_2(self):
        self.cameraNovex64_06.stop()
        self.camera64_06_thread.quit()
        self.camera64_06_thread.wait()

    @Slot(bool)
    def connectCameraSignal_2(self, connSignal):
        """Проверка соединения с соккетом камеры"""
        if connSignal:
            self.ui.cameraTextEdit_2.appendPlainText(f"{(time.strftime('%H:%M:%S'))} - Есть подключение к камере")
            self.ui.startPrint_btn.setEnabled(False)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")

            # Если включен режим печать с верифекацией, то подключаемся к принтеру
            printMode = configFile.Config().configParser.get('PRINTER2', "PrinteMode")
            if printMode == 'All':
                MainWindow.printer_2(self)
        else:
            self.ui.cameraTextEdit_2.appendPlainText(f"{(time.strftime('%H:%M:%S'))} - Ошибка подключения к камере")
            self.ui.startPrint_btn.setEnabled(True)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}"
                                                 "QPushButton: hover{background - color: rgb(66, 66, 66);")
            MainWindow.stopThread_camera_2(self)

    @Slot(str)
    def scanCodes_2(self, code):
        """Метод получения кодов с камеры и записи в БД"""
        print(code)
        self.ui.cameraTextEdit_2.appendPlainText(f"{(time.strftime('%H:%M:%S'))} - {code}")
        #self.printScanList.append(code)
        printMode = configFile.Config().configParser.get('PRINTER2', "PrinteMode")
        if code != 'NOREAD' and code != '':
            rollCode = self.ui.rollNumberEdit_2.text()
            queryDB.DatabaseConn('marking_db').queryInsert(
                'INSERT INTO serial.code_scaned(mark_code, group_code, status) VALUES (?,?,?)', (code, rollCode, 5))

        elif code == 'NOREAD' and printMode == 'All':
            MainWindow.pause_resume_Novex504(self)

########################################################################################################################
####################################################### ПОИСК ##########################################################
    def threadSearchScaner(self):
        """Создаем поток сканера для поиска"""
        self.searchThread = QThread()
        self.searchScaner = ui_scaner.SearchScaner()
        self.searchScaner.moveToThread(self.searchThread)
        self.searchScaner.searchCodes.connect(self.scanerSearchValue)
        #self.searchScaner.infoSearchSignal.connect(self.fillingPlainText)
        self.searchThread.started.connect(self.searchScaner.run)
        self.searchThread.start()

    def stop_threadSearchScaner(self):
        self.searchScaner.stop()
        self.searchThread.quit()
        self.searchThread.wait()

    @Slot(str)
    def scanerSearchValue(self, stringValue):
        """Вызов функции поиска с аргументом полученным со сканера"""
        self.ui.searchLine.setText(stringValue)
        MainWindow.searchFunction(self)

    def fillingKISearchTable(self, database, KIvalue):
        """Функция заполнения таблицы поиска КМ"""

        listKM = (queryDB.DatabaseConn(database).querySelectFetchall(
            "select created, updated, batch, group_number, status, aggregate_number from serial.mark_codes where code = " + "'" + KIvalue + "'"
        ))

        for string in listKM:

            codeCreated = string[0].strftime("%d.%m.%Y")
            if string[1] == None:
                codeUpdated = ''
            else:
                codeUpdated = string[1].strftime("%d.%m.%Y")
            #code = listKM[2]

            if string[4] == 0:
                codeStatus = 'Полный'
            elif string[4] == 1:
                codeStatus = 'Пустой'
            elif string[4] == 2:
                codeStatus = 'Брак'
            elif string[4] == 3:
                codeStatus = 'Печать'
            elif string[4] == 4:
                codeStatus = 'Новый'
            elif string[4] == 5:
                codeStatus = 'Напечатан'
            elif string[4] == 6:
                codeStatus = 'Экспорт'

            if string[3] == None:
                codeRoll = ''
            else:
                codeRoll = string[3]

            if string[5] == None:
                codeAggregate = ''
            else:
                codeAggregate = str(string[5])

            date = datetime.datetime.now()
            expiration_date = (date - string[0] )
            print(expiration_date)
            self.ui.KiSearchData_Tab.setItem(0, 0, QTableWidgetItem(str(codeCreated)))  # Дата получения
            self.ui.KiSearchData_Tab.setItem(0, 1, QTableWidgetItem(str(codeUpdated)))  # Дата обновления
            self.ui.KiSearchData_Tab.setItem(0, 2, QTableWidgetItem(str("")))           # Срок годности
            self.ui.KiSearchData_Tab.setItem(0, 3, QTableWidgetItem(string[2]))        # Номер заказа
            self.ui.KiSearchData_Tab.setItem(0, 4, QTableWidgetItem(codeAggregate))    # Код аггрегата
            self.ui.KiSearchData_Tab.setItem(0, 5, QTableWidgetItem(codeRoll))         # Код рулона
            self.ui.KiSearchData_Tab.setItem(0, 6, QTableWidgetItem(codeStatus))       # Статус
            self.ui.KiSearchData_Tab.setItem(0, 7, QTableWidgetItem(str(KIvalue)))     # КМ

    def fillingRollSearchTable(self, rollValue):
        """Функция заполнения таблицы с кодом рулона"""

        rollValuelist = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            "select code, batch, group_number from serial.mark_codes where group_number = " + "'" + rollValue + "'"
        ))
        countKM_in_Roll = len(rollValuelist)
        rollBatch = rollValuelist[0][1]
        print(countKM_in_Roll)
        print(rollBatch)
        self.ui.RollSearchData_Tab.setItem(0, 0, QTableWidgetItem(str(rollBatch)))  # Дата получения
        self.ui.RollSearchData_Tab.setItem(0, 1, QTableWidgetItem(str(rollValue)))  # Дата обновления
        self.ui.RollSearchData_Tab.setItem(0, 2, QTableWidgetItem(str(countKM_in_Roll)))  # Срок годности

    def fillingAggregatSearchTable(self, database, aggValue):
        """Функция заполения таблицы кодами аггрегата"""
        aggValuelist = (queryDB.DatabaseConn(database).querySelectFetchall(
            "select code, batch from serial.mark_codes where aggregate_number = " + "'" + aggValue + "'"
        ))

        while self.ui.aggSearchData_Tab.rowCount() > 0:
            self.ui.aggSearchData_Tab.removeRow(0)

        index = 0

        for data in aggValuelist:

            rowcount = self.ui.aggSearchData_Tab.rowCount()
            self.ui.aggSearchData_Tab.insertRow(rowcount)

            self.ui.aggSearchData_Tab.setItem(index, 0, QTableWidgetItem(str(index + 1)))
            self.ui.aggSearchData_Tab.setItem(index, 1, QTableWidgetItem(data[1]))
            self.ui.aggSearchData_Tab.setItem(index, 2, QTableWidgetItem(aggValue))
            self.ui.aggSearchData_Tab.setItem(index, 3, QTableWidgetItem(data[0]))
            index += 1

    def searchFunction(self):
        """Функция проверки длины поискового запроса.
            При определенной длине происходит поиск"""
        stateCheckBox = self.ui.archive_checkBox.isChecked()
        if stateCheckBox == True:
            database = 'archive_db'
            logging.info(f'Выбран режим поиска в архиве')
        else:
            logging.info(f'Выбран режим поиска в активных заказах')
            database = 'marking_db'
        searchValue = self.ui.searchLine.text()
        lengthValue = len(searchValue)
        print(searchValue)
        print(lengthValue)
        #ui_functions.UIFunctions.resultSearchBatchWindow(self)
        #height = self.ui.BatchResult_Container.height()

        match lengthValue:
            # Поиск по номеру заказа
            case count if 1 <= count <= 5:
                logging.info(f'Поиск по номеру заказа: {searchValue}')
                #ui_functions.UIFunctions.closeResultSearchWindow(self)
                lenQuery = len((queryDB.DatabaseConn(database).querySelectFetchone(
                    'select batch from serial.exchange_files where batch = ?', searchValue
                )))
                if lenQuery > 0:
                    fillingTabel = self.ui.batchData_Tab_2
                    MainWindow.loadStatusKM_function(self, fillingTabel, searchValue)
                    ui_functions.UIFunctions.resultSearchBatchWindow(self)
                #else:
                    #ui_functions.UIFunctions.closeResultSearchWindow(self)

            # Поиск по Коду рулона
            case count if 6 <= count <= 10:
                logging.info(f'Поиск по коду рулона: {searchValue}')
                lenQuery = len((queryDB.DatabaseConn(database).querySelectFetchall(
                    "select code from serial.mark_codes where group_number = " + "'" + searchValue + "'"
                )))
                if lenQuery > 0:
                    MainWindow.fillingRollSearchTable(self, searchValue)
                    ui_functions.UIFunctions.resultSearchRollCodeWindow(self)

                else:
                    print("нет Roll_number")

            # Поиск по Аггрегату или КМ
            case count if 11 <= count <= 42:
                if searchValue.find('\x1d') != -1:
                    print("поиск по коду активирован")
                    logging.info(f'Поиск по КМ: {searchValue}')
                    lenQuery = len((queryDB.DatabaseConn(database).querySelectFetchone(
                            'select * from serial.mark_codes where code = ?', searchValue
                        )))

                    if lenQuery > 0:
                        MainWindow.fillingKISearchTable(self, database, searchValue)
                        ui_functions.UIFunctions.resultSearchKIWindow(self)

                else:
                    logging.info(f'Поиск по коду аггрегата: {searchValue}')
                    lenQuery = len(queryDB.DatabaseConn(database).querySelectFetchall(
                        'select code from serial.mark_codes where aggregate_number = ' + "'" + searchValue + "'"))
                    print(f'количество {lenQuery}')
                    if lenQuery > 0:
                        MainWindow.fillingAggregatSearchTable(self, database, searchValue)
                        ui_functions.UIFunctions.resultSearchAggregatWindow(self)
                    else:
                        print("нет aggregat")

            # Поиск по КМ
            #case count if 30 <= count <= 42:
                #print("поиск по коду активирован")
                #logging.info(f'Поиск по КМ: {searchValue}')
                #lenQuery = len((queryDB.DatabaseConn(database).querySelectFetchone(
                #    'select * from serial.mark_codes where code = ?', searchValue
                #)))

                #if lenQuery > 0:
                #    MainWindow.fillingKISearchTable(self, database, searchValue)
                #    ui_functions.UIFunctions.resultSearchKIWindow(self)

            # не соответсвует длинам поиска
            case _:
                logging.info(f'{searchValue} не соответсвует не одному параметру длины поиска')
                ui_functions.UIFunctions.closeResultSearchWindow(self)

        self.ui.searchLine.clear()

########################################################################################################################
####################################################### ????? ##########################################################

    def tempUpdate(self):
        listcodes = queryDB.DatabaseConn('marking_db').querySelectFetchone(
            'Select code from serial.mark_codes where batch = ?', 2537)
        for item in listcodes:
            queryDB.DatabaseConn('marking_db').queryInsert(
                'insert into serial.code_scaned (mark_code, status, group_code) values(?,?,?)', (item,0, '2537001')
            )
            time.sleep(0.5)



        ###############################################################################

    def stopPrinting2(self):
        self.scaner.stop()

    def clearPrinting(self):
        self.scaner.clear()

    def loadModePrint(self, button):
        #print(button.text())
        if button.text() == 'Без даты':
            self.ui.dateEdit.setEnabled(False)
            self.template = 'TemplateDM'
            self.dateForPrint = ''
            self.idTemplate = 0

        elif button.text() == 'С датой':
            self.ui.dateEdit.setEnabled(True)
            self.template = 'TemplateWithDate'
            self.idTemplate = 1

        elif button.text() == 'Групповые':
            self.ui.dateEdit.setEnabled(False)
            self.template = 'TemplateGroup'
            self.idTemplate = 2
            self.dateForPrint = ''

    def loadToFile(self, button):
        #print(button.text())
        if button.text() == 'Сохранить в файл':
            self.ui.startPrint_btn.setEnabled(False)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            self.ui.saveCodeInFile_btn.setEnabled(True)
            self.ui.saveCodeInFile_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)};"
                                                     "QPushButton: hover{background - color: rgb(66, 66, 66);")
            self.idRadioButton = 2
        elif button.text() == 'Печать всех этикеток':
            self.ui.allPrint_rbtn.setChecked(True)
            self.ui.startPrint_btn.setEnabled(True)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}"
                                                 "QPushButton: hover{background - color: rgb(66, 66, 66);")
            self.ui.saveCodeInFile_btn.setEnabled(False)
            self.ui.saveCodeInFile_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            self.idRadioButton = 0
        elif button.text() == 'Число этикеток':
            self.ui.countPrint_line.setEnabled(True)
            self.ui.startLabelPrint_Edit.setEnabled(True)
            #self.ui.endLabelPrint_Edit.setEnabled(True)
            self.ui.startLabelPrint_Edit.setText('1')
            self.ui.endLabelPrint_Edit.setText(str(len(MainWindow.loadKM_forPrint(self))))
            self.idRadioButton = 1
            #self.ui.startLabelPrint_Edit.setValidator(QIntValidator(10))

    def search(self, s):
        # Clear current selection.
        self.ui.activOrder_Tab.setCurrentItem(None)

        if not s:
            # Empty string, don't search.
            return

        matching_items = self.ui.activOrder_Tab.findItems(s, Qt.MatchStartsWith)
        if matching_items:
            # We have found something.
            item = matching_items[0]  # Take the first.
            self.ui.activOrder_Tab.setCurrentItem(item)


    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW LINE PAGE
        if btnName == "lineButton" or btnName == "startLineButton":
            widgets.stackedWidget.setCurrentWidget(widgets.linePage)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass
            # UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW ORDER PAGE
        if btnName == "ordersButton" or btnName == "startOrdersButton":
            widgets.stackedWidget.setCurrentWidget(widgets.ordersPage)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass
            # UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW SETTING PAGE
        if btnName == "settingsButton" or btnName =="startSettingsButton":
            widgets.stackedWidget.setCurrentWidget(widgets.settingPage)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass

        # SHOW SEARCH PAGE
        if btnName == "searchButton" or btnName == "startSearchButton":
            widgets.stackedWidget.setCurrentWidget(widgets.searchePage)
            # запустить поток сканера
            MainWindow.threadSearchScaner(self)

        # SHOW PRINT PAGE
        if btnName == "printFrameButton":
            widgets.stackedWidget.setCurrentWidget(widgets.printPage)
            #MainWindow.printing(self)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass

        if btnName == "rollFrameButton":
            widgets.stackedWidget.setCurrentWidget(widgets.rollPage)
            #MainWindow.printing(self)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass



    def setPicture(self):
        """Загрузка изображение в заказ"""
        address = configFile.Config().configParser.get('BASE', "imageAddress")
        pixmap = QPixmap(f'{address}barcode.png')
        pixmap.width()
        pixmap.heightMM()
        self.ui.selectedImageDM.setPixmap(pixmap)



    def loadPrint(self):
        """Отправка задания на печать
            на выбраннный принтер"""
        listforprint = []
        if self.idTemplate == 1:
            selectedDate = datetime.datetime.strptime(self.ui.dateEdit.text(), '%d.%m.%Y').date()
            self.dateForPrint = selectedDate.strftime('%d.%m.%y')

        listCode = MainWindow.loadKM_forPrint(self)
        # print(self.idRadioButton)
        if self.idRadioButton == 0:
            # print('Печатаем весь заказа')
            MainWindow.threadTest(self, listCode, self.idTemplate, self.dateForPrint)
            #print(self.ui.dateEdit.text())
        elif self.idRadioButton == 1:
            # print('Печатаем часть заказа')
            #print(listCode)
            #print(self.ui.countPrint_line.text())

            # Печать диапозона от выбранного числа и до конца
            if self.ui.countPrint_line.text() == '0' or self.ui.countPrint_line.text() == '':
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                #print(listCode[startCode:])
                #MainWindow.threadTest(self, listCode[startCode:], self.idTemplate, self.dateForPrint)
            # Печать диапозона от выбранного числа и до указанного ограничения
            elif int(self.ui.countPrint_line.text()) > 0:
                #print(self.ui.startLabelPrint_Edit.text())
                startCode = int(self.ui.startLabelPrint_Edit.text())-1
                endCode = (int(self.ui.startLabelPrint_Edit.text())-1)+int(self.ui.countPrint_line.text())
                #print(listCode[startCode:endCode])
                #MainWindow.threadTest(self, listCode[startCode:endCode], self.idTemplate, self.dateForPrint)




    def orderFrame_ini(self):
        """Инициализация таблицы заказа и блокировка кнопок действий с заказом"""
        countColumn = self.ui.batchData_Tab.columnCount()
        print(countColumn)
        # Очистка таблицы
        while countColumn > 0:
            countColumn = countColumn - 1
            self.ui.batchData_Tab.setItem(0, countColumn, QTableWidgetItem(''))
            # countColumn = countColumn - 1

        self.ui.closeBatch_btn.setEnabled(False)
        self.ui.closeBatch_btn.setStyleSheet("QPushButton {background-color : rgb(255, 255, 255)}")

        self.ui.deleteBatch_btn.setEnabled(False)
        self.ui.deleteBatch_btn.setStyleSheet("QPushButton {background-color : rgb(255, 255, 255)}")

        self.ui.showKM_btn.setEnabled(False)
        self.ui.showKM_btn.setStyleSheet("QPushButton {background-color : rgb(255, 255, 255)}")

        self.ui.exportBatch_btn.setEnabled(False)
        self.ui.exportBatch_btn.setStyleSheet("QPushButton {background-color : rgb(255, 255, 255)}")

        self.ui.sendBatchOnLine_btn.setEnabled(False)
        self.ui.sendBatchOnLine_btn.setStyleSheet("QPushButton {background-color : rgb(255, 255, 255)}")

        self.ui.printButton.setEnabled(False)
        self.ui.printButton.setStyleSheet("QPushButton {background-color : rgb(255, 255, 255)}")

    def lineFrame_ini(self):
        """Инициализация таблицы заказа на странице линий и блокировка кнопок действий с заказом"""
        countRow = self.ui.batchOnLine_Tab.rowCount()
        print(countRow)
        # Очистка таблицы
        while self.ui.batchOnLine_Tab.rowCount() > 0:
            self.ui.batchOnLine_Tab.removeRow(0)

        self.ui.deleteOrderButton.setEnabled(False)
        #self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color : transparent)}")
        self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color : rgb(255, 255, 255)}")

        self.ui.closeOrderButton.setEnabled(False)
        self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color : transparent}")

        self.ui.New_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")
        self.ui.Work_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")
        self.ui.End_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")

    def loadBatch(self):
        """Заполнение Списка доступных для работы заказов"""

        logging.info(f'Заполняется таблица с доступными заказами')
        date = datetime.datetime.now()
        print(date)
        delta = datetime.timedelta(days=30)
        print(delta)

        # Выгрузка саписка активных заказов
        list_batch = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select batch, created, gtin from serial.exchange_files where status < 6 order by batch'))

        # Очистка таблицы ативных заказов
        while self.ui.activOrder_Tab.rowCount() > 0:
            self.ui.activOrder_Tab.removeRow(0)

        # Добавление строк по количеству доступных заказов
        for item in list_batch:
            rowcount = self.ui.activOrder_Tab.rowCount()
            self.ui.activOrder_Tab.insertRow(rowcount)

        # Заполнение таблицы заказами
        index = 0
        for batch_item in list_batch:
            live = ((batch_item[1] + delta) - date)
            print(live)
            gtinItem = batch_item[2]
            nameItem = queryDB.DatabaseConn('Marking_db').querySelectFetchone("select name from serial.product where gtin =?", gtinItem)
            if nameItem == []:
                nameItem = ['']
            #print(datetime.date())
            #dateLive = (filetype[0][2] + datetime.timedelta(days=30)).strftime("%d.%m.%Y")
            """date2 = batch_item[1]
            result = str(date) - str(date2)
            print(result)"""
            number = QTableWidgetItem(str(index + 1))
            number.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.activOrder_Tab.setItem(index, 0, QTableWidgetItem(number))
            self.ui.activOrder_Tab.setItem(index, 1, QTableWidgetItem(batch_item[0]))
            self.ui.activOrder_Tab.setItem(index, 2, QTableWidgetItem(str(nameItem[0])))
            self.ui.activOrder_Tab.setItem(index, 3, QTableWidgetItem(str(live)))
            index = index + 1

        MainWindow.orderFrame_ini(self)

    def loadKM_InKITU(self, agregateNumber):
        """Заполнение таблицы кодами относящихся к выбранному КИТУ"""
        logging.info(f'Выгрузка КМ по КИТУ {batchItem}')
        listKI_In_KITU = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select code, status from serial.mark_codes where aggregate_number = ' + str(agregateNumber)))
        return listKI_In_KITU

    def showKI_in_KITU(self):
        """Вызов окна с таблицей КМ по выбранному КИТУ"""
        item = self.ui.orderKITU_tab.selectedItems()
        selectedKITU = item[1].text()
        statusKITU = item[2].text()

        if statusKITU == 'Полный':
            listKI_In_KITU = MainWindow.loadKM_InKITU(self, selectedKITU)
            if self.ui.KI_from_KITU_Container.width() == 0:
                ui_functions.UIFunctions.ki_Window(self)

            """Создание таблицы для КМ"""
            while self.ui.ki_from_KITU_tab.rowCount() > 0:
                self.ui.ki_from_KITU_tab.removeRow(0)

            for data in listKI_In_KITU:
                rowcount = self.ui.ki_from_KITU_tab.rowCount()
                self.ui.ki_from_KITU_tab.insertRow(rowcount)

            index = 0
            for data in listKI_In_KITU:

                self.ui.ki_from_KITU_tab.setItem(index, 0, QTableWidgetItem(str(index + 1)))
                self.ui.ki_from_KITU_tab.setItem(index, 1, QTableWidgetItem(data[0]))
                if data[1] == 0:
                    statusKI = 'Полный'
                elif data[1] == 4:
                    statusKI = 'Новый'

                self.ui.ki_from_KITU_tab.setItem(index, 2, QTableWidgetItem(statusKI))
                index = index + 1
        else:
            if self.ui.KI_from_KITU_Container.width() > 0:
                ui_functions.UIFunctions.ki_Window(self)

        #print(listKI_In_KITU)
        #statusLine = item[1].text()

    def loadListKM(self):
        """Выгрузка КМ по выбранному заказу и формирование списка
        При нажатии на кнопку 'Показать КМ'"""
        # global listKMorder
        logging.info(f'Выгрузка КМ по заказу {batchItem}')
        listKMorder = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select created, updated, code, status, group_number, aggregate_number from serial.mark_codes where batch = ' + batchItem))
        return listKMorder

    def showListKM(self):
        """Вызов окна с таблицей всех КМ при нажатие на кнопку 'Показать КМ' """
        listKMorder = MainWindow.loadListKM(self)
        height = self.ui.codeContainer.height()
        indexID = 0
        if height == 0:

            for string in listKMorder:
                rowcount = self.ui.orderKM_tab.rowCount()
                self.ui.orderKM_tab.insertRow(rowcount)

                codeCreated = string[0]
                if string[1] == None:
                    codeUpdated = ''
                else:
                    codeUpdated = string[1]
                code = string[2].strip('\n\t')

                if string[3] == 0:
                    codeStatus = 'Полный'
                elif string[3] == 1:
                    codeStatus = 'Пустой'
                elif string[3] == 2:
                    codeStatus = 'Брак'
                elif string[3] == 3:
                    codeStatus = 'Печать'
                elif string[3] == 4:
                    codeStatus = 'Новый'
                elif string[3] == 5:
                    codeStatus = 'Напечатан'
                elif string[3] == 6:
                    codeStatus = 'Экспорт'

                if string[4] == None:
                    codeRoll = ''
                else:
                    codeRoll = string[4]

                if string[5] == None:
                    codeAggregate = ''
                else:
                    codeAggregate = string[5]

                self.ui.orderKM_tab.setItem(indexID, 0, QTableWidgetItem(str(indexID + 1)))
                self.ui.orderKM_tab.setItem(indexID, 1, QTableWidgetItem(str(codeCreated)))
                self.ui.orderKM_tab.setItem(indexID, 2, QTableWidgetItem(str(codeUpdated)))
                self.ui.orderKM_tab.setItem(indexID, 3, QTableWidgetItem(str(code)))
                self.ui.orderKM_tab.setItem(indexID, 4, QTableWidgetItem(codeStatus))
                self.ui.orderKM_tab.setItem(indexID, 5, QTableWidgetItem(codeRoll))
                self.ui.orderKM_tab.setItem(indexID, 6, QTableWidgetItem(codeAggregate))

                indexID = indexID + 1

    def loadStatusKM_function(self, tabelName, batch):
        """Функция для подсчета статусов КМ в выбранном заказе
        Активация кнопок действия с заказом"""
        listStatus = (queryDB.DatabaseConn('marking_db').querySelectFetchone(
            'select status from serial.mark_codes where batch = ?', int(batch)))

        filetype = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select filetype, status, created from serial.exchange_files where batch = ' + batch))
        dateCreated = filetype[0][2].strftime("%d.%m.%Y")
        dateLive = (filetype[0][2] + datetime.timedelta(days=30)).strftime("%d.%m.%Y")

        # Проверка и подсчет статутосов КМ
        codeNew = listStatus.count(4)
        codeToPrint = listStatus.count(3)
        codePrinting = listStatus.count(5)
        codeFull = listStatus.count(0)
        codeExport = listStatus.count(6)
        codeReject = listStatus.count(2)

        if codeNew > 0 or codeToPrint > 0:
            self.ui.printButton.setEnabled(True)
            self.ui.printButton.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")

        print(dateLive)
        # Заполнения таблицы
        tabelName.setItem(0, 0, QTableWidgetItem(dateCreated))
        tabelName.setItem(0, 1, QTableWidgetItem(batch))
        tabelName.setItem(0, 2, QTableWidgetItem(str(codeNew)))
        tabelName.setItem(0, 3, QTableWidgetItem(str(codeToPrint)))
        tabelName.setItem(0, 5, QTableWidgetItem(str(codeFull)))
        tabelName.setItem(0, 4, QTableWidgetItem(str(codePrinting)))
        tabelName.setItem(0, 6, QTableWidgetItem(str(codeReject))) # Брак
        tabelName.setItem(0, 7, QTableWidgetItem(str(codeExport)))
        tabelName.setItem(0, 8, QTableWidgetItem(dateLive))
        # Проверка статуса заказа (доступен/ отправлен на линию)
        if filetype[0][1] == 1:
            tabelName.setItem(0, 9, QTableWidgetItem('Доступен'))
            self.ui.sendBatchOnLine_btn.setEnabled(True)
            self.ui.sendBatchOnLine_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")

            self.ui.closeBatch_btn.setEnabled(True)
            self.ui.closeBatch_btn.setStyleSheet("QPushButton {background-color: rgb(36, 149, 255);}")

            self.ui.deleteBatch_btn.setEnabled(True)
            self.ui.deleteBatch_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")

            self.ui.showKM_btn.setEnabled(True)
            self.ui.showKM_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")

        elif filetype[0][1] == 2:
            tabelName.setItem(0, 9, QTableWidgetItem('На линии'))

            self.ui.closeBatch_btn.setEnabled(False)
            self.ui.closeBatch_btn.setStyleSheet("QPushButton {background-color: transparent;}")

            self.ui.deleteBatch_btn.setEnabled(False)
            self.ui.deleteBatch_btn.setStyleSheet("QPushButton {background-color : transparent;}")

            self.ui.showKM_btn.setEnabled(True)
            self.ui.showKM_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")
            # self.ui.showKM_btn.setStyleSheet("QPushButton : hover {background-color : rgb(33, 37, 43);}")
            # self.ui.showKM_btn.setStyleSheet("QPushButton : pressed {background-color : rgb(0, 147, 249);}")

            self.ui.sendBatchOnLine_btn.setEnabled(False)
            self.ui.sendBatchOnLine_btn.setStyleSheet("QPushButton {background-color : transparent;}")

        elif filetype[0][1] == 4:
            tabelName.setItem(0, 9, QTableWidgetItem('Завершен'))

            self.ui.sendBatchOnLine_btn.setEnabled(False)
            self.ui.sendBatchOnLine_btn.setStyleSheet("QPushButton {background-color : transparent;}")

        elif filetype[0][1] == 5:
            tabelName.setItem(0, 9, QTableWidgetItem('Выгружен с линии'))

            self.ui.closeBatch_btn.setEnabled(False)
            self.ui.closeBatch_btn.setStyleSheet("QPushButton {background-color: transparent;}")

            self.ui.deleteBatch_btn.setEnabled(False)
            self.ui.deleteBatch_btn.setStyleSheet("QPushButton {background-color : transparent;}")

            self.ui.showKM_btn.setEnabled(True)
            self.ui.showKM_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")
            # self.ui.showKM_btn.setStyleSheet("QPushButton : hover {background-color : rgb(33, 37, 43);}")
            # self.ui.showKM_btn.setStyleSheet("QPushButton : pressed {background-color : rgb(0, 147, 249);}")

        elif filetype[0][1] == 6:
            tabelName.setItem(0, 9, QTableWidgetItem('Экспортирован'))

        elif filetype[0][1] == 7:
            tabelName.setItem(0, 9, QTableWidgetItem('Закрыт'))

        elif filetype[0][1] == 8:
            tabelName.setItem(0, 9, QTableWidgetItem('Удален'))

        return listStatus

    def clickedBatch(self):
        """Подсчитывем статусы кодов и заполняем таблицу
            при выборе доступнуго заказа в таблице"""
        global batchItem
        ##################################Таблица КМ #################################################
        # Сворачивание окна просмотра КМ заказа при нажатие на другой заказ в таблице архивных заказов
        height = self.ui.codeContainer.height()
        if height > 0:
            ui_functions.UIFunctions.dmWindow(self)
        # Удаление всех строк в таблице КМ выбранного заказа при закрытие окна
        while self.ui.orderKM_tab.rowCount() > 0:
            self.ui.orderKM_tab.removeRow(0)

        ##################################Таблица КИТУ #################################################
        # Сворачивание окна просмотра КИТУ заказа при нажатие на другой заказ в таблице архивных заказов
        height = self.ui.KITUContainer.height()
        if height > 0:
            ui_functions.UIFunctions.kituWindow(self)
        # Удаление всех строк в таблице КМ выбранного заказа при закрытие окна
        while self.ui.orderKITU_tab.rowCount() > 0:
            self.ui.orderKITU_tab.removeRow(0)

        ##################################Таблица Линий #################################################
        # Сворачивание окна просмотра Линий для отправки заказа при нажатие на другой заказ в таблице архивных заказов
        height = self.ui.sendLineContainer.height()
        if height > 0:
            ui_functions.UIFunctions.sendLineWindow(self)
        # Удаление всех строк в таблице КМ выбранного заказа при закрытие окна
        while self.ui.sendLine_tab.rowCount() > 0:
            self.ui.sendLine_tab.removeRow(0)

        # Выгрузка КМ по номеру заказа из таблицы активных заказаов
        orderItem = self.ui.activOrder_Tab.selectedItems()
        batchItem = orderItem[1].text()


        fileValue = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select filetype, status from serial.exchange_files where batch = ' + batchItem))
        #print(fileValue[0][1])
        filetype = fileValue[0][0]
        statusBatch = fileValue[0][1]

        fillingTabel = self.ui.batchData_Tab
        MainWindow.loadStatusKM_function(self, fillingTabel, batchItem)

        listlist = MainWindow.loadStatusKM_function(self, fillingTabel, batchItem)
        codeNew = listlist.count(4)
        codeFull = listlist.count(0)
        codeToPrint = listlist.count(3)
        codePrinting = listlist.count(5)
        codeExport = listlist.count(6)

        # активауия/деактивация кнопки отправки заказа на линию
        if statusBatch == 1:
            self.ui.sendBatchOnLine_btn.setEnabled(True)
            self.ui.sendBatchOnLine_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")
        else:
            self.ui.sendBatchOnLine_btn.setEnabled(False)
            self.ui.sendBatchOnLine_btn.setStyleSheet("QPushButton {background-color : transparent;}")

        # активация/деактивация кнопки отображения таблицы групповых кодов
        if filetype == 1:
            self.ui.showKITU.setEnabled(True)
            self.ui.showKITU.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")
        else:
            self.ui.showKITU.setEnabled(False)
            self.ui.showKITU.setStyleSheet("QPushButton {background-color :  transparent;}")

        # активация/деактивация кнопки экспорта заказа (выгрузка КМ в документ для отчета)
        if codeFull > 0:
            self.ui.exportBatch_btn.setEnabled(True)
            self.ui.exportBatch_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")
        else:
            self.ui.exportBatch_btn.setEnabled(False)
            self.ui.exportBatch_btn.setStyleSheet("QPushButton {background-color : transparent;}")

        # активация/деактивация кнопки выгрузки КМ для печати
        if codeNew > 0 or codeToPrint > 0:
            self.ui.printButton.setEnabled(True)
            self.ui.printButton.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")

            """self.ui.sendBatchOnLine_btn.setEnabled(True)
            self.ui.sendBatchOnLine_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")"""
        else:
            """self.ui.sendBatchOnLine_btn.setEnabled(False)
            self.ui.sendBatchOnLine_btn.setStyleSheet("QPushButton {background-color : transparent;}")"""
            self.ui.printButton.setEnabled(False)
            self.ui.printButton.setStyleSheet("QPushButton {background-color : transparent;}")

    def loadLine(self):
        """ВКЛАДКА ЛИНИИ
        Заполнение таблицы доступных для работы линий. Проверка статуса сети (активна/не активна)"""
        batch = ''

        list_line = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select Name, IP from serial.Lines'))

        while self.ui.lineData_Tab.rowCount() > 0:
            self.ui.lineData_Tab.removeRow(0)

        for data in list_line:
            rowcount = self.ui.lineData_Tab.rowCount()
            self.ui.lineData_Tab.insertRow(rowcount)

        index = 0
        for ip in list_line:
            #print(ip)

            self.ui.lineData_Tab.setItem(index, 0, QTableWidgetItem(ip[0]))
            #self.ui.lineData_Tab.setItem(index, 2, QTableWidgetItem(ip[1]))
            self.ui.lineData_Tab.setItem(index, 1, QTableWidgetItem(localLine.ping(ip[1])))
            index = index + 1

    # self.tableWidget.setItem(3, 5, QtGui.QTableWidgetItem())
    # self.tableWidget.item(3, 5).setBackground(QtGui.QColor(100, 100, 150))

    def clickLineInTab(self):
        """Выгрузка данных по выбранной линии"""
        kortejBatch = ()
        listBatchOnLine = []
        global serverIP

        item = self.ui.lineData_Tab.selectedItems()
        self.nameLine = item[0].text()
        statusLine = item[1].text()

        if statusLine == 'Активна':
            if statusLine == 'Активна':
                itemIP = (queryDB.DatabaseConn('marking_db').querySelectFetchone(
                    "select ip from serial.lines where name = ?", self.nameLine))
                serverIP = (itemIP[0].strip(" '"))
                print(serverIP)
            """listActiveBatchInLine = (queryDB.DatabaseConn('client_db', server=serverIP).querySelectFetchall(
                'select batch, name from serial.exchange_files ex, serial.product pr where ex.gtin = pr.gtin'))"""
            listActiveBatchInLine = (queryDB.DatabaseConn('client_db', server=serverIP).querySelectFetchall(
                'select batch, gtin from serial.exchange_files order by batch'))
            # print(listActiveBatchInLine)

            while self.ui.batchOnLine_Tab.rowCount() > 0:
                self.ui.batchOnLine_Tab.removeRow(0)

            for data in listActiveBatchInLine:
                rowcount = self.ui.batchOnLine_Tab.rowCount()
                self.ui.batchOnLine_Tab.insertRow(rowcount)

            index = 0
            for item in listActiveBatchInLine:
                # print(ip)
                nameProduct = (queryDB.DatabaseConn('marking_db').querySelectFetchone(
                    "select name from serial.Product where gtin = ?", item[1]))
                countCodes = queryDB.DatabaseConn('client_db', server=serverIP).querySelectFetchone(
                    "select code from serial.mark_codes where batch = ?", item[0])
                countFullCodes = queryDB.DatabaseConn('client_db', server=serverIP).querySelectFetchone(
                    "select code from serial.mark_codes where status = 0 and batch = ?", item[0])
                self.ui.batchOnLine_Tab.setItem(index, 0, QTableWidgetItem(item[0]))
                self.ui.batchOnLine_Tab.setItem(index, 1, QTableWidgetItem(str(len(countCodes))))
                self.ui.batchOnLine_Tab.setItem(index, 2, QTableWidgetItem(str(len(countFullCodes))))
                if len(nameProduct):
                    self.ui.batchOnLine_Tab.setItem(index, 3, QTableWidgetItem(nameProduct[0]))
                index = index + 1

    def clickBatchInTab(self):
        """Выбор и отображение информации по заказам на выбранной линии"""
        global batchOnLine
        item = self.ui.batchOnLine_Tab.selectedItems()
        batchOnLine = item[0].text()

        print(batchOnLine)

        status = (queryDB.DatabaseConn('client_db', server=serverIP).querySelectFetchone(
            'select status from serial.exchange_files where batch =?', batchOnLine))
        if status[0] == 2:
            self.ui.New_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")
            self.ui.Work_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")
            self.ui.End_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")

            self.ui.deleteOrderButton.setEnabled(True)
            self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color: rgb(36, 149, 255);}")
            self.ui.deleteOrderButton.setStyleSheet("QPushButton:hover {background-color: rgb(66, 66, 66);}")
            self.ui.deleteOrderButton.setStyleSheet("QPushButton:pressed {background-color: rgb(245, 246, 250);}")
            self.ui.closeOrderButton.setEnabled(True)
            self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color: rgb(36, 149, 255);}")
            self.ui.closeOrderButton.setStyleSheet("QPushButton:hover {background-color: rgb(66, 66, 66);}")
            self.ui.closeOrderButton.setStyleSheet("QPushButton:pressed {background-color: rgb(245, 246, 250);}")


        elif status[0] == 3:
            self.ui.New_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")
            self.ui.Work_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")
            self.ui.End_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")

            self.ui.deleteOrderButton.setEnabled(False)
            self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color: transparent;}")
            self.ui.closeOrderButton.setEnabled(False)
            self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color: transparent;}")

        elif status[0] == 4:
            self.ui.New_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")
            self.ui.Work_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")
            self.ui.End_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")

            self.ui.deleteOrderButton.setEnabled(False)
            self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color: transparent;}")
            self.ui.closeOrderButton.setEnabled(True)
            self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color: rgb(36, 149, 255);}")
            self.ui.closeOrderButton.setStyleSheet("QPushButton:hover {background-color: rgb(66, 66, 66);}")
            self.ui.closeOrderButton.setStyleSheet("QPushButton:pressed {background-color: rgb(245, 246, 250);}")
        else:
            self.ui.New_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")
            self.ui.Work_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")
            self.ui.End_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")

            self.ui.deleteOrderButton.setEnabled(False)
            self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color: transparent;}")
            self.ui.closeOrderButton.setEnabled(False)
            self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color: transparent;}")

    def closeOrderOnLine(self):
        """Закрытие заказа на линии после того как заказ отработали на линии"""
        logging.info(f'Нажата кнопка закрыть заказ {batchOnLine} на линии')
        listMSG = ['getbatchfromline']
        # valueEX = MainWindow.clickLineInSendTab(self)
        # print(valueEX)
        print(batchOnLine)
        print("Начинаем отправку")
        ClientSocket = (queryDB.DatabaseConn('marking_db').querySelectFetchone(
                    "select IP from serial.Lines where name = ?", self.nameLine))
        # ClientSocket = configFile.Config().configParser.get('SERVER', "ClientSocket")
        listMSG.append(batchOnLine)
        listMSG.append(ClientSocket)
        # client.Client().reciveClient(listMSG)
        serverAnswer = client.Client().reciveClient(listMSG)
        print(serverAnswer)
        if serverAnswer:
            logging.info(f"Вызвана функция обновления заказов на линии после закрытия отработанного заказа")
            #MainWindow.clickLineInTab(self)

    def deleteOrderOnLine(self):
        """Удаление закза с линии
        Удалить можно только заказ в статсуе получен(2)"""
        logging.info(f'Нажата кнопка удалить заказ {batchOnLine} на линии')
        ClientIP_temp = (queryDB.DatabaseConn('marking_db').querySelectFetchone(
            "select IP from serial.Lines where name = ?", self.nameLine))
        print(str(ClientIP_temp).strip("]['"))
        ClientIP = str(ClientIP_temp).strip("]['")
        queryDB.DatabaseConn('client_db', ClientIP).queryDelete(
            'DELETE FROM serial.mark_codes WHERE batch=' + batchOnLine)
        queryDB.DatabaseConn('client_db', ClientIP).queryDelete(
            'DELETE FROM serial.exchange_files WHERE batch=' + batchOnLine)
        queryDB.DatabaseConn('marking_db').queryUpdate(
            "update serial.exchange_files set status = 1 where batch = " + batchOnLine)

    def closeOrderInBD(self):
        """Закрытие зааказа:
            Вызов функции переноса КМ на сервере:
            Переносим КМ в архивную БД
            Переносим Заказ в архивную ДБ"""
        logging.info(f'Нажата кнопка закрыть заказ {batchItem}')
        listMSG = ['closeorder']
        valueEX = MainWindow.clickLineInSendTab(self)
        # print(valueEX)
        print("Начинаем закрытие заказа")
        listMSG.append(batchItem)
        client.Client().reciveClient(listMSG)

    def deleteOrderInDB(self):
        """Удаление заказа:
            Удаление КМ из Mark_Codes
            Exchange_files
            Удаленини КМ из Group_codes"""
        logging.info(f'Нажата кнопка удалить заказ {batchItem}')
        print('Удаляем заказ ' + batchItem)
        queryDB.DatabaseConn('marking_db').queryUpdate(
            '''UPDATE serial.exchange_files SET status = 8 WHERE batch = ''' + batchItem)
        MainWindow.loadBatch(self)

    def sendBatchToLocalStation(self):
        """Отправка задания на линии при нажатии кнопки отправить"""
        logging.info(f'Нажата кнопка отправить заказ {batchItem} на линию')
        listMSG = ['sendbatchonline']
        valueEX = MainWindow.clickLineInSendTab(self)
        #print(valueEX)

        print("Начинаем отправку")
        exchangeList = queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select uuid, status, gtin from serial.exchange_files where batch =' + "'" + batchItem + "'")

        kortej = (exchangeList[0][0], exchangeList[0][1], batchItem, exchangeList[0][2])
        localIP = selectedLineIP
        listMSG.append(batchItem)
        listMSG.append(localIP[0])
        client.Client().reciveClient(listMSG)

    def exportOrder_function(self):
        """Экспорт выбранного заказа по нажатию кнопки "Экспорт":
            Отправка номера заказа на сервер
            и вызов функции создания выходного файла"""
        logging.info(f'Нажата кнопка экспортировать заказ {batchItem}')
        listMSG = ['export']
        valueEX = MainWindow.clickLineInSendTab(self)

        print("Начинаем экспорт")
        listMSG.append(batchItem)
        client.Client().reciveClient(listMSG)
        MainWindow.loadBatch(self)

    def loadLine_in_lin_box(self):
        index = 0
        list_line_in_box = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select Name, IP from serial.Lines'))

        while self.ui.sendLine_tab.rowCount() > 0:
            self.ui.sendLine_tab.removeRow(0)

        for data in list_line_in_box:
            rowcount = self.ui.sendLine_tab.rowCount()
            self.ui.sendLine_tab.insertRow(rowcount)

            self.ui.sendLine_tab.setItem(index, 0, QTableWidgetItem(str(index + 1)))
            self.ui.sendLine_tab.setItem(index, 1, QTableWidgetItem(data[0]))
            self.ui.sendLine_tab.setItem(index, 2, QTableWidgetItem(localLine.ping(data[1])))
            index += 1

    def loadKITU_in_tab(self):
        index = 0
        list_KITU_in_box = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select code, status from serial.group_codes where batch = ' + batchItem))

        while self.ui.orderKITU_tab.rowCount() > 0:
            self.ui.orderKITU_tab.removeRow(0)

        for data in list_KITU_in_box:
            if data[1] == 4:
                statusKITU = 'Новый'
            elif data[1] == 0:
                statusKITU = 'Полный'
            rowcount = self.ui.orderKITU_tab.rowCount()
            self.ui.orderKITU_tab.insertRow(rowcount)

            self.ui.orderKITU_tab.setItem(index, 0, QTableWidgetItem(str(index + 1)))
            self.ui.orderKITU_tab.setItem(index, 1, QTableWidgetItem(data[0]))
            self.ui.orderKITU_tab.setItem(index, 2, QTableWidgetItem(statusKITU))
            index += 1

    def selectLine_in_send_tab(self):
        """Выбор линии для отправки задания"""
        global selectedLineIP
        item = self.ui.sendLine_tab.selectedItems()
        lineName = item[1].text()
        statusLine = item[2].text()
        print(statusLine)
        if statusLine == 'Активна':
            self.ui.sendOrder_btn.setEnabled(True)
            self.ui.sendOrder_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}")
            self.ui.sendOrder_btn.setStyleSheet("QPushButton.hover {background-color : rgb(66, 66, 66);}")
        else:
            self.ui.sendOrder_btn.setEnabled(False)
            self.ui.sendOrder_btn.setStyleSheet("QPushButton {background-color : rgb(255, 255, 255);color : rgb(193, 193, 193);}")


        selectedLineIP = queryDB.DatabaseConn("Marking_db").querySelectFetchone("SELECT IP FROM SERIAL.LINES WHERE name =?",
                                                                lineName)
        print("Выбрана линия " + lineName)
        print(selectedLineIP)
        print(batchItem)

        #return selectedLineIP

    def clickLineInSendTab(self):
        """Подготовка данных для отправки на линиию"""
        listKMorder = MainWindow.loadListKM(self)

        listForSend = []
        kortej = ()

        for codeItem in listKMorder:
            code = codeItem[2]
            codeStatus = 4
            batch = batchItem
            kortej = kortej + (code, codeStatus, batch)
            listForSend.append(kortej)
            kortej = ()

        value = listForSend
        #print(value)
        return value

    def sendOrder_onLine(self):
        '''Отправка задания на линии при нажатии кнопки отправить'''
        valueEX = MainWindow.clickLineInSendTab(self)
        print(valueEX)

        print("Начинаем отправку")
        exchangeList = queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select uuid, status, gtin from serial.exchange_files where batch =' + "'" + batchItem + "'")

        #kortej = ()
        kortej = (exchangeList[0][0], exchangeList[0][1], batchItem, exchangeList[0][2])
        queryDB.DatabaseConn('client_db').queryInsert(
            'INSERT INTO serial.exchange_files (uuid, status, batch, gtin) VALUES (?,?,?,?)', kortej)


        queryDB.DatabaseConn('client_db').queryInsertMany(
            'INSERT INTO serial.mark_codes(code, status, batch) VALUES (?,?,?)', valueEX)

        """queryDB.DatabaseConn('client_db').queryInsert(
            'INSERT INTO serial.exchange_files (uuid, status, batch, gtin) VALUES (?,?,?)', value_ex)"""

        """IPlist = queryDB.DatabaseConn('marking_db').querySelectFetchone(
            'select IP from serial.Lines where name =' + "'" + lineName + "'"
        )"""


    ###############################################################################
    ########################### ВКЛАДКА НАСТРОЙКИ #################################
    # Обновление таблицы с продуктами на странице настроек
    def loadExistentProduct(self):
        # Выгрузка саписка активных заказов
        list_product = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select name, gtin, quantity from serial.Product order by name'))
        #print(list_product)
        # Очистка таблицы ативных заказов
        while self.ui.currentProd_Tab.rowCount() > 0:
            self.ui.currentProd_Tab.removeRow(0)

        # Добавление строк по количеству доступных заказов
        for item in list_product:
            rowcount = self.ui.currentProd_Tab.rowCount()
            self.ui.currentProd_Tab.insertRow(rowcount)

        # Заполнение таблицы заказами
        index = 0
        for product_item in list_product:
            """ive = (product_item[1] + delta) - date
            print(str(ive))"""

            #date2 = batch_item[1]
            #result = str(date) - str(date2)
            #print(result)

            self.ui.currentProd_Tab.setItem(index, 0, QTableWidgetItem(str(index + 1)))
            self.ui.currentProd_Tab.setItem(index, 1, QTableWidgetItem(product_item[0]))
            self.ui.currentProd_Tab.setItem(index, 2, QTableWidgetItem(product_item[1]))
            self.ui.currentProd_Tab.setItem(index, 3, QTableWidgetItem(str(product_item[2])))
            index = index + 1

        #MainWindow.orderFrame_ini(self)"""

    def clearcolor(self, lineName):
        """Возврат основного цвета строки ввода данных"""
        lineName.setStyleSheet("QLineEdit {border: 2px solid rgb(33, 37, 43);}")

    # Добавление продукта на странице настроек
    def addNewProduct(self):
        """Функция добавления нового продукта"""
        nameProduct = str(self.ui.productNameEdit.text())
        GTINProduct = str(self.ui.productGTINedit.text())
        countProduct = str(self.ui.productCountEdit.text())
        if nameProduct != '':
            if GTINProduct != '':
                if countProduct != '':

                    valueProd = [GTINProduct, nameProduct, countProduct]
                    queryDB.DatabaseConn('marking_db').queryInsert(
                        'INSERT INTO serial.Product (GTIN, name, quantity) VALUES (?,?,?)', valueProd)

                    ui_functions.UIFunctions.addProductWindow(self)
                    MainWindow.loadExistentProduct(self)
                    self.ui.productNameEdit.clear()
                    self.ui.productGTINedit.clear()
                    self.ui.productCountEdit.clear()
                else:
                    self.ui.productCountEdit.setStyleSheet("QLineEdit {border: 2px solid rgb(255, 85, 127);}")
            else:
                self.ui.productGTINedit.setStyleSheet("QLineEdit {border: 2px solid rgb(255, 85, 127);}")
        else:
            self.ui.productNameEdit.setStyleSheet("QLineEdit {border: 2px solid rgb(255, 85, 127);}")

    #Передача значений выбранной строки таблицы продуктов в переменные
    def sendRowProductSettingTable(self):
        global productName_item
        global GTIN_item
        global countProduct_item

        self.ui.editProductBtn.setEnabled(True)
        self.ui.deleteProductBtn.setEnabled(True)

        prodItem = self.ui.currentProd_Tab.selectedItems()
        productName_item = prodItem[1].text()
        GTIN_item = prodItem[2].text()
        countProduct_item = prodItem[3].text()

        self.ui.productNameUpdate.setText(productName_item)
        self.ui.productGTINeditUpdate.setText(GTIN_item)
        self.ui.productCountEditUpdate.setText(countProduct_item)

    #Удаление проудкта из таблицы на странице настроек
    def deleteProductInSettings(self):
        print(GTIN_item)
        self.ui.editProductBtn.setEnabled(False)
        self.ui.deleteProductBtn.setEnabled(False)

        queryDB.DatabaseConn('marking_db').queryDelete(
            'DELETE FROM serial.Product WHERE gtin=' + "'" + GTIN_item + "'")
        MainWindow.loadExistentProduct(self)

    # Редактирование данных о продукте на странице настроек
    def updateProductInSetting(self):
        print(GTIN_item)
        self.ui.editProductBtn.setEnabled(False)
        self.ui.deleteProductBtn.setEnabled(False)
        new_productName_item = str(self.ui.productNameUpdate.text())
        new_GTIN_item = str(self.ui.productGTINeditUpdate.text())
        new_countProduct_item = str(self.ui.productCountEditUpdate.text())
        queryDB.DatabaseConn('marking_db').queryUpdate(
            """UPDATE serial.product SET name = """ + """'""" + new_productName_item + """'""" + """, gtin = """ + """'""" + new_GTIN_item + """'""" + """, quantity = """ + """'""" + new_countProduct_item + """'""" + """ WHERE gtin = """ + """'""" + GTIN_item + """'""")

        ui_functions.UIFunctions.editProductWindow(self)
        MainWindow.loadExistentProduct(self)

        #self.ui.productNameUpdate.setText(productName_item)
        #self.ui.productGTINeditUpdate.setText(GTIN_item)
        #self.ui.productCountEditUpdate.setText(countProduct_item)

    # Обновление таблицы с линиями на странице настроек
    def loadExistentLines(self):
        # Выгрузка созданных линий
        list_lines = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select name, IP from serial.Lines'))

        # Очистка таблицы ативных заказов
        while self.ui.currentLine_Tab.rowCount() > 0:
            self.ui.currentLine_Tab.removeRow(0)

        # Добавление строк по количеству доступных заказов
        for item in list_lines:
            rowcount = self.ui.currentLine_Tab.rowCount()
            self.ui.currentLine_Tab.insertRow(rowcount)

        # Заполнение таблицы заказами
        index = 0
        for lines_item in list_lines:
            """ive = (product_item[1] + delta) - date
            print(str(ive))"""

            # date2 = batch_item[1]
            # result = str(date) - str(date2)
            # print(result)

            self.ui.currentLine_Tab.setItem(index, 0, QTableWidgetItem(str(index + 1)))
            self.ui.currentLine_Tab.setItem(index, 1, QTableWidgetItem(lines_item[0]))
            self.ui.currentLine_Tab.setItem(index, 2, QTableWidgetItem(lines_item[1]))
            index = index + 1

    # Добавление продукта на странице настроек
    def addNewLines(self):

        nameLines = str(self.ui.lineNameEdit.text())
        IPLines = str(self.ui.lineIPEdit.text())

        if nameLines != '':
            if IPLines !='':
                valueLines = [nameLines, IPLines]
                queryDB.DatabaseConn('marking_db').queryInsert(
                    'INSERT INTO serial.Lines (Name, IP) VALUES (?,?)', valueLines)

                ui_functions.UIFunctions.addLineWindow(self)
                MainWindow.loadExistentLines(self)
                # Очистка полей заполнения
                self.ui.lineNameEdit.clear()
                self.ui.lineIPEdit.clear()
            else:
                self.ui.lineIPEdit.setStyleSheet("QLineEdit {border: 2px solid rgb(255, 85, 127);}")
        else:
            self.ui.lineNameEdit.setStyleSheet("QLineEdit {border: 2px solid rgb(255, 85, 127);}")

    # Передача значений выбранной строки таблицы продуктов в переменные
    def sendRowLineSettingTable(self):
        global lineName_item
        global IP_item

        # Разблокировка кнопок редактирования значения линий
        self.ui.editLineBtn.setEnabled(True)
        self.ui.deleteLineBtn.setEnabled(True)

        lineItem = self.ui.currentLine_Tab.selectedItems()
        lineName_item = lineItem[1].text()
        IP_item = lineItem[2].text()

        self.ui.lineNameUpdate.setText(lineName_item)
        self.ui.lineIPUpdate.setText(IP_item)

    # Удаление проудкта из таблицы на странице настроек
    def deleteLineInSettings(self):
        print(IP_item)
        # Блокировка кнопок редактирования линий
        self.ui.editLineBtn.setEnabled(False)
        self.ui.deleteLineBtn.setEnabled(False)

        queryDB.DatabaseConn('marking_db').queryDelete(
            'DELETE FROM serial.Lines WHERE IP=' + "'" + IP_item + "'")
        MainWindow.loadExistentLines(self)

    # Редактирование данных о продукте на странице настроек
    def updateLineInSetting(self):
        print(IP_item)
        # Блокировка кнопок редактирования линий
        self.ui.editLineBtn.setEnabled(False)
        self.ui.deleteLineBtn.setEnabled(False)

        new_lineName_item = str(self.ui.lineNameUpdate.text())
        new_IP_item = str(self.ui.lineIPUpdate.text())

        queryDB.DatabaseConn('marking_db').queryUpdate(
            """UPDATE serial.Lines SET name = """ + """'""" + new_lineName_item + """'""" + """, IP = """ + """'""" + new_IP_item + """'""" + """ WHERE IP = """ + """'""" + IP_item + """'""")

        ui_functions.UIFunctions.editLineWindow(self)
        MainWindow.loadExistentLines(self)

        # self.ui.productNameUpdate.setText(productName_item)
        # self.ui.productGTINeditUpdate.setText(GTIN_item)
        # self.ui.productCountEditUpdate.setText(countProduct_item)

    ###############################################################################
    ########################### ВКЛАДКА ПОИСК #################################

    ###############################################################################
    ################################## ПОТОКИ #####################################
    @Slot(list)
    def emitCode(self, listFromPrint_temp):
        print(f'Список отпечатаннх {listFromPrint_temp}')
        listForUpdate = []
        listFromPrint = []
        for line in listFromPrint_temp:
            listFromPrint.append(line.strip().replace('~d029', '\x1d'))
        kortej = ()

        for code in listFromPrint:
            codeStatus = 5
            kortej = kortej + (code, codeStatus)
            listForUpdate.append(kortej)
            kortej = ()
        print(listForUpdate)

        """queryDB.DatabaseConn('marking_db').queryInsertMany(
            'INSERT INTO serial.code_scaned (mark_code, status) VALUES (?,?)', listForUpdate)"""
        #listForUpdate.clear()

    @Slot(bool)
    def stopPrinting(self, stope):
        print('пришел сигнал')
        if stope:
            MainWindow.stopPrintThread(self)

    @Slot(bool)
    def readyImage(self, stop):
        #print('Пришла картинка')
        if stop:
            MainWindow.setPicture(self)
            MainWindow.stopPrintThread(self)

    def printThread(self):
        return self.thread.isRunning()

    """def threadTest(self, code, idTemlate, date):
        global stopPrint
        # threadLive = MainWindow.printThread(self)
        # self.thread = QThread()
        #threadLive = self.thread.isRunning()
        #print(f'Поток {threadLive}')
        if not stopPrint:
            self.thread = QThread()
            stopPrint = True
        else:
            self.scaner = Printer.TestThread(code, idTemlate, date)
            self.scaner.moveToThread(self.thread)
            self.scaner.returnCode.connect(self.emitCode)
            self.scaner.stopSignal.connect(self.stopPrinting)
            self.thread.started.connect(self.scaner.run)
            self.thread.start()"""

    def stopPrintThread(self):
        self.scaner.stop()
        self.thread.quit()
        self.thread.wait()

    def threadImage(self, code):
        """Создаем поток создания картинки"""
        self.thread2 = QThread()
        self.createImage = imageSave.ImageThread(code)
        self.createImage.moveToThread(self.thread2)
        self.createImage.imageSignal.connect(self.readyImage)
        self.thread2.started.connect(self.createImage.run)
        self.thread2.start()

    def stopPrintThread(self):
        self.createImage.stop()
        self.thread2.quit()
        self.thread2.wait()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
