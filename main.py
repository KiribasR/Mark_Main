import time
import os
from ui_Master import *
from modules.orders import queryDB
from modules.orders import client
import sys
import datetime
import logging
import json
from logging.handlers import TimedRotatingFileHandler
from modules import ui_scaner
from modules import configFile
from modules import ui_functions
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules.lines import localLine
import PrinterNovex
import PrinterTSC
import imageSave
import socketCamera
import threading
from queue import Empty, Queue

stopPrint = False
pauseNovex64 = False
pauseNovex504 = False

"""logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(logDirect,
                                   when="s",
                                   interval=20,
                                   backupCount=5)
logger.addHandler(handler)
logger = logging.getLogger('Logs')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler = TimedRotatingFileHandler(f'{datetime.date.today().strftime("%d.%m.%Y")}.log', when="midnight", backupCount=3)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

logger.addHandler(handler)"""

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
        ####################################### Активация кнопок меню ##################################################
        # Кнопка меню "рулоны"
        if configFile.Config().configParser.get('BASE', "Roll") == '1':
            self.ui.rollFrameButton.setVisible(True)
        else:
            self.ui.rollFrameButton.setVisible(False)

        # Кнопка меню "создать задание"
        if configFile.Config().configParser.get('BASE', "PrintHouse") == '1':
            self.ui.selectLoadBatchMode_frame.setVisible(True)
            self.ui.createOrderButton.setVisible(True)
        else:
            self.ui.selectLoadBatchMode_frame.setVisible(False)
            self.ui.createOrderButton.setVisible(False)

        #self.ui.printer3_page.setVisible(False)


        self.printScanList = []
        ############################################# АНИМАЦИИ #########################################################
        # Смена размера колонок таблицы созданных заказов "для типографии"
        horizontalHeaderLastOrderTab = self.ui.lastOrder_Tab.horizontalHeader()
        horizontalHeaderLastOrderTab.resizeSection(0, 60)
        horizontalHeaderLastOrderTab.resizeSection(1, 150)
        horizontalHeaderLastOrderTab.resizeSection(2, 150)
        horizontalHeaderLastOrderTab.resizeSection(3, 200)
        horizontalHeaderLastOrderTab.resizeSection(4, 300)


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
        horizontalHeaderActivOrderTab.resizeSection(1, 100)
        horizontalHeaderActivOrderTab.resizeSection(2, 280)
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
        #widgets.startSettingsButton.clicked.connect(self.buttonClick)
        widgets.startCreateButton.clicked.connect(self.buttonClick)
        widgets.searchButton.clicked.connect(self.buttonClick)
        widgets.startSearchButton.clicked.connect(self.buttonClick)
        widgets.printFrameButton.clicked.connect(self.buttonClick)
        widgets.rollFrameButton.clicked.connect(self.buttonClick)
        widgets.createOrderButton.clicked.connect(self.buttonClick)




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
        self.ui.startLineButton.clicked.connect(lambda: MainWindow.lineFrame_ini(self))
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
        self.ui.deleteBatch_btn.clicked.connect(lambda: MainWindow.qMassegeDelete(self))

        # Вызов функции сохранения км в файл для печати
        self.ui.saveCodeInFile_btn.clicked.connect(lambda: MainWindow.saveCodeToPrintFile(self))
        self.ui.printButton.clicked.connect(lambda: MainWindow.detectionPrintMode(self, 'printKM'))
        self.ui.KITUsendPrint_button.clicked.connect(lambda: MainWindow.detectionPrintMode(self, 'printKITU'))

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
        #self.ui.startSettingsButton.clicked.connect(lambda: MainWindow.loadExistentProduct(self))
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
        self.ui.template_combobox.currentIndexChanged.connect(self.changeTemplateCombobox)
        self.ui.template_combobox_2.currentIndexChanged.connect(self.changeTemplateCombobox)
        self.ui.template_combobox_3.currentIndexChanged.connect(self.changeTemplateCombobox)
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
        #self.ui.pushButton.clicked.connect(lambda: MainWindow.testTemplate(self))
        #self.ui.pushButton_4.clicked.connect(lambda: MainWindow.sendListToPrint(self))

        ##################################testprint_2###################################


        #self.ui.pushButton_5.clicked.connect(lambda: MainWindow.startPrint(self))  # Запуск потока принтера
        #self.ui.pushButton_8.clicked.connect(lambda: MainWindow.startPrintNovex64(self))

        ##################################Создание заданий###################################
        self.ui.comboBox.activated.connect(lambda: MainWindow.createButtonEnabled(self))
        self.ui.createOrderBtn.clicked.connect(lambda: MainWindow.createNewOrder(self))
        MainWindow.loadProductList(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

########################################################################################################################
################################################ Смена рабочего окна ###################################################
    def activeButton(self, btn, buttonList):
        """Метод возвращает дефолтный цвет кнопки
            закрашивает кнопку выбранного экрана"""
        for button in buttonList:
            button.setStyleSheet("QPushButton {background-color : rgb(66, 66, 66)}"
                                   "QPushButton:hover {background-color: rgb(40, 44, 52)}"
                                   "QPushButton:pressed {background-color: rgb(36, 149, 255)}")
            button.setEnabled(True)

        if btn.objectName() == "startCreateButton":
            self.ui.createOrderButton.setStyleSheet("QPushButton {background-color : rgb(99, 99, 99)}")
        elif btn.objectName() == "startSearchButton":
            self.ui.searchButton.setStyleSheet("QPushButton {background-color : rgb(99, 99, 99)}")
        elif btn.objectName() == "startOrdersButton":
            self.ui.ordersButton.setStyleSheet("QPushButton {background-color : rgb(99, 99, 99)}")
        elif btn.objectName() == "startLineButton":
            self.ui.lineButton.setStyleSheet("QPushButton {background-color : rgb(99, 99, 99)}")
        elif btn.objectName() == "printButton":
            self.ui.printFrameButton.setStyleSheet("QPushButton {background-color : rgb(99, 99, 99)}")
        else:
            btn.setStyleSheet("QPushButton {background-color : rgb(99, 99, 99)}")

    def buttonClick(self):
        btn = self.sender()
        #print(btn)
        btnName = btn.objectName()
        btnList = [self.ui.createOrderButton, self.ui.ordersButton, self.ui.lineButton, self.ui.searchButton,
                   self.ui.printFrameButton, self.ui.rollFrameButton, self.ui.settingsButton]
        MainWindow.activeButton(self, btn, btnList)

        # SHOW LINE PAGE
        if btnName == "lineButton" or btnName == "startLineButton":
            widgets.stackedWidget.setCurrentWidget(widgets.linePage)
            self.ui.lineButton.setEnabled(False)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass

        # SHOW ORDER PAGE
        if btnName == "ordersButton" or btnName == "startOrdersButton":
            widgets.stackedWidget.setCurrentWidget(widgets.ordersPage)
            self.ui.ordersButton.setEnabled(False)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass

        # SHOW SETTING PAGE
        if btnName == "settingsButton" or btnName =="startSettingsButton":
            widgets.stackedWidget.setCurrentWidget(widgets.settingPage)
            self.ui.settingsButton.setEnabled(False)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass

        # SHOW SEARCH PAGE
        if btnName == "searchButton" or btnName == "startSearchButton":
            widgets.stackedWidget.setCurrentWidget(widgets.searchePage)
            # запустить поток сканера
            self.ui.searchButton.setEnabled(False)
            MainWindow.threadSearchScaner(self)

        # SHOW PRINT PAGE
        if btnName == "printFrameButton" or btnName == "printButton":
            widgets.stackedWidget.setCurrentWidget(widgets.printPage)
            self.ui.printFrameButton.setEnabled(False)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass

        # SHOW ROLL PAGE
        if btnName == "rollFrameButton":
            widgets.stackedWidget.setCurrentWidget(widgets.rollPage)
            self.ui.rollFrameButton.setEnabled(False)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass

        # SHOW CREATE PAGE
        if btnName == "createOrderButton" or btnName == "startCreateButton":
            widgets.stackedWidget.setCurrentWidget(widgets.createOrderPage)
            self.ui.createOrderButton.setEnabled(False)
            #MainWindow.loadProductList(self)
            MainWindow.loadCreatedBatch(self)
            MainWindow.fillingLastBatch(self)
            try:
                MainWindow.stop_threadSearchScaner(self)
            except:
                pass

########################################################################################################################
######################################## ФОРМИРОВАНИЕ ЗАДАНИЕ ДЛЯ ТИПОГРАФИИ ###########################################
    def loadProductList(self):
        """Метод выгружает из БД список продуктов и
            заполняет выпадающий список для выбора"""
        self.ui.comboBox.clear()

        productList = queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'Select gtin, name from serial.product', [])

        # Cоздание словаря
        self.dictonaryProduct = {}

        for value in productList:
            self.dictonaryProduct[value[0]] = value[1]

        # Заполнение выпадающего списка
        for key in self.dictonaryProduct.keys():
            self.ui.comboBox.addItem(self.dictonaryProduct.get(key))

    def loadCreatedBatch(self):
        """Метод выгружает все задания за текущую дату
            и присваевает следующий по порядку номер"""

        curDate = datetime.date.today()
        listCurDateBatch = queryDB.DatabaseConn('marking_db').querySelectFetchone(
            'Select batch from serial.exchange_files where mode = 1 and convert(Date, created) = ?', curDate)

        if len(listCurDateBatch):
            newBatch = int(max(listCurDateBatch))+1
        else:
            newBatch = int(curDate.strftime('%d%m%y')+'01')

        self.ui.numCreatedOrder_edit.setText(str(newBatch))

    def createButtonEnabled(self):
        """При выборе наименования продукта
         кнопка "создать" становится активной"""
        if not self.ui.createOrderBtn.isEnabled():
            self.ui.createOrderBtn.setEnabled(True)
            self.ui.createOrderBtn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                    "QPushButton:hover {background-color: rgb(40, 44, 52)}"
                                                    "QPushButton:pressed {background-color: rgb(36, 149, 255)}")

    def createButtonDisabled(self):
        """При создании задания
         кнопка "создать" становится неактивной"""
        if self.ui.createOrderBtn.isEnabled():
            self.ui.createOrderBtn.setEnabled(False)
            self.ui.createOrderBtn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")

    def fillingLastBatch(self):
        """Метод заполняет таблицу последними созданными заданиями"""
        listAllOrder = queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'Select batch, created, gtin from serial.exchange_files where mode = 1 order by created DESC', [])

        # Очистка таблицы ативных заказов
        while self.ui.lastOrder_Tab.rowCount() > 0:
            self.ui.lastOrder_Tab.removeRow(0)

        # Добавление строк по количеству доступных заказов
        for item in listAllOrder:
            rowcount = self.ui.lastOrder_Tab.rowCount()
            self.ui.lastOrder_Tab.insertRow(rowcount)

        # Заполнение таблицы заказами
        index = 0
        for order in listAllOrder:

            numOrder = order[0]
            createdOrder = order[1].strftime('%d.%m.%Y')
            gtinOrder = order[2]
            nameOrder = self.dictonaryProduct.get(gtinOrder)

            self.ui.lastOrder_Tab.setItem(index, 0, QTableWidgetItem(str(index+1)))
            self.ui.lastOrder_Tab.setItem(index, 1, QTableWidgetItem(numOrder))
            self.ui.lastOrder_Tab.setItem(index, 2, QTableWidgetItem(createdOrder))
            self.ui.lastOrder_Tab.setItem(index, 3, QTableWidgetItem(gtinOrder))
            self.ui.lastOrder_Tab.setItem(index, 4, QTableWidgetItem(nameOrder))
            index += 1

    def createNewOrder(self):
        """Метод заполняет сохраняет в БД созданное задание"""
        valueList = []

        uuid = f'printing_house{self.ui.numCreatedOrder_edit.text()}'
        filetype = 0
        status = 1
        batch = self.ui.numCreatedOrder_edit.text()

        for key, item in self.dictonaryProduct.items():
            if item == self.ui.comboBox.currentText():
                gtin = key
                pass

        out_uuid = uuid
        mode = 1

        valueList.append(uuid)
        valueList.append(filetype)
        valueList.append(status)
        valueList.append(batch)
        valueList.append(gtin)
        valueList.append(out_uuid)
        valueList.append(mode)

        queryDB.DatabaseConn('marking_db').queryInsert('INSERT INTO serial.exchange_files(uuid, filetype, status, batch, gtin, out_uuid, mode) '
                                                       'VALUES (?,?,?,?,?,?,?)', valueList)
        self.ui.comboBox.setCurrentIndex(-1)
        MainWindow.createButtonDisabled(self)
        MainWindow.fillingLastBatch(self)
        MainWindow.loadCreatedBatch(self)

########################################################################################################################
################################################### СКАНЕР/РУЛОН #######################################################
    def listInRoll(self, rollNumber):
        """Выгрузка км по введенному коду рулона
            Заполнение таблицы кодами с кодом рулона"""
        listCodeInRoll = queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'Select code, status from serial.mark_codes where group_number = ?', rollNumber)

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
        queryDB.DatabaseConn('marking_db').queryInsertMany(
                'INSERT INTO serial.code_scaned(mark_code, pack_code, status) VALUES (?,?,?)', listForSend)
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
    # def testTemplate(self):
    def saveCodeToPrintFile(self):
        """Метод сохранения КМ в файл"""
        listCode = MainWindow.loadKM_forPrint(self)
        direct = configFile.Config().configParser.get('BASE', "SaveFileDir")
        name = (f'{self.batchItem}.txt')
        save = QFileDialog.getSaveFileName(self, "Save File", f"{direct}{name}",  "Text file (*.txt)")

        if save:
            try:
                with open(save[0], "w") as f:
                    for code in listCode:
                        value = code.strip('\n\t')
                        f.write(f'{value}\n')
                queryDB.DatabaseConn('marking_db').queryUpdate(
                    '''UPDATE serial.mark_codes SET status = 3 WHERE batch = ''' + str(self.batchItem))

                logging.info(f'Выгружено на печать {len(listCode)} по заказу {self.batchItem}')
                MainWindow.loadStatusKM_function(self, self.ui.batchData_Tab, self.batchItem)
            except Exception as err:
                logging.info(f"Отмена сохранения файла с номером задания {self.batchItem}:{err} ")
                pass

    def loadKM_forPrint(self):
        """Выгрузка КМ в статусе Новый и Печать для отправки на печать"""
        logging.info(f'Выгружаем коды для печати по заказу {self.batchItem}')
        listCode = queryDB.DatabaseConn('marking_db').querySelectFetchone(
            'Select code from serial.mark_codes where (status = 4 or status = 3) and batch = ?', int(self.batchItem))
        return listCode

    def loadKITU_forPrint(self):
        """Выгрузка КИТУ в статусе Новый для отправки на печать"""
        logging.info(f'Выгружаем КИТУ для печати по заказу {self.batchItem}')
        listKITU = queryDB.DatabaseConn('marking_db').querySelectFetchone(
            'Select code from serial.group_codes where (status = 4 or status = 3) and batch = ?', int(self.batchItem))
        return listKITU

    def detectionPrintMode(self, btnName):
        """Определение способа печати:
            - Если через файл, то вызывает функцию сохранения файла
            - Если онлайн печать, то вызывает функцию печати"""
        # Блокировка кнопки окна печати
        # Определение функции печати (принтер или сохранение в файл)
        settingPrint = configFile.Config().configParser.get('BASE', "Mode")
        MainWindow.listPrintTemplates(self)

        if settingPrint == 'Printer':
            # Определение количества принтеров
            countPrint = configFile.Config().configParser.get('BASE', "PrinterCount")
            MainWindow.fillingPrinterTable(self, countPrint)

            print(btnName)

            # Закрашивание кнопки "Печать" левого меню
            self.ui.printButton.clicked.connect(self.buttonClick)
            MainWindow.transitionToPrinting(self, btnName)

            self.idRadioButton = 0
            self.ui.allPrint_rbtn.setChecked(True)
            self.dateForPrint = ''

            '''self.ui.startPrint_btn.setEnabled(True)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}"
                                                 "QPushButton: hover{background - color: rgb(66, 66, 66);")'''
            self.ui.saveCodeInFile_btn.setEnabled(False)
            self.ui.saveCodeInFile_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")

        else:
            MainWindow.saveCodeToPrintFile(self)
            self.ui.save_rbtn.setChecked(True)
            self.ui.startPrint_btn.setEnabled(False)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            self.ui.saveCodeInFile_btn.setEnabled(True)
            self.ui.saveCodeInFile_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)};"
                                                     "QPushButton: hover{background - color: rgb(66, 66, 66);")

    def listPrintTemplates(self):
        """Метод заполнения списка доступными шаблонами для печати"""
        # Предварительная очистка списка шаблонов
        self.ui.template_combobox.clear()
        self.ui.template_combobox_2.clear()
        self.ui.template_combobox_3.clear()

        listTemplate = os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\template\\Novex')
        print(listTemplate)
        # Заполнение выпадающего списка
        for value in listTemplate:
            self.ui.template_combobox.addItem(value.strip('.json'))
            self.ui.template_combobox_2.addItem(value.strip('.json'))
            self.ui.template_combobox_3.addItem(value.strip('.json'))

    def fillingPrinterTable(self, printerCount):
        """Метод заполнения таблицы доступными для печати принтерами:
         - наименование
         - статус"""
        indexPage = 0
        printerPage = 'printer'+str(indexPage+1) + '_page'
        #print(type(self.ui.printer1_page))
        for indexPage in range(3):
            self.ui.toolBox_2.setItemText(indexPage, 'Принтер не добавлен')
        self.ui.printer1_page.setVisible(False)
        self.ui.printer2_page.setVisible(False)
        self.ui.printer3_page.setVisible(False)

        # Очистка таблицы
        while self.ui.listPrinter_tab.rowCount() > 0:
            self.ui.listPrinter_tab.removeRow(0)

        # Добавление строк по количеству принтеров
        for i in range(int(printerCount)):
            rowcount = self.ui.listPrinter_tab.rowCount()
            self.ui.listPrinter_tab.insertRow(rowcount)

        # Заполнение таблицы наименованием принтеров
        index = 0
        for i in range(int(printerCount)):
            printerName = configFile.Config().configParser.get(f'PRINTER{index+1}', "Name")
            printerIP = configFile.Config().configParser.get(f'PRINTER{index+1}', "IP")
            printerPort = configFile.Config().configParser.get(f'PRINTER{index+1}', "Port")

            # Заполнение таблицы с наименованием принтеров
            number = str(index + 1)
            self.ui.listPrinter_tab.setItem(index, 0, QTableWidgetItem(number))
            self.ui.listPrinter_tab.setItem(index, 1, QTableWidgetItem(printerName))
            self.ui.listPrinter_tab.setItem(index, 2, QTableWidgetItem(localLine.ping(printerIP, int(printerPort))))

            self.ui.toolBox_2.setItemText(i, printerName)
            if index == 0:
                self.ui.printer1_page.setVisible(True)
            elif index == 1:
                self.ui.printer2_page.setVisible(True)
            else:
                self.ui.printer3_page.setVisible(True)

            index = index + 1

    def transitionToPrinting(self, btnName):
        """Функция печати или сохранение кодов в файл"""
        """ # Заполнение таблицы доступными для работы принтерами
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
        self.ui.listPrinter_tab.setItem(2, 2, QTableWidgetItem(localLine.ping(printerIP_3, int(printerPort_3))))"""

        # Переход на страницу печати
        widgets.stackedWidget.setCurrentWidget(widgets.printPage)
        btnList = [self.ui.createOrderButton, self.ui.ordersButton, self.ui.lineButton, self.ui.searchButton,
                   self.ui.printFrameButton, self.ui.rollFrameButton, self.ui.settingsButton]
        MainWindow.activeButton(self, self.ui.printButton, btnList)
        self.ui.dateEdit_1.setDate(datetime.date.today())

        # Заполнение названия
        printItem = self.ui.activOrder_Tab.selectedItems()
        self.ui.selectedBatchForPrint_label.setText(printItem[1].text())
        self.ui.SelectedNameForPrint_label.setText(printItem[2].text())

        # Очистка таблицы
        while self.ui.kmPrint_tab.rowCount() > 0:
            self.ui.kmPrint_tab.removeRow(0)

        # Заполнение таблицы кодами, предназначеными для печати
        if btnName == 'printKM':
            listCodes = MainWindow.loadKM_forPrint(self)
        elif btnName == 'printKITU':
            listCodes = MainWindow.loadKITU_forPrint(self)
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

        self.ui.allCountLabel.setText(f'Доступно для печати этикеток: {len(listCodes)}')

        # Проверка доступности принтера
        MainWindow.detectionPage_printer(self)

    def detectionPage_printer(self):
        """Функция определения текущей вкладки принтера
            блокирует кнопки печати если принтер отключен"""
        currentRowPrintTable = self.ui.listPrinter_tab.currentIndex().row()
        if currentRowPrintTable == -1:
            currentRowPrintTable = 0
        print('Позиция в таблице'+str(currentRowPrintTable))
        item = self.ui.listPrinter_tab.item(currentRowPrintTable, 2).text()

        if item != 'Активна':
            self.ui.startPrint_btn.setEnabled(False)
            self.ui.startPrint_btn.setStyleSheet(("QPushButton {background-color : rgb(119, 119, 119)}"))
        else:
            print('Проверяем шаблон')
            MainWindow.detectionTemplate(self, currentRowPrintTable)

    def changeTemplateCombobox(self, index):
        """При выборе шаблона вызывается активация кнопки печати"""
        MainWindow.detectionPage_printer(self)

    def detectionTemplate(self, curPrinter):
        """Проверка выбран ли шаблон"""

        # Проверка принтера 1
        if curPrinter == 0 or curPrinter == -1:
            if self.ui.template_combobox.currentIndex() == -1:
                self.ui.startPrint_btn.setEnabled(False)
                self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            else:
                self.ui.startPrint_btn.setEnabled(True)
                self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                      "QPushButton:hover {background-color: rgb(40, 44, 52)}"
                                                      "QPushButton:pressed {background-color: rgb(36, 149, 255)}")

        # Проверка принтера 2
        if curPrinter == 1:
            if self.ui.template_combobox_2.currentIndex() == -1:
                self.ui.startPrint_btn.setEnabled(False)
                self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            else:
                self.ui.startPrint_btn.setEnabled(True)
                self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                      "QPushButton:hover {background-color: rgb(40, 44, 52)}"
                                                      "QPushButton:pressed {background-color: rgb(36, 149, 255)}")

        # Проверка принтера 2
        if curPrinter == 2:

            if self.ui.template_combobox_3.currentIndex() == -1:
                self.ui.startPrint_btn.setEnabled(False)
                self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            else:
                self.ui.startPrint_btn.setEnabled(True)
                self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                      "QPushButton:hover {background-color: rgb(40, 44, 52)}"
                                                      "QPushButton:pressed {background-color: rgb(36, 149, 255)}")

    def loadToFile(self, button):
        """Выбор способа печати
            Полностью файл или часть кодов"""
        #print(button.text())
        if button.text() == 'Сохранить в файл':
            self.ui.startPrint_btn.setEnabled(False)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            self.ui.saveCodeInFile_btn.setEnabled(True)
            self.ui.saveCodeInFile_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                      "QPushButton:hover {background-color: rgb(40, 44, 52)}"
                                                      "QPushButton:pressed {background-color: rgb(36, 149, 255)}")
            self.idRadioButton = 2
        elif button.text() == 'Печать всех этикеток':
            self.ui.allPrint_rbtn.setChecked(True)
            """self.ui.startPrint_btn.setEnabled(True)
            self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255);}"
                                                 "QPushButton: hover{background - color: rgb(66, 66, 66);")"""
            self.ui.countPrint_line.setEnabled(False)
            self.ui.countPrint_line.clear()
            self.ui.saveCodeInFile_btn.setEnabled(False)
            self.ui.saveCodeInFile_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            MainWindow.detectionPage_printer(self)
            self.idRadioButton = 0
        elif button.text() == 'Число этикеток':
            self.ui.saveCodeInFile_btn.setEnabled(False)
            self.ui.saveCodeInFile_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
            self.ui.countPrint_line.setEnabled(True)
            self.ui.startLabelPrint_Edit.setEnabled(True)
            #self.ui.endLabelPrint_Edit.setEnabled(True)
            self.ui.startLabelPrint_Edit.setText('1')
            self.ui.endLabelPrint_Edit.setText(str(len(MainWindow.loadKM_forPrint(self))))
            MainWindow.detectionPage_printer(self)
            self.idRadioButton = 1
            #self.ui.startLabelPrint_Edit.setValidator(QIntValidator(10))

    def callInfoPrinter(self):
        item = self.ui.listPrinter_tab.selectedItems()
        positionPrint = item[0].text()
        if positionPrint == '1':
            self.ui.toolBox_2.setCurrentWidget(widgets.printer1_page)
            #MainWindow.definitionPrintMode(self)
            MainWindow.detectionPage_printer(self)
        elif positionPrint == '2':
            self.ui.toolBox_2.setCurrentWidget(widgets.printer2_page)
            #MainWindow.definitionPrintMode(self)
            MainWindow.detectionPage_printer(self)
        elif positionPrint == '3':
            self.ui.toolBox_2.setCurrentWidget(widgets.printer3_page)
            #MainWindow.definitionPrintMode(self)
            MainWindow.detectionPage_printer(self)

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
        MainWindow.detectionPage_printer(self)
        if currentPrinter == 0:
            selectedPrinter = 'PRINTER1'
            printMode = configFile.Config().configParser.get(selectedPrinter, "PrinteMode")

            if printMode == 'All':
                self.ui.cameraTextEdit_1.clear()
                self.ui.cameraTextEdit_1.appendPlainText('Печать с верификацией')

                """if state_printer != 'Активна':
                    self.ui.startPrint_btn.setEnabled(False)
                    self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
                else:
                    self.ui.startPrint_btn.setEnabled(True)
                    self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                         "QPushButton:hover {background-color: rgb(40, 44, 52)}"
                                                         "QPushButton:pressed {background-color: rgb(36, 149, 255)}")"""

            elif printMode == 'Scan':
                self.ui.cameraTextEdit_1.clear()
                self.ui.cameraTextEdit_1.appendPlainText('Режим считывания')

                self.ui.startPrint_btn.setEnabled(True)
                self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                     "QPushButton:hover {background-color: rgb(40, 44, 52)}"
                                                     "QPushButton:pressed {background-color: rgb(36, 149, 255)}")
            else:
                self.ui.cameraTextEdit_1.clear()
                self.ui.cameraTextEdit_1.appendPlainText('Режим печати')

                """if state_printer != 'Активна':
                    self.ui.startPrint_btn.setEnabled(False)
                    self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")
                else:
                    self.ui.startPrint_btn.setEnabled(True)
                    self.ui.startPrint_btn.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                         "QPushButton:hover {background-color: rgb(40, 44, 52)}"
                                                         "QPushButton:pressed {background-color: rgb(36, 149, 255)}")"""

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

        elif currentPrinter == 2:
            selectedPrinter = 'PRINTER3'
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
        elif currentPrinter == 2:
            # MainWindow.printer_2(self)
            MainWindow.printer_3(self)

    # Принтер novex 64-04 (Обращение в поток)
    def printer_1(self):
        """Принтер Novex 64-04"""
        # Выбор и форматирвание даты наносимый на этикетку
        selectedDate = datetime.datetime.strptime(self.ui.dateEdit_1.text(), '%d.%m.%Y').date()
        self.dateForPrint = selectedDate.strftime('%d.%m.%Y')

        # Заполнение данных о печатаемом продукте
        item = self.ui.activOrder_Tab.selectedItems()
        self.ui.batchForPrint_label_1.setText(item[1].text())   # Номер задания
        self.ui.nameForPrint_label_1.setText(item[2].text())    # Наименование
        nameProd = self.ui.SelectedNameForPrint_label.text()    # Наименование наносимое на этикетку

        # Выгрузка КМ для отправки на печать
        listCode = MainWindow.loadKM_forPrint(self)

        # Выбор шаблона
        template = self.ui.template_combobox.currentText()

        printerType = configFile.Config().configParser.get('PRINTER1', "Model")

        # Печать всего заказа
        if self.idRadioButton == 0:
            MainWindow.threadPrinter_1(self, template, listCode, self.dateForPrint, nameProd, printerType)

        # Печать части заказа
        elif self.idRadioButton == 1:
            # Печать диапозона от выбранного числа и до конца
            if self.ui.countPrint_line.text() == '0' or self.ui.countPrint_line.text() == '':
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                MainWindow.threadPrinter_1(self, template, listCode[startCode:], self.dateForPrint, nameProd, printerType)
            # Печать диапозона от выбранного числа и до указанного ограничения
            elif int(self.ui.countPrint_line.text()) > 0:
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                endCode = (int(self.ui.startLabelPrint_Edit.text()) - 1) + int(self.ui.countPrint_line.text())
                MainWindow.threadPrinter_1(self, template, listCode[startCode:endCode], self.dateForPrint, nameProd, printerType)

    @Slot(bool)
    def statusSignal_Printer1(self, signalNovex64):
        """Метод получает сигнал о завершение печати"""
        if signalNovex64:
            MainWindow.terminatePrintNovex64(self)

    def threadPrinter_1(self, template, listForSentPrint, date, name, printerType):
        """Создаем поток принтера"""
        self.Printer_1_thread = QThread()
        if printerType == 'Novex':
            self.printer1 = PrinterNovex.Novex(template, listForSentPrint, date, name, 'PRINTER1')  # имя шаблона, список кодов, ID шаблона, дата, наименование
            self.printer1.moveToThread(self.Printer_1_thread)
            #self.printer.scanCodes.connect(self.scanCodeInRoll)
            self.printer1.stopSignal.connect(self.statusSignal_Printer1)
            self.Printer_1_thread.started.connect(self.printer1.run)
            self.Printer_1_thread.start()
        elif printerType == 'TSC':
            self.printer1 = PrinterTSC.TSC(template, listForSentPrint, date, name, 'PRINTER1')  # имя шаблона, список кодов, ID шаблона, дата, наименование
            self.printer1.moveToThread(self.Printer_1_thread)
            # self.printer.scanCodes.connect(self.scanCodeInRoll)
            # self.printer1.stopSignal.connect(self.statusSignal_Printer1)
            self.Printer_1_thread.started.connect(self.printer1.run)
            self.Printer_1_thread.start()

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
        printMode = configFile.Config().configParser.get('PRINTER1', "PrinteMode")
        if printMode == 'Scan':
            MainWindow.stopThread_camera_1(self)
        #MainWindow.stopThread_camera_1(self)
        #self.printerNovex.stop()
        self.Printer_1_thread.quit()
        self.Printer_1_thread.wait()

    # Принтер novex 504 (Обращение в поток)
    def printer_2(self):
        """Принтер Novex 504"""
        # Выборка и форматирвание даты наносимый на этикетку
        selectedDate = datetime.datetime.strptime(self.ui.dateEdit_2.text(), '%d.%m.%Y').date()
        self.dateForPrint = selectedDate.strftime('%d.%m.%Y')

        # Заполнение данных о печатаемом продукте
        item = self.ui.activOrder_Tab.selectedItems()
        self.ui.batchForPrint_label_2.setText(item[1].text())  # Номер задания
        self.ui.nameForPrint_label_2.setText(item[2].text())  # Наименование
        nameProd = self.ui.SelectedNameForPrint_label.text()  # Наименование наносимое на этикетку

        # Выгрузка КМ для отправки на печать
        listCode = MainWindow.loadKM_forPrint(self)

        printerType = configFile.Config().configParser.get('PRINTER2', "Model")

        # Выбор шаблона
        template = self.ui.template_combobox_2.currentText()

        if self.idRadioButton == 0:
            print('Печатаем весь заказа')
            MainWindow.threadPrinter_2(self, template, listCode, self.dateForPrint, nameProd, printerType)
            print(self.ui.dateEdit_2.text())
        elif self.idRadioButton == 1:
            print('Печатаем часть заказа')
            # Печать диапозона от выбранного числа и до конца
            if self.ui.countPrint_line.text() == '0' or self.ui.countPrint_line.text() == '':
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                #print(listCode[startCode:])
                MainWindow.threadPrinter_2(self, template, listCode[startCode:], self.dateForPrint, nameProd, printerType)
            # Печать диапозона от выбранного числа и до указанного ограничения
            elif int(self.ui.countPrint_line.text()) > 0:
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                endCode = (int(self.ui.startLabelPrint_Edit.text()) - 1) + int(self.ui.countPrint_line.text())
                #print(listCode[startCode:endCode])
                MainWindow.threadPrinter_2(self, template, listCode[startCode:endCode], self.dateForPrint, nameProd, printerType)  # , self.idTemplate, self.dateForPrint

    @Slot(bool)
    def statusSignal_Printer2(self, signalStopPrinter3):
        """Метод получает сигнал о завершение печати"""
        if signalStopPrinter3:
            MainWindow.terminatePrint_2(self)

    def threadPrinter_2(self, template, listForSentPrint, date, name, printerType):
        """Создаем поток принтера"""
        self.Printer_2_thread = QThread()
        if printerType == 'Novex':
            self.printer2 = PrinterNovex.Novex(template, listForSentPrint, date, name, 'PRINTER2')  # имя шаблона, список кодов, ID шаблона, дата, наименование
            self.printer2.moveToThread(self.Printer_2_thread)
            #self.printer.scanCodes.connect(self.scanCodeInRoll)
            self.printer2.stopSignal.connect(self.statusSignal_Printer2)
            self.Printer_2_thread.started.connect(self.printer2.run)
            self.Printer_2_thread.start()
        elif printerType == 'TSC':
            self.printer2 = PrinterTSC.TSC(template, listForSentPrint, date, name, 'PRINTER2')  # имя шаблона, список кодов, ID шаблона, дата, наименование
            self.printer2.moveToThread(self.Printer_2_thread)
            # self.printer.scanCodes.connect(self.scanCodeInRoll)
            self.printer2.stopSignal.connect(self.statusSignal_Printer2)
            self.Printer_2_thread.started.connect(self.printer2.run)
            self.Printer_2_thread.start()

    def terminatePrint_2(self):
        print('Останавливаю поток принтера 2')
        self.ui.batchForPrint_label_2.clear()
        self.ui.nameForPrint_label_2.clear()
        print('Отправляем сигнал на остановку потока камеры')
        printMode = configFile.Config().configParser.get('PRINTER2', "PrinteMode")
        if printMode == 'Scan':
            MainWindow.stopThread_camera_2(self)
        #MainWindow.stopThread_camera_3(self)
        #self.printerNovex.stop()
        self.Printer_2_thread.quit()
        self.Printer_2_thread.wait()

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

    def printer_3(self):
        """Принтер TSC"""
        # Выборка и форматирвание даты наносимый на этикетку
        selectedDate = datetime.datetime.strptime(self.ui.dateEdit_3.text(), '%d.%m.%Y').date()
        self.dateForPrint = selectedDate.strftime('%d.%m.%Y')

        # Заполнение данных о печатаемом продукте
        item = self.ui.activOrder_Tab.selectedItems()
        self.ui.batchForPrint_label_3.setText(item[1].text())   # Номер задания
        self.ui.nameForPrint_label_3.setText(item[2].text())    # Наименование
        nameProd = self.ui.SelectedNameForPrint_label.text()    # Наименование наносимое на этикетку

        # Выгрузка КМ для отправки на печать
        listCode = MainWindow.loadKM_forPrint(self)

        # Выбор шаблона
        template = self.ui.template_combobox_3.currentText()

        printerType = configFile.Config().configParser.get('PRINTER3', "Model")

        # Печать всего заказа
        if self.idRadioButton == 0:
            MainWindow.threadPrinter_3(self, template, listCode, self.dateForPrint, nameProd, printerType)

        # Печать части заказа
        elif self.idRadioButton == 1:
            # Печать диапозона от выбранного числа и до конца
            if self.ui.countPrint_line.text() == '0' or self.ui.countPrint_line.text() == '':
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                MainWindow.threadPrinter_3(self, template, listCode[startCode:], self.dateForPrint, nameProd, printerType)
            # Печать диапозона от выбранного числа и до указанного ограничения
            elif int(self.ui.countPrint_line.text()) > 0:
                startCode = int(self.ui.startLabelPrint_Edit.text()) - 1
                endCode = (int(self.ui.startLabelPrint_Edit.text()) - 1) + int(self.ui.countPrint_line.text())
                MainWindow.threadPrinter_3(self, template, listCode[startCode:endCode], self.dateForPrint, nameProd, printerType)

    @Slot(bool)
    def statusSignal_Printer3(self, signalStopPrinter3):
        """Метод получает сигнал о завершение печати"""
        if signalStopPrinter3:
            MainWindow.terminatePrint_3(self)

    # Принтер TSC (Обращение в поток)
    def threadPrinter_3(self, template, listForSentPrint, date, name, printerType):
        """Создаем поток принтера"""
        self.Printer_3_thread = QThread()
        if printerType == 'Novex':
            self.printer3 = PrinterNovex.Novex(template, listForSentPrint, date, name, 'PRINTER3')  # имя шаблона, список кодов, ID шаблона, дата, наименование
            self.printer3.moveToThread(self.Printer_3_thread)
            # self.printer3.scanCodes.connect(self.scanCodeInRoll)
            self.printer3.stopSignal.connect(self.statusSignal_Printer3)
            self.Printer_3_thread.started.connect(self.printer3.run)
            self.Printer_3_thread.start()
        elif printerType == 'TSC':
            self.printer3 = PrinterTSC.TSC(template, listForSentPrint, date, name, 'PRINTER3')  # имя шаблона, список кодов, ID шаблона, дата, наименование
            self.printer3.moveToThread(self.Printer_3_thread)
            self.printer3.stopSignal.connect(self.statusSignal_Printer3)
            self.Printer_3_thread.started.connect(self.printer3.run)
            self.Printer_3_thread.start()
        #self.TSC_MX341 = QThread()
        #self.printerTSC341 = PrinterTSC.TSC(template, listForSentPrint, date, name, 'PRINTER3')
        #self.printerTSC341.moveToThread(self.TSC_MX341)
        #self.printer.scanCodes.connect(self.scanCodeInRoll)
        #self.printer.infoSignal.connect(self.fillingPlainText)
        # self.TSC_MX341.started.connect(self.printerTSC341.run)
        # self.TSC_MX341.start()

    """def threadPrinter_1(self, template, listForSentPrint, date, name, printerType):
        ""Создаем поток принтера""
        self.Printer_1_thread = QThread()
        if printerType == 'Novex':
            self.printer1 = PrinterNovex.Novex(template, listForSentPrint, date, name, 'PRINTER1')  # имя шаблона, список кодов, ID шаблона, дата, наименование
            self.printer1.moveToThread(self.Printer_1_thread)
            #self.printer.scanCodes.connect(self.scanCodeInRoll)
            self.printer1.stopSignal.connect(self.statusSignal_Printer1)
            self.Printer_1_thread.started.connect(self.printer1.run)
            self.Printer_1_thread.start()
        elif printerType == 'TSC':
            self.printer1 = PrinterTSC.TSC(template, listForSentPrint, date, name, 'PRINTER1')  # имя шаблона, список кодов, ID шаблона, дата, наименование
            self.printer1.moveToThread(self.Printer_1_thread)
            # self.printer.scanCodes.connect(self.scanCodeInRoll)
            # self.printer1.stopSignal.connect(self.statusSignal_Printer1)
            self.Printer_1_thread.started.connect(self.printer1.run)
            self.Printer_1_thread.start()"""

    def terminatePrint_3(self):
        print('Останавливаю поток принтера 3')
        self.ui.batchForPrint_label_3.clear()
        self.ui.nameForPrint_label_3.clear()
        print('Отправляем сигнал на остановку потока камеры')
        printMode = configFile.Config().configParser.get('PRINTER3', "PrinteMode")
        if printMode == 'Scan':
            MainWindow.stopThread_camera_3(self)
        #MainWindow.stopThread_camera_3(self)
        #self.printerNovex.stop()
        self.Printer_3_thread.quit()
        self.Printer_3_thread.wait()

    def sendListToPrint(self):
        """Отправляем список КМ для печати"""
        listForSentPrint = MainWindow.loadKM_forPrint(self)
        #print(listForSentPrint)
        self.printerTSC341.run()

    def clearPrint(self):
        self.printerTSC341.clear()

    def stop_threadPrinter(self):
        self.printerTSC341.stop()
        self.TSC_MX341.quit()
        self.TSC_MX341.wait()

########################################################################################################################
###################################################### КАМЕРЫ ##########################################################
    #Камера для принтера 1 (novex 64-04)
    def thread_camera_1(self):
        printMode = configFile.Config().configParser.get("PRINTER1", "PrinteMode")
        if printMode == "All" or printMode == "Scan":
            """Создаем поток камеры"""
            self.camera64_04_thread = QThread()
            self.cameraNovex64_04 = socketCamera.Camera("CAMERA1")
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
            "select created, updated, batch, group_number, status, aggregate_number from serial.mark_codes where code = ?", KIvalue))

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
            "select code, batch, group_number from serial.mark_codes where group_number = ?", rollValue))
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
            "select code, batch from serial.mark_codes where aggregate_number = ?", aggValue))

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
                    "select code from serial.mark_codes where group_number = ?", searchValue)))
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
################################################# ВКЛАДКА "ЗАКАЗЫ" #####################################################
    def loadBatch(self):
        """Заполнение Списка доступных для работы заказов"""
        logging.info(f'Заполняется таблица с доступными заказами')

        # Определение режима работы (Производство или типография+производство)
        mode = int(configFile.Config().configParser.get('BASE', "PrintHouse"))

        # Определние срока годности
        lifetime = int(configFile.Config().configParser.get('BASE', "LiveCodes"))
        date = datetime.datetime.now()
        delta = datetime.timedelta(days=lifetime)

        mabufacture = self.ui.mabufacture_checkBox.isChecked()
        printHouse = self.ui.printHouse_checkBox.isChecked()
        # Выгрузка списка активных заказов
        if mode == 0:
            list_batch = queryDB.DatabaseConn('marking_db').querySelectFetchall(
                'select batch, created, gtin from serial.exchange_files where status < 6 or status = 9 order by created desc',[])
        elif mode == 1:
            # Определение выбранного условия выгрузки активных заказов
            if mabufacture and not printHouse:
                list_batch = queryDB.DatabaseConn('marking_db').querySelectFetchall(
                    'select batch, created, gtin from serial.exchange_files where mode = 0 and status < 6 or status = 9 order by batch desc', [])
            elif not mabufacture and printHouse:
                list_batch = queryDB.DatabaseConn('marking_db').querySelectFetchall(
                    'select batch, created, gtin from serial.exchange_files where mode = 1 and status < 6 or status = 9 order by batch desc',
                    [])
            else:
                list_batch = queryDB.DatabaseConn('marking_db').querySelectFetchall(
                    'select batch, created, gtin from serial.exchange_files where status < 6 or status = 9 order by batch desc', [])

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
            orderNumber = batch_item[0]
            # Вычленение дня из отавшегося срока жизни
            livestring = str((batch_item[1] + delta) - date)
            live = f'{livestring[:str(livestring).find(" ")]} д.'

            gtinItem = batch_item[2]
            nameItem = self.dictonaryProduct.get(gtinItem)

            if nameItem == []:
                nameItem = ['']

            number = QTableWidgetItem(str(index + 1))
            self.ui.activOrder_Tab.setItem(index, 0, QTableWidgetItem(number))
            self.ui.activOrder_Tab.setItem(index, 1, QTableWidgetItem(orderNumber))
            self.ui.activOrder_Tab.setItem(index, 2, QTableWidgetItem(nameItem))
            self.ui.activOrder_Tab.setItem(index, 3, QTableWidgetItem(live))
            index += 1

        MainWindow.orderFrame_ini(self)

    def orderFrame_ini(self):
        """Инициализация таблицы заказа"""
        countColumn = self.ui.batchData_Tab.columnCount()
        print(countColumn)
        # Очистка таблицы
        while countColumn > 0:
            countColumn = countColumn - 1
            self.ui.batchData_Tab.setItem(0, countColumn, QTableWidgetItem(''))

        # Формирование списка кнопок для инициализации и блокировки
        self.orderBtnList = [self.ui.closeBatch_btn, self.ui.deleteBatch_btn, self.ui.showKM_btn, self.ui.exportBatch_btn,
                   self.ui.sendBatchOnLine_btn, self.ui.printButton, self.ui.showKITU]

        MainWindow.orderTabButtonDisabled(self, self.orderBtnList)
        MainWindow.iniFrameKMtable(self)

    def orderTabButtonDisabled(self, buttonList):
        """Блокировка кнопок действий с заказом"""
        for button in buttonList:
            button.setEnabled(False)
            button.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")

    def orderTabButtonEnabled(self, buttonList):
        """Активация кнопок действий с заказом"""
        MainWindow.orderTabButtonDisabled(self, self.orderBtnList)
        for button in buttonList:
            button.setEnabled(True)
            button.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                 "QPushButton:hover {background-color: rgb(66, 66, 66)}"
                                 "QPushButton:pressed {background-color: rgb(245, 246, 250)}")

    def iniFrameKMtable(self):
        """Инициализация фрейма (скрытие таблицб если были открыты) при выделении
            другого заказа или при переходе с другой страницы"""
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
        # Удаление всех строк в таблице линий выбранного заказа при закрытие окна
        while self.ui.sendLine_tab.rowCount() > 0:
            self.ui.sendLine_tab.removeRow(0)

    def clickedBatch(self):
        """Подсчитывем статусы кодов и заполняем таблицу
            при выборе доступнуго заказа в таблице"""
        MainWindow.iniFrameKMtable(self)
        #global batchItem

        # Выгрузка КМ по номеру заказа из таблицы активных заказаов
        orderItem = self.ui.activOrder_Tab.selectedItems()
        self.batchItem = str(orderItem[1].text())

        fileValue = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select filetype, status from serial.exchange_files where batch = ?', int(self.batchItem)))

        filetype = fileValue[0][0]
        statusBatch = fileValue[0][1]

        fillingTabel = self.ui.batchData_Tab
        #print(fillingTabel)
        #print(self.batchItem)
        MainWindow.loadStatusKM_function(self, fillingTabel, self.batchItem)

    def loadStatusKM_function(self, tabelName, batch):
        """Функция для подсчета статусов КМ в выбранном заказе
        Активация кнопок действия с заказом"""
        listActivetedButton = []

        # Выборка статусов всех КМ по выбранному заказу
        listStatus = (queryDB.DatabaseConn('marking_db').querySelectFetchone(
            'select status from serial.mark_codes where batch = ?', int(batch)))

        #print(f'List: {listStatus}')
        # Выборка данных по выбранному заказу (Тип файла, статус, дата создания)
        orderDataList = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select filetype, status, created from serial.exchange_files where batch = ?', int(batch)))
        fileTypeOrder = orderDataList[0][0]
        statusOrder = orderDataList[0][1]
        createdOrder = orderDataList[0][2]

        # Расчет даты окончания срока годности
        lifetime = int(configFile.Config().configParser.get('BASE', "LiveCodes"))
        dateCreated = createdOrder.strftime("%d.%m.%Y")
        dateLive = (createdOrder + datetime.timedelta(days=lifetime)).strftime("%d.%m.%Y")

        # Проверка и подсчет статутосов КМ
        codeNew = listStatus.count(4)
        codeToPrint = listStatus.count(3)
        codePrinting = listStatus.count(5)
        codeFull = listStatus.count(0)
        codeExport = listStatus.count(6)
        codeReject = listStatus.count(2)

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

        if codeNew > 0 or codeToPrint > 0:
            listActivetedButton.append(self.ui.printButton)

        # Проверка статуса заказа (доступен/ отправлен на линию)
        if statusOrder == 1:
            tabelName.setItem(0, 9, QTableWidgetItem('Доступен'))
            listActivetedButton.append(self.ui.sendBatchOnLine_btn)
            listActivetedButton.append(self.ui.closeBatch_btn)
            listActivetedButton.append(self.ui.deleteBatch_btn)
            listActivetedButton.append(self.ui.showKM_btn)
            if fileTypeOrder == 1:
                listActivetedButton.append(self.ui.showKITU)

        elif statusOrder == 2:
            tabelName.setItem(0, 9, QTableWidgetItem('На линии'))
            listActivetedButton.append(self.ui.showKM_btn)
            if fileTypeOrder == 1:
                listActivetedButton.append(self.ui.showKITU)

        elif statusOrder == 4:
            tabelName.setItem(0, 9, QTableWidgetItem('Завершен'))
            listActivetedButton.append(self.ui.showKM_btn)
            if fileTypeOrder == 1:
                listActivetedButton.append(self.ui.showKITU)

        elif statusOrder == 5:
            tabelName.setItem(0, 9, QTableWidgetItem('Выгружен с линии'))
            listActivetedButton.append(self.ui.showKM_btn)
            if fileTypeOrder == 1:
                listActivetedButton.append(self.ui.showKITU)

            if codeFull > 0:
                listActivetedButton.append(self.ui.exportBatch_btn)

        elif statusOrder == 6:
            tabelName.setItem(0, 9, QTableWidgetItem('Экспортирован'))

        elif statusOrder == 7:
            tabelName.setItem(0, 9, QTableWidgetItem('Закрыт'))

        elif statusOrder == 8:
            tabelName.setItem(0, 9, QTableWidgetItem('Удален'))

        elif statusOrder == 9:
            tabelName.setItem(0, 9, QTableWidgetItem('Открыт повторно'))
            listActivetedButton.append(self.ui.sendBatchOnLine_btn)
            listActivetedButton.append(self.ui.closeBatch_btn)
            listActivetedButton.append(self.ui.deleteBatch_btn)
            listActivetedButton.append(self.ui.showKM_btn)
            if fileTypeOrder == 1:
                listActivetedButton.append(self.ui.showKITU)

        MainWindow.orderTabButtonEnabled(self, listActivetedButton)

    def loadListKM(self, typeCode, agregateNumber=None):
        """Выгрузка КМ по выбранному заказу и формирование списка
        При нажатии на кнопку 'Показать КМ'"""
        if typeCode == 'KM':
            logging.info(f'Выгрузка КМ по заказу {self.batchItem}')
            listKMorder = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
                'select created, updated, code, status, group_number, aggregate_number from serial.mark_codes where batch = ?', int(self.batchItem)))
        elif typeCode == 'KITU':
            logging.info(f'Выгрузка КМ по КИТУ {self.batchItem}')
            listKMorder = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
                'select code, status from serial.group_codes where batch = ?', int(self.batchItem)))
        return listKMorder

    def showListKM(self):
        """Вызов окна с таблицей всех КМ при нажатие на кнопку 'Показать КМ' """
        listKMorder = MainWindow.loadListKM(self, 'KM')
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
                self.ui.orderKM_tab.setItem(indexID, 1, QTableWidgetItem(codeCreated.strftime("%H:%H:%S %d.%m.%Y")))
                self.ui.orderKM_tab.setItem(indexID, 2, QTableWidgetItem(codeUpdated.strftime("%H:%H:%S %d.%m.%Y")))
                self.ui.orderKM_tab.setItem(indexID, 3, QTableWidgetItem(str(code)))
                self.ui.orderKM_tab.setItem(indexID, 4, QTableWidgetItem(codeStatus))
                self.ui.orderKM_tab.setItem(indexID, 5, QTableWidgetItem(codeRoll))
                self.ui.orderKM_tab.setItem(indexID, 6, QTableWidgetItem(codeAggregate))

                indexID += 1

    def loadKM_InKITU(self, agregateNumber):
        """Заполнение таблицы кодами относящихся к выбранному КИТУ"""
        logging.info(f'Выгрузка КМ по КИТУ {self.batchItem}')
        listKI_In_KITU = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select code, status from serial.mark_codes where aggregate_number = ' + str(agregateNumber)))
        return listKI_In_KITU

    def loadKITU_in_tab(self):
        """Вызов окна с таблицей всех КИГУ при нажатие на кнопку 'Показать КИГУ' """
        list_KITU_in_box = MainWindow.loadListKM(self, 'KITU')
        index = 0
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

    def showKI_in_KITU(self):
        """Вызов окна с таблицей КМ по выбранному КИТУ"""
        item = self.ui.orderKITU_tab.selectedItems()
        selectedKITU = item[1].text()
        statusKITU = item[2].text()

        if statusKITU == 'Полный':
            listKI_In_KITU = MainWindow.loadListKM(self, 'KITU', selectedKITU)
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

    def closeOrderInBD(self):
        """Закрытие зааказа:
            Вызов функции переноса КМ на сервере:
            Переносим КМ в архивную БД
            Переносим Заказ в архивную ДБ"""
        logging.info(f'Нажата кнопка закрыть заказ {self.batchItem}')
        listMSG = ['closeorder']
        print("Начинаем закрытие заказа")
        listMSG.append(self.batchItem)
        client.Client().reciveClient(listMSG)

    def qMassegeDelete(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle('Удалить задание?')
        msgbox.setText(f'Вы уверенны,что хотите удалить задание {self.batchItem}?')
        msgbox.addButton('Да', QMessageBox.YesRole)
        msgbox.addButton('Нет', QMessageBox.NoRole)
        reply = msgbox.exec()
        print(reply)

        if reply == 0:
            logging.info(f'Пользователь подтвердил подвердил удаление заказа - {self.batchItem}')
            #print(f'Вызываем фугкцию удаления заказа - {self.batchItem}')
            MainWindow.deleteOrderInDB(self)
        else:
            logging.info(f'Пользователь отклонил удаления заказа - {self.batchItem}')

    def deleteOrderInDB(self):
        """Удаление заказа:
            Удаление КМ из Mark_Codes
            Exchange_files
            Удаленини КМ из Group_codes"""
        logging.info(f'Нажата кнопка удалить заказ {self.batchItem}')
        print('Удаляем заказ ' + self.batchItem)
        queryDB.DatabaseConn('marking_db').queryDelete('delete from serial.exchange_files WHERE batch = ''' + int(self.batchItem))
        queryDB.DatabaseConn('marking_db').queryDelete('delete from serial.mark_codes WHERE batch = ''' + int(self.batchItem))
        """queryDB.DatabaseConn('marking_db').queryUpdate(
            '''UPDATE serial.exchange_files SET status = 8 WHERE batch = ''' + self.batchItem)"""

        MainWindow.loadBatch(self)

    def sendBatchToLocalStation(self):
        """Отправка задания на линии при нажатии кнопки отправить"""
        logging.info(f'Нажата кнопка отправить заказ {self.batchItem} на линию')
        listMSG = ['sendbatchonline']
        #valueEX = MainWindow.clickLineInSendTab(self)

        print("Начинаем отправку")
        exchangeList = queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select uuid, status, gtin from serial.exchange_files where batch = ?', int(self.batchItem))

        kortej = (exchangeList[0][0], exchangeList[0][1], self.batchItem, exchangeList[0][2])
        localIP = selectedLineIP
        listMSG.append(self.batchItem)
        listMSG.append(localIP[0])
        client.Client().reciveClient(listMSG)

    def exportOrder_function(self):
        """Экспорт выбранного заказа по нажатию кнопки "Экспорт":
            Отправка номера заказа на сервер
            и вызов функции создания выходного файла"""
        logging.info(f'Нажата кнопка экспортировать заказ {self.batchItem}')
        listMSG = ['export']
        #valueEX = MainWindow.clickLineInSendTab(self)

        print("Начинаем экспорт")
        listMSG.append(self.batchItem)
        client.Client().reciveClient(listMSG)
        MainWindow.loadBatch(self)

    def loadLine_in_lin_box(self):
        index = 0
        list_line_in_box = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select Name, IP from serial.Lines', []))

        while self.ui.sendLine_tab.rowCount() > 0:
            self.ui.sendLine_tab.removeRow(0)

        for data in list_line_in_box:
            rowcount = self.ui.sendLine_tab.rowCount()
            self.ui.sendLine_tab.insertRow(rowcount)

            self.ui.sendLine_tab.setItem(index, 0, QTableWidgetItem(str(index + 1)))
            self.ui.sendLine_tab.setItem(index, 1, QTableWidgetItem(data[0]))
            self.ui.sendLine_tab.setItem(index, 2, QTableWidgetItem(localLine.ping(data[1])))
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
            self.ui.sendOrder_btn.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119);color : rgb(255, 255, 255);}")

        selectedLineIP = queryDB.DatabaseConn("Marking_db").querySelectFetchone("SELECT IP FROM SERIAL.LINES WHERE name =?",
                                                                lineName)
        print("Выбрана линия " + lineName)
        print(selectedLineIP)
        print(self.batchItem)

    def clickLineInSendTab(self):
        """Подготовка данных для отправки на линиию"""
        listKMorder = MainWindow.loadListKM(self)

        listForSend = []
        kortej = ()

        for codeItem in listKMorder:
            code = codeItem[2]
            codeStatus = 4
            batch = self.batchItem
            kortej = kortej + (code, codeStatus, batch)
            listForSend.append(kortej)
            kortej = ()

        value = listForSend
        return value

    def sendOrder_onLine(self):
        """Отправка задания на линии при нажатии кнопки отправить"""
        valueEX = MainWindow.clickLineInSendTab(self)
        print(valueEX)

        print("Начинаем отправку")
        exchangeList = queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select uuid, status, gtin from serial.exchange_files where batch = ?', int(self.batchItem))

        kortej = (exchangeList[0][0], exchangeList[0][1], self.batchItem, exchangeList[0][2])
        queryDB.DatabaseConn('client_db').queryInsert(
            'INSERT INTO serial.exchange_files (uuid, status, batch, gtin) VALUES (?,?,?,?)', kortej)

        queryDB.DatabaseConn('client_db').queryInsertMany(
            'INSERT INTO serial.mark_codes(code, status, batch) VALUES (?,?,?)', valueEX)

########################################################################################################################
################################################# ВКЛАДКА "ЛИНИИ" ######################################################
    def lineFrame_ini(self):
        """Инициализация таблицы заказа на странице линий и блокировка кнопок действий с заказом"""
        countRow = self.ui.batchOnLine_Tab.rowCount()
        print(countRow)
        # Очистка таблицы
        while self.ui.batchOnLine_Tab.rowCount() > 0:
            self.ui.batchOnLine_Tab.removeRow(0)

        self.ui.deleteOrderButton.setEnabled(False)
        self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")

        self.ui.closeOrderButton.setEnabled(False)
        self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color : rgb(119, 119, 119)}")

        self.ui.New_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")
        self.ui.Work_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")
        self.ui.End_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")

    def loadLine(self):
        """ВКЛАДКА ЛИНИИ
        Заполнение таблицы доступных для работы линий. Проверка статуса сети (активна/не активна)"""
        list_line = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select Name, IP from serial.Lines', []))

        while self.ui.lineData_Tab.rowCount() > 0:
            self.ui.lineData_Tab.removeRow(0)

        for data in list_line:
            rowcount = self.ui.lineData_Tab.rowCount()
            self.ui.lineData_Tab.insertRow(rowcount)

        index = 0
        for ip in list_line:
            self.ui.lineData_Tab.setItem(index, 0, QTableWidgetItem(ip[0]))
            self.ui.lineData_Tab.setItem(index, 1, QTableWidgetItem(localLine.ping(ip[1])))
            index += 1

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
                'select batch, gtin from serial.exchange_files order by batch', []))

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
                countRejectCodes = queryDB.DatabaseConn('client_db', server=serverIP).querySelectFetchone(
                    "select code from serial.mark_codes where status = 2 and batch = ?", item[0])
                self.ui.batchOnLine_Tab.setItem(index, 0, QTableWidgetItem(item[0]))
                self.ui.batchOnLine_Tab.setItem(index, 1, QTableWidgetItem(str(len(countCodes))))
                self.ui.batchOnLine_Tab.setItem(index, 2, QTableWidgetItem(str(len(countFullCodes))))
                self.ui.batchOnLine_Tab.setItem(index, 3, QTableWidgetItem(str(len(countRejectCodes))))
                if len(nameProduct):
                    self.ui.batchOnLine_Tab.setItem(index, 4, QTableWidgetItem(nameProduct[0]))
                index += 1

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
            self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                    "QPushButton:hover {background-color: rgb(66, 66, 66)}"
                                                    "QPushButton:pressed {background-color: rgb(245, 246, 250)}")
            self.ui.closeOrderButton.setEnabled(True)
            self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                    "QPushButton:hover {background-color: rgb(66, 66, 66)}"
                                                    "QPushButton:pressed {background-color: rgb(245, 246, 250)}")

        elif status[0] == 3:
            self.ui.New_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")
            self.ui.Work_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")
            self.ui.End_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")

            self.ui.deleteOrderButton.setEnabled(False)
            self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color: rgb(119, 119, 119);}")
            self.ui.closeOrderButton.setEnabled(False)
            self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color: rgb(119, 119, 119);}")

        elif status[0] == 4:
            self.ui.New_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")
            self.ui.Work_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")
            self.ui.End_lineEdit.setStyleSheet("QLineEdit{background-color : rgb(0, 125, 0);}")

            self.ui.deleteOrderButton.setEnabled(False)
            self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color: rgb(119, 119, 119);}")
            self.ui.closeOrderButton.setEnabled(True)
            self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color : rgb(36, 149, 255)}"
                                                   "QPushButton:hover {background-color: rgb(66, 66, 66)}"
                                                   "QPushButton:pressed {background-color: rgb(245, 246, 250)}")
        else:
            self.ui.New_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")
            self.ui.Work_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")
            self.ui.End_lineEdit.setStyleSheet("QLineEdit{background-color : transparent;}")

            self.ui.deleteOrderButton.setEnabled(False)
            self.ui.deleteOrderButton.setStyleSheet("QPushButton {background-color: rgb(119, 119, 119);}")
            self.ui.closeOrderButton.setEnabled(False)
            self.ui.closeOrderButton.setStyleSheet("QPushButton {background-color: rgb(119, 119, 119);}")

    def closeOrderOnLine(self):
        """Закрытие заказа на линии после того как заказ отработали на линии"""
        logging.info(f'Нажата кнопка закрыть заказ {batchOnLine} на линии')
        listMSG = ['getbatchfromline']
        print(batchOnLine)
        print("Начинаем отправку")
        ClientSocket = (queryDB.DatabaseConn('marking_db').querySelectFetchone(
            "select IP from serial.Lines where name = ?", self.nameLine))

        listMSG.append(batchOnLine)
        listMSG.append(ClientSocket)

        serverAnswer = client.Client().reciveClient(listMSG)
        print(serverAnswer)
        if serverAnswer:
            logging.info(f"Вызвана функция обновления заказов на линии после закрытия отработанного заказа")

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
        queryDB.DatabaseConn('client_db', ClientIP).queryDelete(
            'DELETE FROM serial.group_codes WHERE batch=' + batchOnLine)
        queryDB.DatabaseConn('marking_db').queryUpdate(
            "update serial.exchange_files set status = 1 where batch = " + batchOnLine)

########################################################################################################################
####################################################### ????? ##########################################################
    def clearPrinting(self):
        self.scaner.clear()

    """def loadModePrint(self, button):
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
            self.dateForPrint = ''"""



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

########################################################################################################################
################################################# ВКЛАДКА НАСТРОЙКИ ####################################################
    # Обновление таблицы с продуктами на странице настроек
    def loadExistentProduct(self):
        # Выгрузка саписка активных заказов
        list_product = (queryDB.DatabaseConn('marking_db').querySelectFetchall(
            'select name, gtin, quantity from serial.Product order by name', []))
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
            'select name, IP from serial.Lines', []))

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

########################################################################################################################
#################################################### ПОТОКИ ############################################################
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
    MainWindow.loadProductList
    sys.exit(app.exec())
