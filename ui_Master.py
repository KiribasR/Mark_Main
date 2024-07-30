# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MasterGvNNAT.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QButtonGroup,
    QCheckBox, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1478, 860)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"/*_______________________________________________________\n"
"Main Container */\n"
"#MainContainer {	\n"
"	background-color: rgb(245, 246, 250);\n"
"	border: None;\n"
"}\n"
"\n"
"#activOrderList {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"/*__________________________________________*/\n"
"#leftMenuContainer{	\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"\n"
"\n"
"/* MENUS */\n"
"#topAccFrame .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"\n"
"\n"
"}\n"
"/*_____________________*/\n"
"\n"
"#toggleBox .QPushButton  {	\n"
"	background-position: left center;\n"
"	border-left: 10px;\n"
"    background-repeat: no-repeat;\n"
""
                        "	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	/*border-left: 5px solid transparent;\n"
"	background-color: transparent;*/\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"	padding-right: 00px;\n"
"}\n"
"\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"/*_________________________________________*/\n"
"#topMenu .QPushButton  {	\n"
"	background-position: left center;\n"
"	border-left: 10px;\n"
"    background-repeat: no-repeat;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	/*border-left: 5px solid transparent;\n"
"	background-color: transparent;*/\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"	padding-right: 00px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(36, 149, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#topMenu .QPushButton"
                        ":isChecked{\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"#bottomMenu .QPushButton  {	\n"
"	background-position: left center;\n"
"	border-left: 10px;\n"
"    background-repeat: no-repeat;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	/*border-left: 5px solid transparent;\n"
"	background-color: transparent;*/\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"	padding-right: 00px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(36, 149, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"/*_______________________________________*/\n"
"#accMenuContainer {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#accTopMenu{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Label */\n"
"#label { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#closeAccButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
""
                        "#closeAccButton:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#closeAccButton:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"#loginForm{\n"
"	background-color: rgb(189, 147, 249);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#loginButton{	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 50px;\n"
"}\n"
" #changeWindowLogButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 5px;\n"
"}\n"
"#loginButton:hover {\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"#loginButton:pressed {	\n"
"	background-color: rgb(33, 37, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#loginFrame .QLineEdit{\n"
"	color: rgb("
                        "255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	padding:10px 10px;\n"
"	background-color: rgb(255, 170, 255);\n"
"}\n"
"\n"
"#registerButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"#changeWindowRegButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left:10px;\n"
"}\n"
"\n"
"\n"
"#registerButton:hover {\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"#registerButton:pressed {	\n"
"	background-color: rgb(33, 37, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#registerFrame .QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	padding:10px 10px;\n"
"	background-color: rgb(255, 170, 255);\n"
"}\n"
"\n"
"#topCentralContainer{	\n"
"	border:non"
                        "e;\n"
"	border-color: rgb(66, 66, 66);\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget\n"
"QTableWidget {	\n"
"	background-color: rgb(0, 85, 127);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}"
                        "\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QListWidget{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QListWidget:hover {\n"
"	border: "
                        "2px solid rgb(64, 71, 88);\n"
"}\n"
"QListWidget:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"#LineContainer#\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"#linePage .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#linePage.QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#linePage.QPushButton:pressed {\n"
"	"
                        "background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 25px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(255, 255, 255);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(36, 149, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px"
                        ";\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(255, 255, 255);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(36, 149, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
""
                        "    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid 36, 149, 255;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: transparent;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(36, 149, 255);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboB"
                        "ox */\n"
"QComboBox{\n"
"	background-color: rgb(245, 246, 250);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/*LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(245, 246, 250);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	paddi"
                        "ng-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);}")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainContainer = QFrame(self.styleSheet)
        self.MainContainer.setObjectName(u"MainContainer")
        self.MainContainer.setStyleSheet(u"")
        self.MainContainer.setFrameShape(QFrame.StyledPanel)
        self.MainContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.MainContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QFrame(self.MainContainer)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(60, 16777215))
        self.leftMenuContainer.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.leftMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.leftMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topAccFrame = QFrame(self.leftMenuContainer)
        self.topAccFrame.setObjectName(u"topAccFrame")
        self.topAccFrame.setMinimumSize(QSize(0, 0))
        self.topAccFrame.setMaximumSize(QSize(16777215, 50))
        self.topAccFrame.setFrameShape(QFrame.StyledPanel)
        self.topAccFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topAccFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.userButton = QPushButton(self.topAccFrame)
        self.userButton.setObjectName(u"userButton")
        self.userButton.setEnabled(False)
        self.userButton.setMinimumSize(QSize(0, 50))
        self.userButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);")
        self.userButton.setIconSize(QSize(50, 50))

        self.verticalLayout_3.addWidget(self.userButton)


        self.verticalLayout_2.addWidget(self.topAccFrame)

        self.leftMenuFrame = QFrame(self.leftMenuContainer)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.leftMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.toggleBox.setFrameShape(QFrame.StyledPanel)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(0, 50))
        self.toggleButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleButton.setIcon(icon)
        self.toggleButton.setIconSize(QSize(50, 50))

        self.verticalLayout_5.addWidget(self.toggleButton)


        self.verticalLayout_4.addWidget(self.toggleBox, 0, Qt.AlignTop)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.topMenu.setFrameShape(QFrame.StyledPanel)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.topMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.createOrderButton = QPushButton(self.topMenu)
        self.createOrderButton.setObjectName(u"createOrderButton")
        self.createOrderButton.setMinimumSize(QSize(0, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-task.png", QSize(), QIcon.Normal, QIcon.Off)
        self.createOrderButton.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.createOrderButton)

        self.ordersButton = QPushButton(self.topMenu)
        self.ordersButton.setObjectName(u"ordersButton")
        self.ordersButton.setMinimumSize(QSize(0, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icons8-\u0441\u043f\u0438\u0441\u043e\u043a-\u0434\u0435\u043b-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ordersButton.setIcon(icon2)
        self.ordersButton.setIconSize(QSize(18, 18))
        self.ordersButton.setCheckable(True)

        self.verticalLayout_6.addWidget(self.ordersButton)

        self.lineButton = QPushButton(self.topMenu)
        self.lineButton.setObjectName(u"lineButton")
        self.lineButton.setMinimumSize(QSize(0, 50))
        self.lineButton.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icons8-\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lineButton.setIcon(icon3)
        self.lineButton.setIconSize(QSize(18, 18))
        self.lineButton.setCheckable(True)
        self.lineButton.setChecked(False)

        self.verticalLayout_6.addWidget(self.lineButton)

        self.searchButton = QPushButton(self.topMenu)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(0, 50))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon4)
        self.searchButton.setCheckable(True)

        self.verticalLayout_6.addWidget(self.searchButton)

        self.printFrameButton = QPushButton(self.topMenu)
        self.printFrameButton.setObjectName(u"printFrameButton")
        self.printFrameButton.setMinimumSize(QSize(0, 50))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.printFrameButton.setIcon(icon5)
        self.printFrameButton.setCheckable(True)

        self.verticalLayout_6.addWidget(self.printFrameButton)

        self.rollFrameButton = QPushButton(self.topMenu)
        self.rollFrameButton.setObjectName(u"rollFrameButton")
        self.rollFrameButton.setMinimumSize(QSize(0, 50))
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-cut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rollFrameButton.setIcon(icon6)
        self.rollFrameButton.setCheckable(True)

        self.verticalLayout_6.addWidget(self.rollFrameButton)


        self.verticalLayout_4.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.bottomMenu.setFrameShape(QFrame.StyledPanel)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.settingsButton = QPushButton(self.bottomMenu)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(0, 50))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon7)
        self.settingsButton.setIconSize(QSize(50, 50))
        self.settingsButton.setCheckable(True)

        self.verticalLayout_7.addWidget(self.settingsButton)


        self.verticalLayout_4.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.leftMenuFrame, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.accMenuContainer = QFrame(self.MainContainer)
        self.accMenuContainer.setObjectName(u"accMenuContainer")
        self.accMenuContainer.setMinimumSize(QSize(0, 0))
        self.accMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.accMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.accMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.accMenuContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.accTopMenu = QFrame(self.accMenuContainer)
        self.accTopMenu.setObjectName(u"accTopMenu")
        self.accTopMenu.setMinimumSize(QSize(300, 0))
        self.accTopMenu.setFrameShape(QFrame.StyledPanel)
        self.accTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.accTopMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.accTopMenu)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.closeAccButton = QPushButton(self.accTopMenu)
        self.closeAccButton.setObjectName(u"closeAccButton")
        self.closeAccButton.setMinimumSize(QSize(28, 50))
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAccButton.setIcon(icon8)
        self.closeAccButton.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.closeAccButton, 0, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_8.addWidget(self.accTopMenu, 0, Qt.AlignTop)

        self.topFrame = QFrame(self.accMenuContainer)
        self.topFrame.setObjectName(u"topFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy)
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.topFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.loginForm = QStackedWidget(self.topFrame)
        self.loginForm.setObjectName(u"loginForm")
        self.loginFrame = QWidget()
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.loginFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.loginFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u":/icons/images/icons/icons8-change-user-50.png"))

        self.verticalLayout_11.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_3 = QLabel(self.loginFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_11.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.frame = QFrame(self.loginFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_12.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_12.addWidget(self.lineEdit_2)


        self.verticalLayout_11.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.loginButton = QPushButton(self.loginFrame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(170, 40))
        self.loginButton.setMaximumSize(QSize(150, 40))
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/icons8-\u0432\u043e\u0439\u0442\u0438-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loginButton.setIcon(icon9)
        self.loginButton.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.loginButton, 0, Qt.AlignHCenter)

        self.changeWindowLogButton = QPushButton(self.loginFrame)
        self.changeWindowLogButton.setObjectName(u"changeWindowLogButton")
        self.changeWindowLogButton.setMinimumSize(QSize(150, 50))
        self.changeWindowLogButton.setMaximumSize(QSize(150, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(True)
        self.changeWindowLogButton.setFont(font1)
        self.changeWindowLogButton.setIconSize(QSize(50, 50))

        self.verticalLayout_11.addWidget(self.changeWindowLogButton, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.loginForm.addWidget(self.loginFrame)
        self.registerFrame = QWidget()
        self.registerFrame.setObjectName(u"registerFrame")
        self.registerFrame.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.registerFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.registerFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 50))
        self.label_5.setPixmap(QPixmap(u":/icons/images/icons/icons8-registration-50.png"))

        self.verticalLayout_14.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.registerFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_14.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 99, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.frame_2 = QFrame(self.registerFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_13.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_13.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_13.addWidget(self.lineEdit_5)


        self.verticalLayout_14.addWidget(self.frame_2)

        self.verticalSpacer_6 = QSpacerItem(20, 102, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_6)

        self.registerButton = QPushButton(self.registerFrame)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(170, 40))
        self.registerButton.setMaximumSize(QSize(150, 40))
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/icons8-\u0433\u0430\u043b\u043e\u0447\u043a\u0430-\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u043d\u043e\u0433\u043e-\u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430-\u0438\u043d\u0441\u0442\u0430\u0433\u0440\u0430\u043c-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.registerButton.setIcon(icon10)
        self.registerButton.setIconSize(QSize(24, 24))

        self.verticalLayout_14.addWidget(self.registerButton, 0, Qt.AlignHCenter)

        self.changeWindowRegButton = QPushButton(self.registerFrame)
        self.changeWindowRegButton.setObjectName(u"changeWindowRegButton")
        self.changeWindowRegButton.setMinimumSize(QSize(100, 50))
        self.changeWindowRegButton.setMaximumSize(QSize(150, 50))
        self.changeWindowRegButton.setFont(font1)

        self.verticalLayout_14.addWidget(self.changeWindowRegButton, 0, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 99, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_7)

        self.loginForm.addWidget(self.registerFrame)

        self.verticalLayout_10.addWidget(self.loginForm)


        self.verticalLayout_8.addWidget(self.topFrame)


        self.horizontalLayout.addWidget(self.accMenuContainer)

        self.centralMenuContainer = QFrame(self.MainContainer)
        self.centralMenuContainer.setObjectName(u"centralMenuContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralMenuContainer.sizePolicy().hasHeightForWidth())
        self.centralMenuContainer.setSizePolicy(sizePolicy1)
        self.centralMenuContainer.setStyleSheet(u"border:none;")
        self.centralMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.centralMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.centralMenuContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.topCentralContainer = QFrame(self.centralMenuContainer)
        self.topCentralContainer.setObjectName(u"topCentralContainer")
        self.topCentralContainer.setFrameShape(QFrame.StyledPanel)
        self.topCentralContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topCentralContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toptop = QFrame(self.topCentralContainer)
        self.toptop.setObjectName(u"toptop")
        sizePolicy1.setHeightForWidth(self.toptop.sizePolicy().hasHeightForWidth())
        self.toptop.setSizePolicy(sizePolicy1)
        self.toptop.setFrameShape(QFrame.StyledPanel)
        self.toptop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.toptop)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.toptop)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.titleRightInfo)


        self.horizontalLayout_2.addWidget(self.toptop)

        self.rightButtons = QFrame(self.topCentralContainer)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setFrameShape(QFrame.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.minimizeButton = QPushButton(self.rightButtons)
        self.minimizeButton.setObjectName(u"minimizeButton")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon11)
        self.minimizeButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.rightButtons)
        self.restoreButton.setObjectName(u"restoreButton")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon12)
        self.restoreButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.rightButtons)
        self.closeButton.setObjectName(u"closeButton")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon13)
        self.closeButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_2.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.topCentralContainer, 0, Qt.AlignTop)

        self.contentBottom = QFrame(self.centralMenuContainer)
        self.contentBottom.setObjectName(u"contentBottom")
        sizePolicy.setHeightForWidth(self.contentBottom.sizePolicy().hasHeightForWidth())
        self.contentBottom.setSizePolicy(sizePolicy)
        self.contentBottom.setFrameShape(QFrame.StyledPanel)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.contentBottom)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(235, 235, 235);\n"
"border: none;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color: rgb(36, 149, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;\n"
"}\n"
"QTableWid"
                        "get::item:selected{\n"
"	background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(36, 149, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;}\n"
"\n"
"/*LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(245, 246, 250);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLin"
                        "eEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.linePage = QWidget()
        self.linePage.setObjectName(u"linePage")
        sizePolicy2.setHeightForWidth(self.linePage.sizePolicy().hasHeightForWidth())
        self.linePage.setSizePolicy(sizePolicy2)
        self.linePage.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.linePage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lineTabContainer = QFrame(self.linePage)
        self.lineTabContainer.setObjectName(u"lineTabContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineTabContainer.sizePolicy().hasHeightForWidth())
        self.lineTabContainer.setSizePolicy(sizePolicy3)
        self.lineTabContainer.setStyleSheet(u"#lineTabContainer{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color: rgb(36, 149, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;"
                        "\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(36, 149, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"")
        self.lineTabContainer.setFrameShape(QFrame.StyledPanel)
        self.lineTabContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.lineTabContainer)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 0, 9, -1)
        self.lineData_Tab = QTableWidget(self.lineTabContainer)
        if (self.lineData_Tab.columnCount() < 2):
            self.lineData_Tab.setColumnCount(2)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.lineData_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.lineData_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.lineData_Tab.setObjectName(u"lineData_Tab")
        self.lineData_Tab.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineData_Tab.sizePolicy().hasHeightForWidth())
        self.lineData_Tab.setSizePolicy(sizePolicy4)
        self.lineData_Tab.setMinimumSize(QSize(0, 0))
        self.lineData_Tab.setMaximumSize(QSize(16777215, 16777215))
        self.lineData_Tab.setFrameShape(QFrame.NoFrame)
        self.lineData_Tab.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lineData_Tab.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lineData_Tab.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.lineData_Tab.setAutoScroll(True)
        self.lineData_Tab.setAutoScrollMargin(16)
        self.lineData_Tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lineData_Tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.lineData_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lineData_Tab.setShowGrid(True)
        self.lineData_Tab.setGridStyle(Qt.SolidLine)
        self.lineData_Tab.setWordWrap(True)
        self.lineData_Tab.setCornerButtonEnabled(True)
        self.lineData_Tab.setRowCount(0)
        self.lineData_Tab.setColumnCount(2)
        self.lineData_Tab.horizontalHeader().setVisible(True)
        self.lineData_Tab.horizontalHeader().setCascadingSectionResizes(True)
        self.lineData_Tab.horizontalHeader().setMinimumSectionSize(150)
        self.lineData_Tab.horizontalHeader().setDefaultSectionSize(160)
        self.lineData_Tab.horizontalHeader().setHighlightSections(False)
        self.lineData_Tab.horizontalHeader().setStretchLastSection(False)
        self.lineData_Tab.verticalHeader().setVisible(False)
        self.lineData_Tab.verticalHeader().setMinimumSectionSize(50)
        self.lineData_Tab.verticalHeader().setHighlightSections(False)
        self.lineData_Tab.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_22.addWidget(self.lineData_Tab, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.refreshLineButton = QPushButton(self.lineTabContainer)
        self.refreshLineButton.setObjectName(u"refreshLineButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.refreshLineButton.sizePolicy().hasHeightForWidth())
        self.refreshLineButton.setSizePolicy(sizePolicy5)
        self.refreshLineButton.setMinimumSize(QSize(150, 0))
        self.refreshLineButton.setMaximumSize(QSize(250, 16777215))
        self.refreshLineButton.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshLineButton.setIcon(icon14)
        self.refreshLineButton.setIconSize(QSize(50, 50))

        self.verticalLayout_22.addWidget(self.refreshLineButton, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.lineTabContainer)

        self.lineStatusContainer = QFrame(self.linePage)
        self.lineStatusContainer.setObjectName(u"lineStatusContainer")
        sizePolicy3.setHeightForWidth(self.lineStatusContainer.sizePolicy().hasHeightForWidth())
        self.lineStatusContainer.setSizePolicy(sizePolicy3)
        self.lineStatusContainer.setMinimumSize(QSize(0, 0))
        self.lineStatusContainer.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#lineStatusContainer{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color: rgb(36, 149, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: "
                        "5px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(36, 149, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}")
        self.lineStatusContainer.setFrameShape(QFrame.StyledPanel)
        self.lineStatusContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.lineStatusContainer)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.frame_6 = QFrame(self.lineStatusContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.batchOnLine_Tab = QTableWidget(self.frame_6)
        if (self.batchOnLine_Tab.columnCount() < 5):
            self.batchOnLine_Tab.setColumnCount(5)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.batchOnLine_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.batchOnLine_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.batchOnLine_Tab.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.batchOnLine_Tab.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.batchOnLine_Tab.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        self.batchOnLine_Tab.setObjectName(u"batchOnLine_Tab")
        sizePolicy3.setHeightForWidth(self.batchOnLine_Tab.sizePolicy().hasHeightForWidth())
        self.batchOnLine_Tab.setSizePolicy(sizePolicy3)
        self.batchOnLine_Tab.setMinimumSize(QSize(0, 0))
        self.batchOnLine_Tab.setStyleSheet(u"QTableWidget::item:selected{\n"
"	background-color: rgb(217, 217, 217);\n"
"}")
        self.batchOnLine_Tab.setFrameShape(QFrame.NoFrame)
        self.batchOnLine_Tab.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.batchOnLine_Tab.setAutoScroll(True)
        self.batchOnLine_Tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.batchOnLine_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.batchOnLine_Tab.setRowCount(0)
        self.batchOnLine_Tab.horizontalHeader().setCascadingSectionResizes(True)
        self.batchOnLine_Tab.horizontalHeader().setMinimumSectionSize(100)
        self.batchOnLine_Tab.horizontalHeader().setDefaultSectionSize(200)
        self.batchOnLine_Tab.horizontalHeader().setHighlightSections(False)
        self.batchOnLine_Tab.horizontalHeader().setProperty("showSortIndicator", True)
        self.batchOnLine_Tab.horizontalHeader().setStretchLastSection(True)
        self.batchOnLine_Tab.verticalHeader().setVisible(False)
        self.batchOnLine_Tab.verticalHeader().setCascadingSectionResizes(False)
        self.batchOnLine_Tab.verticalHeader().setMinimumSectionSize(40)
        self.batchOnLine_Tab.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_18.addWidget(self.batchOnLine_Tab)


        self.verticalLayout_17.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.statusLine_frame = QFrame(self.lineStatusContainer)
        self.statusLine_frame.setObjectName(u"statusLine_frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.statusLine_frame.sizePolicy().hasHeightForWidth())
        self.statusLine_frame.setSizePolicy(sizePolicy6)
        self.statusLine_frame.setLayoutDirection(Qt.LeftToRight)
        self.statusLine_frame.setFrameShape(QFrame.StyledPanel)
        self.statusLine_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.statusLine_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.New_lineEdit = QLineEdit(self.statusLine_frame)
        self.New_lineEdit.setObjectName(u"New_lineEdit")
        self.New_lineEdit.setMinimumSize(QSize(0, 50))
        self.New_lineEdit.setMaximumSize(QSize(150, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.New_lineEdit.setFont(font4)
        self.New_lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.New_lineEdit.setStyleSheet(u"\n"
"font: 700 12pt \"Segoe UI\";")
        self.New_lineEdit.setAlignment(Qt.AlignCenter)
        self.New_lineEdit.setDragEnabled(True)
        self.New_lineEdit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.New_lineEdit)

        self.Work_lineEdit = QLineEdit(self.statusLine_frame)
        self.Work_lineEdit.setObjectName(u"Work_lineEdit")
        self.Work_lineEdit.setMinimumSize(QSize(0, 50))
        self.Work_lineEdit.setMaximumSize(QSize(150, 16777215))
        self.Work_lineEdit.setStyleSheet(u"\n"
"font: 700 12pt \"Segoe UI\";")
        self.Work_lineEdit.setAlignment(Qt.AlignCenter)
        self.Work_lineEdit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.Work_lineEdit)

        self.End_lineEdit = QLineEdit(self.statusLine_frame)
        self.End_lineEdit.setObjectName(u"End_lineEdit")
        self.End_lineEdit.setMinimumSize(QSize(0, 50))
        self.End_lineEdit.setMaximumSize(QSize(150, 16777215))
        self.End_lineEdit.setStyleSheet(u"\n"
"\n"
"font: 700 12pt \"Segoe UI\";")
        self.End_lineEdit.setAlignment(Qt.AlignCenter)
        self.End_lineEdit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.End_lineEdit)


        self.verticalLayout_17.addWidget(self.statusLine_frame)

        self.frame_11 = QFrame(self.lineStatusContainer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 60))
        self.frame_11.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(119, 119, 119);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.deleteOrderButton = QPushButton(self.frame_11)
        self.deleteOrderButton.setObjectName(u"deleteOrderButton")
        self.deleteOrderButton.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.deleteOrderButton.sizePolicy().hasHeightForWidth())
        self.deleteOrderButton.setSizePolicy(sizePolicy2)
        self.deleteOrderButton.setMinimumSize(QSize(150, 40))
        self.deleteOrderButton.setMaximumSize(QSize(150, 40))
        self.deleteOrderButton.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"color: rgb(193, 193, 193);\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-ban.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteOrderButton.setIcon(icon15)
        self.deleteOrderButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.deleteOrderButton)

        self.closeOrderButton = QPushButton(self.frame_11)
        self.closeOrderButton.setObjectName(u"closeOrderButton")
        self.closeOrderButton.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.closeOrderButton.sizePolicy().hasHeightForWidth())
        self.closeOrderButton.setSizePolicy(sizePolicy2)
        self.closeOrderButton.setMinimumSize(QSize(150, 40))
        self.closeOrderButton.setMaximumSize(QSize(150, 40))
        self.closeOrderButton.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"	\n"
"	color: rgb(193, 193, 193);\n"
"}\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeOrderButton.setIcon(icon16)
        self.closeOrderButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.closeOrderButton)


        self.verticalLayout_17.addWidget(self.frame_11, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.lineStatusContainer)

        self.stackedWidget.addWidget(self.linePage)
        self.rollPage = QWidget()
        self.rollPage.setObjectName(u"rollPage")
        self.verticalLayout_78 = QVBoxLayout(self.rollPage)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.addLine_Frame_2 = QFrame(self.rollPage)
        self.addLine_Frame_2.setObjectName(u"addLine_Frame_2")
        sizePolicy1.setHeightForWidth(self.addLine_Frame_2.sizePolicy().hasHeightForWidth())
        self.addLine_Frame_2.setSizePolicy(sizePolicy1)
        self.addLine_Frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(66, 66, 66);\n"
"	selection-color: rgb(255, 0, 255);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color:"
                        " rgb(36, 149, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(36, 149, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}")
        self.addLine_Frame_2.setFrameShape(QFrame.StyledPanel)
        self.addLine_Frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.addLine_Frame_2)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.frame_64 = QFrame(self.addLine_Frame_2)
        self.frame_64.setObjectName(u"frame_64")
        sizePolicy6.setHeightForWidth(self.frame_64.sizePolicy().hasHeightForWidth())
        self.frame_64.setSizePolicy(sizePolicy6)
        self.frame_64.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_64)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_15 = QLabel(self.frame_64)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_71.addWidget(self.label_15, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_70.addWidget(self.frame_64)

        self.frame_74 = QFrame(self.addLine_Frame_2)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.rollCode_edit = QLineEdit(self.frame_74)
        self.rollCode_edit.setObjectName(u"rollCode_edit")
        self.rollCode_edit.setMinimumSize(QSize(0, 30))
        self.rollCode_edit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(245, 246, 250);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(66, 66, 66);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"	color: rgb(66, 66, 66);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_49.addWidget(self.rollCode_edit)

        self.rollButton = QPushButton(self.frame_74)
        self.rollButton.setObjectName(u"rollButton")
        self.rollButton.setMinimumSize(QSize(200, 45))

        self.horizontalLayout_49.addWidget(self.rollButton)


        self.verticalLayout_70.addWidget(self.frame_74)

        self.frame_65 = QFrame(self.addLine_Frame_2)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_65)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, -1, 0, -1)
        self.listLineContainer_2 = QFrame(self.frame_65)
        self.listLineContainer_2.setObjectName(u"listLineContainer_2")
        self.listLineContainer_2.setFrameShape(QFrame.StyledPanel)
        self.listLineContainer_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.listLineContainer_2)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.rollTable = QTableWidget(self.listLineContainer_2)
        if (self.rollTable.columnCount() < 4):
            self.rollTable.setColumnCount(4)
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.rollTable.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.rollTable.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.rollTable.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        self.rollTable.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.rollTable.setObjectName(u"rollTable")
        self.rollTable.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.rollTable.sizePolicy().hasHeightForWidth())
        self.rollTable.setSizePolicy(sizePolicy4)
        self.rollTable.setMinimumSize(QSize(0, 0))
        self.rollTable.setMaximumSize(QSize(16777215, 16777215))
        self.rollTable.setFrameShape(QFrame.NoFrame)
        self.rollTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.rollTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rollTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.rollTable.setAutoScroll(True)
        self.rollTable.setAutoScrollMargin(16)
        self.rollTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.rollTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.rollTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.rollTable.setShowGrid(True)
        self.rollTable.setGridStyle(Qt.SolidLine)
        self.rollTable.setWordWrap(True)
        self.rollTable.setCornerButtonEnabled(True)
        self.rollTable.setRowCount(0)
        self.rollTable.setColumnCount(4)
        self.rollTable.horizontalHeader().setVisible(True)
        self.rollTable.horizontalHeader().setCascadingSectionResizes(True)
        self.rollTable.horizontalHeader().setMinimumSectionSize(0)
        self.rollTable.horizontalHeader().setDefaultSectionSize(160)
        self.rollTable.horizontalHeader().setHighlightSections(False)
        self.rollTable.horizontalHeader().setStretchLastSection(False)
        self.rollTable.verticalHeader().setVisible(False)
        self.rollTable.verticalHeader().setMinimumSectionSize(25)
        self.rollTable.verticalHeader().setDefaultSectionSize(30)
        self.rollTable.verticalHeader().setHighlightSections(False)
        self.rollTable.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_42.addWidget(self.rollTable)

        self.listAction = QPlainTextEdit(self.listLineContainer_2)
        self.listAction.setObjectName(u"listAction")
        self.listAction.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(66, 66, 66);\n"
"font: 14pt \"Segoe UI\";\n"
"padding-left: 10px")
        self.listAction.setReadOnly(True)

        self.horizontalLayout_42.addWidget(self.listAction)


        self.verticalLayout_72.addWidget(self.listLineContainer_2)


        self.verticalLayout_70.addWidget(self.frame_65)


        self.verticalLayout_78.addWidget(self.addLine_Frame_2)

        self.stackedWidget.addWidget(self.rollPage)
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.verticalLayout_41 = QVBoxLayout(self.startPage)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_20 = QFrame(self.startPage)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	font: 18pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 20px;	\n"
"\n"
"\n"
"}\n"
"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_20)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_27 = QFrame(self.frame_20)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 24pt \"Segoe UI\";")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_27)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_8 = QLabel(self.frame_27)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_47.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.verticalLayout_48.addWidget(self.frame_27)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_23)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_23)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy7)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_19.setSpacing(18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.startCreateButton = QPushButton(self.frame_21)
        self.startCreateButton.setObjectName(u"startCreateButton")
        self.startCreateButton.setMinimumSize(QSize(200, 150))
        self.startCreateButton.setMaximumSize(QSize(200, 150))
        self.startCreateButton.setIcon(icon10)
        self.startCreateButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_19.addWidget(self.startCreateButton)

        self.startOrdersButton = QPushButton(self.frame_21)
        self.startOrdersButton.setObjectName(u"startOrdersButton")
        self.startOrdersButton.setMinimumSize(QSize(200, 150))
        self.startOrdersButton.setMaximumSize(QSize(200, 150))
        self.startOrdersButton.setIcon(icon2)
        self.startOrdersButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_19.addWidget(self.startOrdersButton)


        self.verticalLayout_42.addWidget(self.frame_21, 0, Qt.AlignLeft)

        self.frame_22 = QFrame(self.frame_23)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy8)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_21.setSpacing(18)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.startLineButton = QPushButton(self.frame_22)
        self.startLineButton.setObjectName(u"startLineButton")
        self.startLineButton.setMinimumSize(QSize(200, 150))
        self.startLineButton.setMaximumSize(QSize(200, 150))
        self.startLineButton.setIcon(icon3)
        self.startLineButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_21.addWidget(self.startLineButton)

        self.startSearchButton = QPushButton(self.frame_22)
        self.startSearchButton.setObjectName(u"startSearchButton")
        self.startSearchButton.setMinimumSize(QSize(200, 150))
        self.startSearchButton.setMaximumSize(QSize(200, 150))
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/icons8-\u043f\u043e\u0438\u0441\u043a-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startSearchButton.setIcon(icon17)
        self.startSearchButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_21.addWidget(self.startSearchButton)


        self.verticalLayout_42.addWidget(self.frame_22)


        self.verticalLayout_48.addWidget(self.frame_23, 0, Qt.AlignHCenter)


        self.verticalLayout_41.addWidget(self.frame_20, 0, Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.startPage)
        self.ordersPage = QWidget()
        self.ordersPage.setObjectName(u"ordersPage")
        self.ordersPage.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.ordersPage)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.ordersPage)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setMinimumSize(QSize(1189, 777))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.activOrderList = QFrame(self.frame_8)
        self.activOrderList.setObjectName(u"activOrderList")
        sizePolicy8.setHeightForWidth(self.activOrderList.sizePolicy().hasHeightForWidth())
        self.activOrderList.setSizePolicy(sizePolicy8)
        self.activOrderList.setMinimumSize(QSize(600, 0))
        self.activOrderList.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#activOrderList {\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color: rgb(36, 149, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 5px;"
                        "\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(36, 149, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}/*\n"
"QHeaderView::section:vertical {\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}*/")
        self.activOrderList.setFrameShape(QFrame.StyledPanel)
        self.activOrderList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.activOrderList)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.serchLineEdit = QLineEdit(self.activOrderList)
        self.serchLineEdit.setObjectName(u"serchLineEdit")
        self.serchLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(245, 246, 250);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(66, 66, 66);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"	color: rgb(66, 66, 66);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_20.addWidget(self.serchLineEdit)

        self.activOrder_Tab = QTableWidget(self.activOrderList)
        if (self.activOrder_Tab.columnCount() < 4):
            self.activOrder_Tab.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font5);
        self.activOrder_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.activOrder_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.activOrder_Tab.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.activOrder_Tab.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.activOrder_Tab.setObjectName(u"activOrder_Tab")
        sizePolicy4.setHeightForWidth(self.activOrder_Tab.sizePolicy().hasHeightForWidth())
        self.activOrder_Tab.setSizePolicy(sizePolicy4)
        self.activOrder_Tab.setMinimumSize(QSize(580, 0))
        self.activOrder_Tab.setStyleSheet(u"QTableWidget::item:selected{\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}")
        self.activOrder_Tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.activOrder_Tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.activOrder_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.activOrder_Tab.setTextElideMode(Qt.ElideLeft)
        self.activOrder_Tab.setSortingEnabled(False)
        self.activOrder_Tab.setRowCount(0)
        self.activOrder_Tab.horizontalHeader().setHighlightSections(True)
        self.activOrder_Tab.horizontalHeader().setProperty("showSortIndicator", False)
        self.activOrder_Tab.verticalHeader().setVisible(False)
        self.activOrder_Tab.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_20.addWidget(self.activOrder_Tab)

        self.frame_87 = QFrame(self.activOrderList)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(0, 50))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.refreshBatch_button = QPushButton(self.frame_87)
        self.refreshBatch_button.setObjectName(u"refreshBatch_button")
        sizePolicy6.setHeightForWidth(self.refreshBatch_button.sizePolicy().hasHeightForWidth())
        self.refreshBatch_button.setSizePolicy(sizePolicy6)
        self.refreshBatch_button.setMinimumSize(QSize(200, 50))
        self.refreshBatch_button.setMaximumSize(QSize(200, 16777215))
        self.refreshBatch_button.setStyleSheet(u"")

        self.horizontalLayout_53.addWidget(self.refreshBatch_button, 0, Qt.AlignLeft)

        self.selectLoadBatchMode_frame = QFrame(self.frame_87)
        self.selectLoadBatchMode_frame.setObjectName(u"selectLoadBatchMode_frame")
        self.selectLoadBatchMode_frame.setStyleSheet(u"")
        self.selectLoadBatchMode_frame.setFrameShape(QFrame.StyledPanel)
        self.selectLoadBatchMode_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.selectLoadBatchMode_frame)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.printHouse_checkBox = QCheckBox(self.selectLoadBatchMode_frame)
        self.printHouse_checkBox.setObjectName(u"printHouse_checkBox")
        self.printHouse_checkBox.setEnabled(True)
        self.printHouse_checkBox.setChecked(True)
        self.printHouse_checkBox.setTristate(False)

        self.verticalLayout_89.addWidget(self.printHouse_checkBox)

        self.mabufacture_checkBox = QCheckBox(self.selectLoadBatchMode_frame)
        self.mabufacture_checkBox.setObjectName(u"mabufacture_checkBox")
        self.mabufacture_checkBox.setChecked(True)

        self.verticalLayout_89.addWidget(self.mabufacture_checkBox)


        self.horizontalLayout_53.addWidget(self.selectLoadBatchMode_frame, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_87)


        self.horizontalLayout_6.addWidget(self.activOrderList)

        self.orderFrame = QFrame(self.frame_8)
        self.orderFrame.setObjectName(u"orderFrame")
        sizePolicy1.setHeightForWidth(self.orderFrame.sizePolicy().hasHeightForWidth())
        self.orderFrame.setSizePolicy(sizePolicy1)
        self.orderFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#orderFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 20px;	\n"
"}\n"
"\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color: rgb(36, 149, 255);\n"
"	padding-left: 15px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(255, 255, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHe"
                        "ader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}/*\n"
"QHeaderView::section:vertical {\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}*/\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(255, 255, 255);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(36, 149, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-rad"
                        "ius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(255, 255, 255);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(36, 149, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height:"
                        " 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.orderFrame.setFrameShape(QFrame.StyledPanel)
        self.orderFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.orderFrame)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.frame_9 = QFrame(self.orderFrame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_9)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.batchData_Tab = QTableWidget(self.frame_9)
        if (self.batchData_Tab.columnCount() < 10):
            self.batchData_Tab.setColumnCount(10)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font5);
        self.batchData_Tab.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        if (self.batchData_Tab.rowCount() < 1):
            self.batchData_Tab.setRowCount(1)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab.setItem(0, 0, __qtablewidgetitem25)
        font6 = QFont()
        font6.setPointSize(10)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFont(font6);
        self.batchData_Tab.setItem(0, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab.setItem(0, 2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab.setItem(0, 3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab.setItem(0, 4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab.setItem(0, 5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab.setItem(0, 6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font6);
        self.batchData_Tab.setItem(0, 7, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab.setItem(0, 8, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab.setItem(0, 9, __qtablewidgetitem34)
        self.batchData_Tab.setObjectName(u"batchData_Tab")
        sizePolicy1.setHeightForWidth(self.batchData_Tab.sizePolicy().hasHeightForWidth())
        self.batchData_Tab.setSizePolicy(sizePolicy1)
        self.batchData_Tab.setMaximumSize(QSize(16777215, 100))
        self.batchData_Tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.batchData_Tab.setSelectionMode(QAbstractItemView.NoSelection)
        self.batchData_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.batchData_Tab.setShowGrid(True)
        self.batchData_Tab.setSortingEnabled(False)
        self.batchData_Tab.setRowCount(1)
        self.batchData_Tab.setColumnCount(10)
        self.batchData_Tab.horizontalHeader().setVisible(True)
        self.batchData_Tab.horizontalHeader().setCascadingSectionResizes(False)
        self.batchData_Tab.horizontalHeader().setMinimumSectionSize(50)
        self.batchData_Tab.horizontalHeader().setDefaultSectionSize(130)
        self.batchData_Tab.horizontalHeader().setHighlightSections(False)
        self.batchData_Tab.horizontalHeader().setStretchLastSection(True)
        self.batchData_Tab.verticalHeader().setVisible(False)
        self.batchData_Tab.verticalHeader().setMinimumSectionSize(35)
        self.batchData_Tab.verticalHeader().setDefaultSectionSize(35)
        self.batchData_Tab.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_26.addWidget(self.batchData_Tab)


        self.verticalLayout_21.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.orderFrame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.closeBatch_btn = QPushButton(self.frame_15)
        self.closeBatch_btn.setObjectName(u"closeBatch_btn")
        self.closeBatch_btn.setEnabled(False)
        self.closeBatch_btn.setMinimumSize(QSize(0, 50))
        self.closeBatch_btn.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.closeBatch_btn)

        self.deleteBatch_btn = QPushButton(self.frame_15)
        self.deleteBatch_btn.setObjectName(u"deleteBatch_btn")
        self.deleteBatch_btn.setEnabled(False)
        self.deleteBatch_btn.setMinimumSize(QSize(0, 50))
        self.deleteBatch_btn.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.deleteBatch_btn)

        self.showKM_btn = QPushButton(self.frame_15)
        self.showKM_btn.setObjectName(u"showKM_btn")
        self.showKM_btn.setEnabled(False)
        self.showKM_btn.setMinimumSize(QSize(0, 50))
        self.showKM_btn.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.showKM_btn)

        self.showKITU = QPushButton(self.frame_15)
        self.showKITU.setObjectName(u"showKITU")
        self.showKITU.setEnabled(False)
        self.showKITU.setMinimumSize(QSize(0, 50))
        self.showKITU.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.showKITU)

        self.sendBatchOnLine_btn = QPushButton(self.frame_15)
        self.sendBatchOnLine_btn.setObjectName(u"sendBatchOnLine_btn")
        self.sendBatchOnLine_btn.setEnabled(False)
        self.sendBatchOnLine_btn.setMinimumSize(QSize(0, 50))
        self.sendBatchOnLine_btn.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.sendBatchOnLine_btn)

        self.exportBatch_btn = QPushButton(self.frame_15)
        self.exportBatch_btn.setObjectName(u"exportBatch_btn")
        self.exportBatch_btn.setEnabled(False)
        self.exportBatch_btn.setMinimumSize(QSize(0, 50))
        self.exportBatch_btn.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.exportBatch_btn)

        self.printButton = QPushButton(self.frame_15)
        self.printButton.setObjectName(u"printButton")
        self.printButton.setEnabled(False)
        self.printButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_10.addWidget(self.printButton)


        self.verticalLayout_27.addWidget(self.frame_15, 0, Qt.AlignTop)

        self.KITUContainer = QFrame(self.frame_10)
        self.KITUContainer.setObjectName(u"KITUContainer")
        sizePolicy3.setHeightForWidth(self.KITUContainer.sizePolicy().hasHeightForWidth())
        self.KITUContainer.setSizePolicy(sizePolicy3)
        self.KITUContainer.setMinimumSize(QSize(0, 0))
        self.KITUContainer.setMaximumSize(QSize(16777215, 0))
        self.KITUContainer.setStyleSheet(u"#KITUContainer {\n"
"	border: 1px solid;\n"
"	border-color: rgb(36, 149, 255);\n"
"	border-radius: 20px;\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-color: qradialgradient(spread:pad, cx:0.619, cy:0.341, radius:0.5, fx:0.909091, fy:0.085, stop:0.346591 rgba(36, 149, 255, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.494318 rgba(36, 149, 255, 80), stop:0.6875 rgba(36, 149, 255, 156), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"")
        self.KITUContainer.setFrameShape(QFrame.StyledPanel)
        self.KITUContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.KITUContainer)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.frame_105 = QFrame(self.KITUContainer)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.KITUsendPrint_button = QPushButton(self.frame_105)
        self.KITUsendPrint_button.setObjectName(u"KITUsendPrint_button")
        sizePolicy6.setHeightForWidth(self.KITUsendPrint_button.sizePolicy().hasHeightForWidth())
        self.KITUsendPrint_button.setSizePolicy(sizePolicy6)
        self.KITUsendPrint_button.setMinimumSize(QSize(200, 50))
        self.KITUsendPrint_button.setMaximumSize(QSize(200, 16777215))
        self.KITUsendPrint_button.setStyleSheet(u"")

        self.horizontalLayout_59.addWidget(self.KITUsendPrint_button)


        self.verticalLayout_104.addWidget(self.frame_105, 0, Qt.AlignLeft)

        self.frame_104 = QFrame(self.KITUContainer)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.orderKITU_tab = QTableWidget(self.frame_104)
        if (self.orderKITU_tab.columnCount() < 3):
            self.orderKITU_tab.setColumnCount(3)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font5);
        self.orderKITU_tab.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font5);
        self.orderKITU_tab.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font5);
        self.orderKITU_tab.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        self.orderKITU_tab.setObjectName(u"orderKITU_tab")
        self.orderKITU_tab.setMinimumSize(QSize(550, 0))
        self.orderKITU_tab.setMaximumSize(QSize(16777215, 16777215))
        self.orderKITU_tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.orderKITU_tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.orderKITU_tab.horizontalHeader().setDefaultSectionSize(130)
        self.orderKITU_tab.horizontalHeader().setStretchLastSection(False)
        self.orderKITU_tab.verticalHeader().setVisible(False)

        self.horizontalLayout_22.addWidget(self.orderKITU_tab)

        self.KI_from_KITU_Container = QFrame(self.frame_104)
        self.KI_from_KITU_Container.setObjectName(u"KI_from_KITU_Container")
        sizePolicy1.setHeightForWidth(self.KI_from_KITU_Container.sizePolicy().hasHeightForWidth())
        self.KI_from_KITU_Container.setSizePolicy(sizePolicy1)
        self.KI_from_KITU_Container.setMinimumSize(QSize(0, 0))
        self.KI_from_KITU_Container.setMaximumSize(QSize(0, 16777215))
        self.KI_from_KITU_Container.setStyleSheet(u"")
        self.KI_from_KITU_Container.setFrameShape(QFrame.StyledPanel)
        self.KI_from_KITU_Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.KI_from_KITU_Container)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.ki_from_KITU_tab = QTableWidget(self.KI_from_KITU_Container)
        if (self.ki_from_KITU_tab.columnCount() < 3):
            self.ki_from_KITU_tab.setColumnCount(3)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font5);
        self.ki_from_KITU_tab.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font5);
        self.ki_from_KITU_tab.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font5);
        self.ki_from_KITU_tab.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        self.ki_from_KITU_tab.setObjectName(u"ki_from_KITU_tab")
        self.ki_from_KITU_tab.setMaximumSize(QSize(600, 16777215))
        self.ki_from_KITU_tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ki_from_KITU_tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ki_from_KITU_tab.horizontalHeader().setDefaultSectionSize(130)
        self.ki_from_KITU_tab.horizontalHeader().setStretchLastSection(False)
        self.ki_from_KITU_tab.verticalHeader().setVisible(False)

        self.verticalLayout_29.addWidget(self.ki_from_KITU_tab)


        self.horizontalLayout_22.addWidget(self.KI_from_KITU_Container)

        self.horizontalSpacer = QSpacerItem(139, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer)


        self.verticalLayout_104.addWidget(self.frame_104)


        self.verticalLayout_27.addWidget(self.KITUContainer)

        self.sendLineContainer = QFrame(self.frame_10)
        self.sendLineContainer.setObjectName(u"sendLineContainer")
        sizePolicy.setHeightForWidth(self.sendLineContainer.sizePolicy().hasHeightForWidth())
        self.sendLineContainer.setSizePolicy(sizePolicy)
        self.sendLineContainer.setMinimumSize(QSize(0, 0))
        self.sendLineContainer.setMaximumSize(QSize(16777215, 0))
        self.sendLineContainer.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.sendLineContainer.setFrameShape(QFrame.StyledPanel)
        self.sendLineContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.sendLineContainer)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.sendLine_tab = QTableWidget(self.sendLineContainer)
        if (self.sendLine_tab.columnCount() < 3):
            self.sendLine_tab.setColumnCount(3)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font5);
        self.sendLine_tab.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font5);
        self.sendLine_tab.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font5);
        self.sendLine_tab.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        self.sendLine_tab.setObjectName(u"sendLine_tab")
        sizePolicy3.setHeightForWidth(self.sendLine_tab.sizePolicy().hasHeightForWidth())
        self.sendLine_tab.setSizePolicy(sizePolicy3)
        self.sendLine_tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sendLine_tab.verticalHeader().setVisible(False)

        self.horizontalLayout_11.addWidget(self.sendLine_tab)

        self.frame_17 = QFrame(self.sendLineContainer)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_17)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.sendOrder_btn = QPushButton(self.frame_17)
        self.sendOrder_btn.setObjectName(u"sendOrder_btn")
        self.sendOrder_btn.setEnabled(False)
        self.sendOrder_btn.setMinimumSize(QSize(200, 50))
        self.sendOrder_btn.setStyleSheet(u"QPushButton {	\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	\n"
"	background-color: rgb(119, 119, 119);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_28.addWidget(self.sendOrder_btn)

        self.canselOrder_btn = QPushButton(self.frame_17)
        self.canselOrder_btn.setObjectName(u"canselOrder_btn")
        self.canselOrder_btn.setMinimumSize(QSize(200, 50))

        self.verticalLayout_28.addWidget(self.canselOrder_btn)


        self.horizontalLayout_11.addWidget(self.frame_17, 0, Qt.AlignTop)


        self.verticalLayout_27.addWidget(self.sendLineContainer)

        self.codeContainer = QFrame(self.frame_10)
        self.codeContainer.setObjectName(u"codeContainer")
        sizePolicy.setHeightForWidth(self.codeContainer.sizePolicy().hasHeightForWidth())
        self.codeContainer.setSizePolicy(sizePolicy)
        self.codeContainer.setMinimumSize(QSize(0, 0))
        self.codeContainer.setMaximumSize(QSize(16777215, 0))
        self.codeContainer.setStyleSheet(u"")
        self.codeContainer.setFrameShape(QFrame.StyledPanel)
        self.codeContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.codeContainer)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.orderKM_tab = QTableWidget(self.codeContainer)
        if (self.orderKM_tab.columnCount() < 8):
            self.orderKM_tab.setColumnCount(8)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFont(font5);
        self.orderKM_tab.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font5);
        self.orderKM_tab.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font5);
        self.orderKM_tab.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFont(font5);
        self.orderKM_tab.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font5);
        self.orderKM_tab.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFont(font5);
        self.orderKM_tab.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFont(font5);
        self.orderKM_tab.setHorizontalHeaderItem(6, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font5);
        self.orderKM_tab.setHorizontalHeaderItem(7, __qtablewidgetitem51)
        self.orderKM_tab.setObjectName(u"orderKM_tab")
        self.orderKM_tab.setMaximumSize(QSize(16777215, 16777215))
        self.orderKM_tab.setStyleSheet(u"QTableWidget::item:selected{\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}")
        self.orderKM_tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.orderKM_tab.horizontalHeader().setDefaultSectionSize(130)
        self.orderKM_tab.horizontalHeader().setStretchLastSection(False)
        self.orderKM_tab.verticalHeader().setVisible(False)

        self.verticalLayout_25.addWidget(self.orderKM_tab)


        self.verticalLayout_27.addWidget(self.codeContainer)


        self.verticalLayout_21.addWidget(self.frame_10)


        self.horizontalLayout_6.addWidget(self.orderFrame)


        self.verticalLayout_19.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.ordersPage)
        self.createOrderPage = QWidget()
        self.createOrderPage.setObjectName(u"createOrderPage")
        self.verticalLayout_92 = QVBoxLayout(self.createOrderPage)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.createFrame = QFrame(self.createOrderPage)
        self.createFrame.setObjectName(u"createFrame")
        sizePolicy2.setHeightForWidth(self.createFrame.sizePolicy().hasHeightForWidth())
        self.createFrame.setSizePolicy(sizePolicy2)
        self.createFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(245, 246, 250);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(36, 149, 255);\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rg"
                        "b(245, 246, 250);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(36, 149, 255);\n"
"}")
        self.createFrame.setFrameShape(QFrame.StyledPanel)
        self.createFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.createFrame)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.frame_89 = QFrame(self.createFrame)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_89)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(10, 0, 0, 0)
        self.label_16 = QLabel(self.frame_89)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_91.addWidget(self.label_16, 0, Qt.AlignTop)


        self.verticalLayout_90.addWidget(self.frame_89, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_90 = QFrame(self.createFrame)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_90)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.frame_92 = QFrame(self.frame_90)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(0, 50))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.numCreatedOrder_edit = QLineEdit(self.frame_92)
        self.numCreatedOrder_edit.setObjectName(u"numCreatedOrder_edit")
        self.numCreatedOrder_edit.setMinimumSize(QSize(0, 30))
        self.numCreatedOrder_edit.setMaximumSize(QSize(300, 16777215))
        self.numCreatedOrder_edit.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(66, 66, 66);")

        self.horizontalLayout_54.addWidget(self.numCreatedOrder_edit)

        self.comboBox = QComboBox(self.frame_92)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 0))
        self.comboBox.setMaximumSize(QSize(16777215, 30))
        self.comboBox.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.comboBox.setMaxVisibleItems(20)

        self.horizontalLayout_54.addWidget(self.comboBox)

        self.createOrderBtn = QPushButton(self.frame_92)
        self.createOrderBtn.setObjectName(u"createOrderBtn")
        self.createOrderBtn.setEnabled(False)
        self.createOrderBtn.setMinimumSize(QSize(150, 40))
        self.createOrderBtn.setMaximumSize(QSize(150, 16777215))
        self.createOrderBtn.setStyleSheet(u"background-color: rgb(119, 119, 119);")

        self.horizontalLayout_54.addWidget(self.createOrderBtn)


        self.verticalLayout_93.addWidget(self.frame_92)


        self.verticalLayout_90.addWidget(self.frame_90)


        self.verticalLayout_92.addWidget(self.createFrame, 0, Qt.AlignTop)

        self.frame_91 = QFrame(self.createOrderPage)
        self.frame_91.setObjectName(u"frame_91")
        sizePolicy.setHeightForWidth(self.frame_91.sizePolicy().hasHeightForWidth())
        self.frame_91.setSizePolicy(sizePolicy)
        self.frame_91.setMinimumSize(QSize(0, 300))
        self.frame_91.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_91)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.frame_93 = QFrame(self.frame_91)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_93)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(10, 0, 0, 0)
        self.label_17 = QLabel(self.frame_93)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_94.addWidget(self.label_17, 0, Qt.AlignTop)


        self.verticalLayout_95.addWidget(self.frame_93)

        self.lastOrder_Tab = QTableWidget(self.frame_91)
        if (self.lastOrder_Tab.columnCount() < 5):
            self.lastOrder_Tab.setColumnCount(5)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFont(font5);
        self.lastOrder_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFont(font5);
        self.lastOrder_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font5);
        self.lastOrder_Tab.setHorizontalHeaderItem(2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setFont(font5);
        self.lastOrder_Tab.setHorizontalHeaderItem(3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setFont(font5);
        self.lastOrder_Tab.setHorizontalHeaderItem(4, __qtablewidgetitem56)
        self.lastOrder_Tab.setObjectName(u"lastOrder_Tab")
        sizePolicy3.setHeightForWidth(self.lastOrder_Tab.sizePolicy().hasHeightForWidth())
        self.lastOrder_Tab.setSizePolicy(sizePolicy3)
        self.lastOrder_Tab.setMinimumSize(QSize(0, 0))
        self.lastOrder_Tab.setStyleSheet(u"QTableWidget::item:selected{\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}")
        self.lastOrder_Tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lastOrder_Tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.lastOrder_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lastOrder_Tab.setTextElideMode(Qt.ElideLeft)
        self.lastOrder_Tab.setSortingEnabled(False)
        self.lastOrder_Tab.setRowCount(0)
        self.lastOrder_Tab.horizontalHeader().setHighlightSections(True)
        self.lastOrder_Tab.horizontalHeader().setProperty("showSortIndicator", False)
        self.lastOrder_Tab.verticalHeader().setVisible(False)
        self.lastOrder_Tab.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_95.addWidget(self.lastOrder_Tab)


        self.verticalLayout_92.addWidget(self.frame_91)

        self.stackedWidget.addWidget(self.createOrderPage)
        self.printPage = QWidget()
        self.printPage.setObjectName(u"printPage")
        self.verticalLayout_49 = QVBoxLayout(self.printPage)
        self.verticalLayout_49.setSpacing(10)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.printPage)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-radius: 20px;	\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color: rgb(36, 149, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;\n"
"}\n"
"QT"
                        "ableWidget::item:selected{\n"
"	background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(36, 149, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(245, 246, 250);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(66, 66, 66);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"	color: rgb(66, 66"
                        ", 66);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(600, 16777215))
        self.frame_31.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_31)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(9, -1, 9, -1)
        self.frame_41 = QFrame(self.frame_31)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(119, 119, 119);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_41)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.startPrint_btn = QPushButton(self.frame_41)
        self.startPrint_btn.setObjectName(u"startPrint_btn")
        self.startPrint_btn.setEnabled(False)
        self.startPrint_btn.setMinimumSize(QSize(40, 40))
        self.startPrint_btn.setMaximumSize(QSize(200, 16777215))
        self.startPrint_btn.setStyleSheet(u"")

        self.verticalLayout_63.addWidget(self.startPrint_btn)

        self.frame_45 = QFrame(self.frame_41)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.allPrint_rbtn = QRadioButton(self.frame_45)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.allPrint_rbtn)
        self.allPrint_rbtn.setObjectName(u"allPrint_rbtn")
        self.allPrint_rbtn.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";")

        self.horizontalLayout_36.addWidget(self.allPrint_rbtn)


        self.verticalLayout_63.addWidget(self.frame_45)

        self.frame_44 = QFrame(self.frame_41)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.countPrint_rbtn = QRadioButton(self.frame_44)
        self.buttonGroup.addButton(self.countPrint_rbtn)
        self.countPrint_rbtn.setObjectName(u"countPrint_rbtn")
        self.countPrint_rbtn.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";")

        self.horizontalLayout_35.addWidget(self.countPrint_rbtn)

        self.countPrint_line = QLineEdit(self.frame_44)
        self.countPrint_line.setObjectName(u"countPrint_line")
        self.countPrint_line.setEnabled(False)

        self.horizontalLayout_35.addWidget(self.countPrint_line)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_3)


        self.verticalLayout_63.addWidget(self.frame_44)

        self.frame_46 = QFrame(self.frame_41)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 0, -1, 0)
        self.save_rbtn = QRadioButton(self.frame_46)
        self.buttonGroup.addButton(self.save_rbtn)
        self.save_rbtn.setObjectName(u"save_rbtn")
        self.save_rbtn.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";")

        self.horizontalLayout_37.addWidget(self.save_rbtn)

        self.saveCodeInFile_btn = QPushButton(self.frame_46)
        self.saveCodeInFile_btn.setObjectName(u"saveCodeInFile_btn")
        self.saveCodeInFile_btn.setEnabled(False)
        self.saveCodeInFile_btn.setMinimumSize(QSize(200, 40))
        self.saveCodeInFile_btn.setMaximumSize(QSize(600, 16777215))
        self.saveCodeInFile_btn.setStyleSheet(u"background-color: rgb(119, 119, 119);")

        self.horizontalLayout_37.addWidget(self.saveCodeInFile_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_4)


        self.verticalLayout_63.addWidget(self.frame_46)


        self.verticalLayout_50.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_31)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_42)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, -1)
        self.kmPrint_tab = QTableWidget(self.frame_42)
        if (self.kmPrint_tab.columnCount() < 3):
            self.kmPrint_tab.setColumnCount(3)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setFont(font5);
        self.kmPrint_tab.setHorizontalHeaderItem(0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFont(font5);
        self.kmPrint_tab.setHorizontalHeaderItem(1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFont(font5);
        self.kmPrint_tab.setHorizontalHeaderItem(2, __qtablewidgetitem59)
        self.kmPrint_tab.setObjectName(u"kmPrint_tab")
        sizePolicy4.setHeightForWidth(self.kmPrint_tab.sizePolicy().hasHeightForWidth())
        self.kmPrint_tab.setSizePolicy(sizePolicy4)
        self.kmPrint_tab.setMinimumSize(QSize(550, 0))
        self.kmPrint_tab.setStyleSheet(u"horizontalHeader.resizeSection: (0, 500)")
        self.kmPrint_tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.kmPrint_tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.kmPrint_tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.kmPrint_tab.setTextElideMode(Qt.ElideLeft)
        self.kmPrint_tab.setSortingEnabled(False)
        self.kmPrint_tab.setRowCount(0)
        self.kmPrint_tab.horizontalHeader().setHighlightSections(True)
        self.kmPrint_tab.horizontalHeader().setProperty("showSortIndicator", False)
        self.kmPrint_tab.horizontalHeader().setStretchLastSection(False)
        self.kmPrint_tab.verticalHeader().setVisible(False)
        self.kmPrint_tab.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_64.addWidget(self.kmPrint_tab)

        self.allCountLabel = QLabel(self.frame_42)
        self.allCountLabel.setObjectName(u"allCountLabel")
        self.allCountLabel.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";")

        self.verticalLayout_64.addWidget(self.allCountLabel)


        self.verticalLayout_50.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_31)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, -1, -1, -1)
        self.label_12 = QLabel(self.frame_43)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";")

        self.horizontalLayout_24.addWidget(self.label_12)

        self.startLabelPrint_Edit = QLineEdit(self.frame_43)
        self.startLabelPrint_Edit.setObjectName(u"startLabelPrint_Edit")
        self.startLabelPrint_Edit.setEnabled(False)
        self.startLabelPrint_Edit.setMaxLength(32767)

        self.horizontalLayout_24.addWidget(self.startLabelPrint_Edit)

        self.endLabelPrint_Edit = QLineEdit(self.frame_43)
        self.endLabelPrint_Edit.setObjectName(u"endLabelPrint_Edit")
        self.endLabelPrint_Edit.setEnabled(False)
        self.endLabelPrint_Edit.setMaxLength(99999)

        self.horizontalLayout_24.addWidget(self.endLabelPrint_Edit)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_2)


        self.verticalLayout_50.addWidget(self.frame_43)


        self.horizontalLayout_23.addWidget(self.frame_31)

        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(800, 0))
        self.frame_30.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_30)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.frame_66 = QFrame(self.frame_30)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMaximumSize(QSize(16777215, 164))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(-1, 0, -1, 0)
        self.listPrinter_tab = QTableWidget(self.frame_66)
        if (self.listPrinter_tab.columnCount() < 3):
            self.listPrinter_tab.setColumnCount(3)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font2);
        self.listPrinter_tab.setHorizontalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setFont(font2);
        self.listPrinter_tab.setHorizontalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setFont(font2);
        self.listPrinter_tab.setHorizontalHeaderItem(2, __qtablewidgetitem62)
        if (self.listPrinter_tab.rowCount() < 2):
            self.listPrinter_tab.setRowCount(2)
        self.listPrinter_tab.setObjectName(u"listPrinter_tab")
        sizePolicy4.setHeightForWidth(self.listPrinter_tab.sizePolicy().hasHeightForWidth())
        self.listPrinter_tab.setSizePolicy(sizePolicy4)
        self.listPrinter_tab.setMinimumSize(QSize(550, 0))
        self.listPrinter_tab.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color: rgb(36, 149, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(36, 149, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	"
                        "padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;}")
        self.listPrinter_tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listPrinter_tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listPrinter_tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listPrinter_tab.setTextElideMode(Qt.ElideLeft)
        self.listPrinter_tab.setSortingEnabled(False)
        self.listPrinter_tab.setRowCount(2)
        self.listPrinter_tab.setColumnCount(3)
        self.listPrinter_tab.horizontalHeader().setHighlightSections(True)
        self.listPrinter_tab.horizontalHeader().setProperty("showSortIndicator", False)
        self.listPrinter_tab.horizontalHeader().setStretchLastSection(False)
        self.listPrinter_tab.verticalHeader().setVisible(False)
        self.listPrinter_tab.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_46.addWidget(self.listPrinter_tab)

        self.frame_5 = QFrame(self.frame_66)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_75 = QFrame(self.frame_5)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setStyleSheet(u"QLabel {\n"
"	color: rgb(66, 66, 66);\n"
"	font: 14pt \"Segoe UI\";\n"
"}")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_75)
        self.verticalLayout_74.setSpacing(10)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, -1, 0)
        self.frame_76 = QFrame(self.frame_75)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_76)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.Label_8 = QLabel(self.frame_76)
        self.Label_8.setObjectName(u"Label_8")
        self.Label_8.setStyleSheet(u"")

        self.verticalLayout_82.addWidget(self.Label_8, 0, Qt.AlignTop)

        self.selectedBatchForPrint_label = QLabel(self.frame_76)
        self.selectedBatchForPrint_label.setObjectName(u"selectedBatchForPrint_label")
        self.selectedBatchForPrint_label.setStyleSheet(u"")

        self.verticalLayout_82.addWidget(self.selectedBatchForPrint_label, 0, Qt.AlignTop)


        self.verticalLayout_74.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.frame_75)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_77)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.Label_9 = QLabel(self.frame_77)
        self.Label_9.setObjectName(u"Label_9")
        self.Label_9.setStyleSheet(u"")

        self.verticalLayout_83.addWidget(self.Label_9)

        self.SelectedNameForPrint_label = QLabel(self.frame_77)
        self.SelectedNameForPrint_label.setObjectName(u"SelectedNameForPrint_label")
        self.SelectedNameForPrint_label.setStyleSheet(u"")

        self.verticalLayout_83.addWidget(self.SelectedNameForPrint_label)


        self.verticalLayout_74.addWidget(self.frame_77)


        self.horizontalLayout_47.addWidget(self.frame_75)

        self.selectedImageDM = QLabel(self.frame_5)
        self.selectedImageDM.setObjectName(u"selectedImageDM")
        self.selectedImageDM.setMinimumSize(QSize(0, 0))
        self.selectedImageDM.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_47.addWidget(self.selectedImageDM)


        self.horizontalLayout_46.addWidget(self.frame_5)


        self.verticalLayout_73.addWidget(self.frame_66)

        self.toolBox_2 = QToolBox(self.frame_30)
        self.toolBox_2.setObjectName(u"toolBox_2")
        sizePolicy.setHeightForWidth(self.toolBox_2.sizePolicy().hasHeightForWidth())
        self.toolBox_2.setSizePolicy(sizePolicy)
        self.toolBox_2.setStyleSheet(u"QToolBox::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border-radius: 5px;\n"
"    color: darkgray;\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 30px; \n"
"    border-radius: 4px;\n"
"	border:1px solid #000;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(36, 149,"
                        " 255);\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(245, 246, 250);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"")
        self.toolBox_2.setFrameShadow(QFrame.Plain)
        self.toolBox_2.setLineWidth(1)
        self.printer1_page = QWidget()
        self.printer1_page.setObjectName(u"printer1_page")
        self.printer1_page.setGeometry(QRect(0, 0, 900, 482))
        self.horizontalLayout_43 = QHBoxLayout(self.printer1_page)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.frame_49 = QFrame(self.printer1_page)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy1.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy1)
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_49)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"QLabel {\n"
"	color: rgb(66, 66, 66);\n"
"	font: 16pt \"Segoe UI\";\n"
"}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_51)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.frame_51)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setStyleSheet(u"")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_62)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.Label_4 = QLabel(self.frame_62)
        self.Label_4.setObjectName(u"Label_4")
        self.Label_4.setStyleSheet(u"")

        self.verticalLayout_68.addWidget(self.Label_4)

        self.batchForPrint_label_1 = QLabel(self.frame_62)
        self.batchForPrint_label_1.setObjectName(u"batchForPrint_label_1")
        self.batchForPrint_label_1.setStyleSheet(u"")

        self.verticalLayout_68.addWidget(self.batchForPrint_label_1)


        self.verticalLayout_65.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_51)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_63)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.Label_5 = QLabel(self.frame_63)
        self.Label_5.setObjectName(u"Label_5")
        self.Label_5.setStyleSheet(u"")

        self.verticalLayout_69.addWidget(self.Label_5)

        self.nameForPrint_label_1 = QLabel(self.frame_63)
        self.nameForPrint_label_1.setObjectName(u"nameForPrint_label_1")
        self.nameForPrint_label_1.setStyleSheet(u"")

        self.verticalLayout_69.addWidget(self.nameForPrint_label_1)


        self.verticalLayout_65.addWidget(self.frame_63, 0, Qt.AlignTop)


        self.verticalLayout_51.addWidget(self.frame_51, 0, Qt.AlignTop)

        self.frame_60 = QFrame(self.frame_49)
        self.frame_60.setObjectName(u"frame_60")
        sizePolicy.setHeightForWidth(self.frame_60.sizePolicy().hasHeightForWidth())
        self.frame_60.setSizePolicy(sizePolicy)
        self.frame_60.setStyleSheet(u"")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.frame_60)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_79)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.imageDM_printer_1 = QLabel(self.frame_79)
        self.imageDM_printer_1.setObjectName(u"imageDM_printer_1")
        sizePolicy.setHeightForWidth(self.imageDM_printer_1.sizePolicy().hasHeightForWidth())
        self.imageDM_printer_1.setSizePolicy(sizePolicy)
        self.imageDM_printer_1.setMinimumSize(QSize(0, 0))
        self.imageDM_printer_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_88.addWidget(self.imageDM_printer_1)

        self.rollNumberEdit_1 = QLineEdit(self.frame_79)
        self.rollNumberEdit_1.setObjectName(u"rollNumberEdit_1")
        self.rollNumberEdit_1.setMinimumSize(QSize(0, 32))

        self.verticalLayout_88.addWidget(self.rollNumberEdit_1)

        self.dateEdit_1 = QDateEdit(self.frame_79)
        self.dateEdit_1.setObjectName(u"dateEdit_1")
        self.dateEdit_1.setEnabled(True)
        self.dateEdit_1.setMinimumSize(QSize(0, 32))
        self.dateEdit_1.setStyleSheet(u"QDateEdit\n"
"{\n"
"	color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";\n"
"    min-height:30px;\n"
"    max-height:30px;\n"
"    border-radius:5px;\n"
"    border:1px solid;\n"
"	border-color: rgb(66, 66, 66);\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QDateEdit:hover,.QDateEdit:focus\n"
"{\n"
"    border-radius:2px;\n"
"    border:1px solid #0f6dbe;\n"
"}\n"
"\n"
"QDateEdit::drop-down\n"
"{\n"
"	background-color: rgb(36, 149, 255);\n"
"    border:1px solid;\n"
"	border-radius:5px;\n"
"    width:30px;\n"
"	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"}\n"
"\n"
"font: 12pt;")
        self.dateEdit_1.setCalendarPopup(True)
        self.dateEdit_1.setDate(QDate(2023, 12, 1))

        self.verticalLayout_88.addWidget(self.dateEdit_1)

        self.frame_86 = QFrame(self.frame_79)
        self.frame_86.setObjectName(u"frame_86")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_86.sizePolicy().hasHeightForWidth())
        self.frame_86.setSizePolicy(sizePolicy9)
        self.frame_86.setMaximumSize(QSize(16777215, 200))
        self.frame_86.setStyleSheet(u"\n"
"QComboBox {\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 30px; \n"
"    border-radius: 4px;\n"
"	border:1px solid #000;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(36, 149, 255);\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(245, 246, 250);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_86)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 5)
        self.template_combobox = QComboBox(self.frame_86)
        self.template_combobox.setObjectName(u"template_combobox")
        self.template_combobox.setMinimumSize(QSize(300, 32))
        self.template_combobox.setMaximumSize(QSize(16777215, 30))
        self.template_combobox.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.template_combobox.setMaxVisibleItems(20)

        self.verticalLayout_67.addWidget(self.template_combobox)


        self.verticalLayout_88.addWidget(self.frame_86)


        self.horizontalLayout_48.addWidget(self.frame_79)

        self.frame_78 = QFrame(self.frame_60)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_78)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.pausePrint_btn_1 = QPushButton(self.frame_78)
        self.pausePrint_btn_1.setObjectName(u"pausePrint_btn_1")
        self.pausePrint_btn_1.setEnabled(True)
        self.pausePrint_btn_1.setMinimumSize(QSize(0, 40))

        self.verticalLayout_84.addWidget(self.pausePrint_btn_1)

        self.endPrint_btn_1 = QPushButton(self.frame_78)
        self.endPrint_btn_1.setObjectName(u"endPrint_btn_1")
        self.endPrint_btn_1.setEnabled(True)
        self.endPrint_btn_1.setMinimumSize(QSize(0, 40))

        self.verticalLayout_84.addWidget(self.endPrint_btn_1)


        self.horizontalLayout_48.addWidget(self.frame_78, 0, Qt.AlignBottom)


        self.verticalLayout_51.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_49)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.Label_2 = QLabel(self.frame_61)
        self.Label_2.setObjectName(u"Label_2")
        self.Label_2.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";")

        self.horizontalLayout_41.addWidget(self.Label_2)

        self.countFromPrint_line_1 = QLineEdit(self.frame_61)
        self.countFromPrint_line_1.setObjectName(u"countFromPrint_line_1")
        self.countFromPrint_line_1.setEnabled(False)

        self.horizontalLayout_41.addWidget(self.countFromPrint_line_1)


        self.verticalLayout_51.addWidget(self.frame_61)


        self.horizontalLayout_43.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.printer1_page)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy3.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy3)
        self.frame_50.setMinimumSize(QSize(400, 0))
        self.frame_50.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_50)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.frame_50)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setStyleSheet(u"QLabel {\n"
"	color: rgb(66, 66, 66);\n"
"	font: 16pt \"Segoe UI\";\n"
"}")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.Label_11 = QLabel(self.frame_84)
        self.Label_11.setObjectName(u"Label_11")
        self.Label_11.setStyleSheet(u"")

        self.horizontalLayout_52.addWidget(self.Label_11)


        self.verticalLayout_66.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.frame_50)
        self.frame_85.setObjectName(u"frame_85")
        sizePolicy.setHeightForWidth(self.frame_85.sizePolicy().hasHeightForWidth())
        self.frame_85.setSizePolicy(sizePolicy)
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_85)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.cameraTextEdit_1 = QPlainTextEdit(self.frame_85)
        self.cameraTextEdit_1.setObjectName(u"cameraTextEdit_1")
        self.cameraTextEdit_1.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(66, 66, 66);\n"
"font: 14pt \"Segoe UI\";\n"
"padding-left: 10px")
        self.cameraTextEdit_1.setReadOnly(True)
        self.cameraTextEdit_1.setMaximumBlockCount(20)

        self.verticalLayout_87.addWidget(self.cameraTextEdit_1)


        self.verticalLayout_66.addWidget(self.frame_85)


        self.horizontalLayout_43.addWidget(self.frame_50)

        self.toolBox_2.addItem(self.printer1_page, u"Novex 64-04")
        self.printer2_page = QWidget()
        self.printer2_page.setObjectName(u"printer2_page")
        self.printer2_page.setGeometry(QRect(0, 0, 900, 482))
        self.horizontalLayout_45 = QHBoxLayout(self.printer2_page)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_67 = QFrame(self.printer2_page)
        self.frame_67.setObjectName(u"frame_67")
        sizePolicy1.setHeightForWidth(self.frame_67.sizePolicy().hasHeightForWidth())
        self.frame_67.setSizePolicy(sizePolicy1)
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_67)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"QLabel {\n"
"	color: rgb(66, 66, 66);\n"
"	font: 16pt \"Segoe UI\";\n"
"}")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_68)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_69)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.Label_6 = QLabel(self.frame_69)
        self.Label_6.setObjectName(u"Label_6")
        self.Label_6.setStyleSheet(u"")

        self.verticalLayout_77.addWidget(self.Label_6)

        self.batchForPrint_label_2 = QLabel(self.frame_69)
        self.batchForPrint_label_2.setObjectName(u"batchForPrint_label_2")
        self.batchForPrint_label_2.setStyleSheet(u"")

        self.verticalLayout_77.addWidget(self.batchForPrint_label_2)


        self.verticalLayout_76.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_68)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_70)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.Label_7 = QLabel(self.frame_70)
        self.Label_7.setObjectName(u"Label_7")
        self.Label_7.setStyleSheet(u"")

        self.verticalLayout_79.addWidget(self.Label_7)

        self.nameForPrint_label_2 = QLabel(self.frame_70)
        self.nameForPrint_label_2.setObjectName(u"nameForPrint_label_2")
        self.nameForPrint_label_2.setStyleSheet(u"")

        self.verticalLayout_79.addWidget(self.nameForPrint_label_2)


        self.verticalLayout_76.addWidget(self.frame_70, 0, Qt.AlignTop)


        self.verticalLayout_75.addWidget(self.frame_68, 0, Qt.AlignTop)

        self.frame_71 = QFrame(self.frame_67)
        self.frame_71.setObjectName(u"frame_71")
        sizePolicy.setHeightForWidth(self.frame_71.sizePolicy().hasHeightForWidth())
        self.frame_71.setSizePolicy(sizePolicy)
        self.frame_71.setStyleSheet(u"")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_80 = QFrame(self.frame_71)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_80)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.imageDM_printer_2 = QLabel(self.frame_80)
        self.imageDM_printer_2.setObjectName(u"imageDM_printer_2")
        self.imageDM_printer_2.setMinimumSize(QSize(0, 0))
        self.imageDM_printer_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_80.addWidget(self.imageDM_printer_2)

        self.rollNumberEdit_2 = QLineEdit(self.frame_80)
        self.rollNumberEdit_2.setObjectName(u"rollNumberEdit_2")
        self.rollNumberEdit_2.setMinimumSize(QSize(50, 32))

        self.verticalLayout_80.addWidget(self.rollNumberEdit_2)

        self.dateEdit_2 = QDateEdit(self.frame_80)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setEnabled(True)
        self.dateEdit_2.setMinimumSize(QSize(0, 32))
        self.dateEdit_2.setStyleSheet(u"QDateEdit\n"
"{\n"
"	color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";\n"
"    min-height:30px;\n"
"    max-height:30px;\n"
"    border-radius:5px;\n"
"    border:1px solid;\n"
"	border-color: rgb(66, 66, 66);\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QDateEdit:hover,.QDateEdit:focus\n"
"{\n"
"    border-radius:2px;\n"
"    border:1px solid #0f6dbe;\n"
"}\n"
"\n"
"QDateEdit::drop-down\n"
"{\n"
"	background-color: rgb(36, 149, 255);\n"
"    border:1px solid;\n"
"	border-radius:5px;\n"
"    width:30px;\n"
"	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"}")
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QDate(2023, 12, 1))

        self.verticalLayout_80.addWidget(self.dateEdit_2)

        self.template_combobox_2 = QComboBox(self.frame_80)
        self.template_combobox_2.setObjectName(u"template_combobox_2")
        self.template_combobox_2.setMinimumSize(QSize(300, 32))
        self.template_combobox_2.setMaximumSize(QSize(16777215, 30))
        self.template_combobox_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.template_combobox_2.setMaxVisibleItems(20)

        self.verticalLayout_80.addWidget(self.template_combobox_2)


        self.horizontalLayout_50.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_71)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_81)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.pausePrint_btn_2 = QPushButton(self.frame_81)
        self.pausePrint_btn_2.setObjectName(u"pausePrint_btn_2")
        self.pausePrint_btn_2.setEnabled(True)
        self.pausePrint_btn_2.setMinimumSize(QSize(0, 40))

        self.verticalLayout_85.addWidget(self.pausePrint_btn_2)

        self.endPrint_btn_2 = QPushButton(self.frame_81)
        self.endPrint_btn_2.setObjectName(u"endPrint_btn_2")
        self.endPrint_btn_2.setEnabled(True)
        self.endPrint_btn_2.setMinimumSize(QSize(0, 40))

        self.verticalLayout_85.addWidget(self.endPrint_btn_2)


        self.horizontalLayout_50.addWidget(self.frame_81, 0, Qt.AlignBottom)


        self.verticalLayout_75.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.frame_67)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.Label_3 = QLabel(self.frame_72)
        self.Label_3.setObjectName(u"Label_3")
        self.Label_3.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";")

        self.horizontalLayout_44.addWidget(self.Label_3)

        self.countFromPrint_line_2 = QLineEdit(self.frame_72)
        self.countFromPrint_line_2.setObjectName(u"countFromPrint_line_2")
        self.countFromPrint_line_2.setEnabled(False)

        self.horizontalLayout_44.addWidget(self.countFromPrint_line_2)


        self.verticalLayout_75.addWidget(self.frame_72)


        self.horizontalLayout_45.addWidget(self.frame_67)

        self.frame_73 = QFrame(self.printer2_page)
        self.frame_73.setObjectName(u"frame_73")
        sizePolicy1.setHeightForWidth(self.frame_73.sizePolicy().hasHeightForWidth())
        self.frame_73.setSizePolicy(sizePolicy1)
        self.frame_73.setMinimumSize(QSize(400, 0))
        self.frame_73.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_73)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_82 = QFrame(self.frame_73)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setStyleSheet(u"QLabel {\n"
"	color: rgb(66, 66, 66);\n"
"	font: 16pt \"Segoe UI\";\n"
"}")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.Label_10 = QLabel(self.frame_82)
        self.Label_10.setObjectName(u"Label_10")
        self.Label_10.setStyleSheet(u"")

        self.horizontalLayout_51.addWidget(self.Label_10)


        self.verticalLayout_81.addWidget(self.frame_82, 0, Qt.AlignTop)

        self.frame_83 = QFrame(self.frame_73)
        self.frame_83.setObjectName(u"frame_83")
        sizePolicy.setHeightForWidth(self.frame_83.sizePolicy().hasHeightForWidth())
        self.frame_83.setSizePolicy(sizePolicy)
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_83)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.cameraTextEdit_2 = QPlainTextEdit(self.frame_83)
        self.cameraTextEdit_2.setObjectName(u"cameraTextEdit_2")
        self.cameraTextEdit_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(66, 66, 66);\n"
"font: 14pt \"Segoe UI\";\n"
"padding-left: 10px")
        self.cameraTextEdit_2.setReadOnly(True)
        self.cameraTextEdit_2.setMaximumBlockCount(20)

        self.verticalLayout_86.addWidget(self.cameraTextEdit_2)


        self.verticalLayout_81.addWidget(self.frame_83)


        self.horizontalLayout_45.addWidget(self.frame_73)

        self.toolBox_2.addItem(self.printer2_page, u"Novex 64-06")
        self.printer3_page = QWidget()
        self.printer3_page.setObjectName(u"printer3_page")
        self.printer3_page.setGeometry(QRect(0, 0, 900, 482))
        self.horizontalLayout_58 = QHBoxLayout(self.printer3_page)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.frame_88 = QFrame(self.printer3_page)
        self.frame_88.setObjectName(u"frame_88")
        sizePolicy1.setHeightForWidth(self.frame_88.sizePolicy().hasHeightForWidth())
        self.frame_88.setSizePolicy(sizePolicy1)
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_88)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.frame_94 = QFrame(self.frame_88)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setStyleSheet(u"QLabel {\n"
"	color: rgb(66, 66, 66);\n"
"	font: 16pt \"Segoe UI\";\n"
"}")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_94)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setStyleSheet(u"")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_95)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.Label_12 = QLabel(self.frame_95)
        self.Label_12.setObjectName(u"Label_12")
        self.Label_12.setStyleSheet(u"")

        self.verticalLayout_98.addWidget(self.Label_12)

        self.batchForPrint_label_3 = QLabel(self.frame_95)
        self.batchForPrint_label_3.setObjectName(u"batchForPrint_label_3")
        self.batchForPrint_label_3.setStyleSheet(u"")

        self.verticalLayout_98.addWidget(self.batchForPrint_label_3)


        self.verticalLayout_97.addWidget(self.frame_95)

        self.frame_96 = QFrame(self.frame_94)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_96)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.Label_13 = QLabel(self.frame_96)
        self.Label_13.setObjectName(u"Label_13")
        self.Label_13.setStyleSheet(u"")

        self.verticalLayout_99.addWidget(self.Label_13)

        self.nameForPrint_label_3 = QLabel(self.frame_96)
        self.nameForPrint_label_3.setObjectName(u"nameForPrint_label_3")
        self.nameForPrint_label_3.setStyleSheet(u"")

        self.verticalLayout_99.addWidget(self.nameForPrint_label_3)


        self.verticalLayout_97.addWidget(self.frame_96, 0, Qt.AlignTop)


        self.verticalLayout_96.addWidget(self.frame_94, 0, Qt.AlignTop)

        self.frame_97 = QFrame(self.frame_88)
        self.frame_97.setObjectName(u"frame_97")
        sizePolicy.setHeightForWidth(self.frame_97.sizePolicy().hasHeightForWidth())
        self.frame_97.setSizePolicy(sizePolicy)
        self.frame_97.setStyleSheet(u"")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_98)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.imageDM_printer_3 = QLabel(self.frame_98)
        self.imageDM_printer_3.setObjectName(u"imageDM_printer_3")
        self.imageDM_printer_3.setMinimumSize(QSize(0, 0))
        self.imageDM_printer_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_100.addWidget(self.imageDM_printer_3)

        self.rollNumberEdit_3 = QLineEdit(self.frame_98)
        self.rollNumberEdit_3.setObjectName(u"rollNumberEdit_3")
        self.rollNumberEdit_3.setMinimumSize(QSize(50, 32))

        self.verticalLayout_100.addWidget(self.rollNumberEdit_3)

        self.dateEdit_3 = QDateEdit(self.frame_98)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setEnabled(True)
        self.dateEdit_3.setMinimumSize(QSize(0, 32))
        self.dateEdit_3.setStyleSheet(u"QDateEdit\n"
"{\n"
"	color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";\n"
"    min-height:30px;\n"
"    max-height:30px;\n"
"    border-radius:5px;\n"
"    border:1px solid;\n"
"	border-color: rgb(66, 66, 66);\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QDateEdit:hover,.QDateEdit:focus\n"
"{\n"
"    border-radius:2px;\n"
"    border:1px solid #0f6dbe;\n"
"}\n"
"\n"
"QDateEdit::drop-down\n"
"{\n"
"	background-color: rgb(36, 149, 255);\n"
"    border:1px solid;\n"
"	border-radius:5px;\n"
"    width:30px;\n"
"	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"}")
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setDate(QDate(2023, 12, 1))

        self.verticalLayout_100.addWidget(self.dateEdit_3)

        self.template_combobox_3 = QComboBox(self.frame_98)
        self.template_combobox_3.setObjectName(u"template_combobox_3")
        self.template_combobox_3.setMinimumSize(QSize(300, 32))
        self.template_combobox_3.setMaximumSize(QSize(16777215, 30))
        self.template_combobox_3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.template_combobox_3.setMaxVisibleItems(20)

        self.verticalLayout_100.addWidget(self.template_combobox_3)


        self.horizontalLayout_55.addWidget(self.frame_98)

        self.frame_99 = QFrame(self.frame_97)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_99)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.pausePrint_btn_3 = QPushButton(self.frame_99)
        self.pausePrint_btn_3.setObjectName(u"pausePrint_btn_3")
        self.pausePrint_btn_3.setEnabled(True)
        self.pausePrint_btn_3.setMinimumSize(QSize(0, 40))

        self.verticalLayout_101.addWidget(self.pausePrint_btn_3)

        self.endPrint_btn_3 = QPushButton(self.frame_99)
        self.endPrint_btn_3.setObjectName(u"endPrint_btn_3")
        self.endPrint_btn_3.setEnabled(True)
        self.endPrint_btn_3.setMinimumSize(QSize(0, 40))

        self.verticalLayout_101.addWidget(self.endPrint_btn_3)


        self.horizontalLayout_55.addWidget(self.frame_99, 0, Qt.AlignBottom)


        self.verticalLayout_96.addWidget(self.frame_97)

        self.frame_100 = QFrame(self.frame_88)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.Label_14 = QLabel(self.frame_100)
        self.Label_14.setObjectName(u"Label_14")
        self.Label_14.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 12pt \"Segoe UI\";")

        self.horizontalLayout_56.addWidget(self.Label_14)

        self.countFromPrint_line_3 = QLineEdit(self.frame_100)
        self.countFromPrint_line_3.setObjectName(u"countFromPrint_line_3")
        self.countFromPrint_line_3.setEnabled(False)

        self.horizontalLayout_56.addWidget(self.countFromPrint_line_3)


        self.verticalLayout_96.addWidget(self.frame_100)


        self.horizontalLayout_58.addWidget(self.frame_88)

        self.frame_101 = QFrame(self.printer3_page)
        self.frame_101.setObjectName(u"frame_101")
        sizePolicy1.setHeightForWidth(self.frame_101.sizePolicy().hasHeightForWidth())
        self.frame_101.setSizePolicy(sizePolicy1)
        self.frame_101.setMinimumSize(QSize(400, 0))
        self.frame_101.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_101)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.frame_102 = QFrame(self.frame_101)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setStyleSheet(u"QLabel {\n"
"	color: rgb(66, 66, 66);\n"
"	font: 16pt \"Segoe UI\";\n"
"}")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.Label_15 = QLabel(self.frame_102)
        self.Label_15.setObjectName(u"Label_15")
        self.Label_15.setStyleSheet(u"")

        self.horizontalLayout_57.addWidget(self.Label_15)


        self.verticalLayout_102.addWidget(self.frame_102, 0, Qt.AlignTop)

        self.frame_103 = QFrame(self.frame_101)
        self.frame_103.setObjectName(u"frame_103")
        sizePolicy.setHeightForWidth(self.frame_103.sizePolicy().hasHeightForWidth())
        self.frame_103.setSizePolicy(sizePolicy)
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_103)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.cameraTextEdit_3 = QPlainTextEdit(self.frame_103)
        self.cameraTextEdit_3.setObjectName(u"cameraTextEdit_3")
        self.cameraTextEdit_3.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(66, 66, 66);\n"
"font: 14pt \"Segoe UI\";\n"
"padding-left: 10px")
        self.cameraTextEdit_3.setReadOnly(True)
        self.cameraTextEdit_3.setMaximumBlockCount(20)

        self.verticalLayout_103.addWidget(self.cameraTextEdit_3)


        self.verticalLayout_102.addWidget(self.frame_103)


        self.horizontalLayout_58.addWidget(self.frame_101)

        self.toolBox_2.addItem(self.printer3_page, u"\u041f\u0440\u0438\u043d\u0442\u0435\u0440 \u043d\u0435 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d")

        self.verticalLayout_73.addWidget(self.toolBox_2)


        self.horizontalLayout_23.addWidget(self.frame_30)


        self.verticalLayout_49.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.printPage)
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.settingPage.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color: rgb(36, 149, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;\n"
"}\n"
"QTableWidg"
                        "et::item:selected{\n"
"	background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(36, 149, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;}\n"
"\n"
"/*LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(245, 246, 250);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLine"
                        "Edit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.settingPage)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.settingProduct_Frame = QFrame(self.settingPage)
        self.settingProduct_Frame.setObjectName(u"settingProduct_Frame")
        sizePolicy1.setHeightForWidth(self.settingProduct_Frame.sizePolicy().hasHeightForWidth())
        self.settingProduct_Frame.setSizePolicy(sizePolicy1)
        self.settingProduct_Frame.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(66, 66, 66);\n"
"	selection-color: rgb(255, 0, 255);\n"
"}\n"
"")
        self.settingProduct_Frame.setFrameShape(QFrame.StyledPanel)
        self.settingProduct_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.settingProduct_Frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_7 = QFrame(self.settingProduct_Frame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy6.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy6)
        self.frame_7.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_24.addWidget(self.label_6, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_23.addWidget(self.frame_7)

        self.frame_12 = QFrame(self.settingProduct_Frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_12)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.listProductContainer = QFrame(self.frame_12)
        self.listProductContainer.setObjectName(u"listProductContainer")
        self.listProductContainer.setFrameShape(QFrame.StyledPanel)
        self.listProductContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.listProductContainer)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.currentProd_Tab = QTableWidget(self.listProductContainer)
        if (self.currentProd_Tab.columnCount() < 4):
            self.currentProd_Tab.setColumnCount(4)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font5);
        self.currentProd_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setFont(font2);
        self.currentProd_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFont(font2);
        self.currentProd_Tab.setHorizontalHeaderItem(2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFont(font2);
        self.currentProd_Tab.setHorizontalHeaderItem(3, __qtablewidgetitem66)
        self.currentProd_Tab.setObjectName(u"currentProd_Tab")
        self.currentProd_Tab.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.currentProd_Tab.sizePolicy().hasHeightForWidth())
        self.currentProd_Tab.setSizePolicy(sizePolicy4)
        self.currentProd_Tab.setMinimumSize(QSize(0, 0))
        self.currentProd_Tab.setMaximumSize(QSize(16777215, 16777215))
        self.currentProd_Tab.setFrameShape(QFrame.NoFrame)
        self.currentProd_Tab.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.currentProd_Tab.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.currentProd_Tab.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.currentProd_Tab.setAutoScroll(True)
        self.currentProd_Tab.setAutoScrollMargin(16)
        self.currentProd_Tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.currentProd_Tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.currentProd_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.currentProd_Tab.setShowGrid(True)
        self.currentProd_Tab.setGridStyle(Qt.SolidLine)
        self.currentProd_Tab.setWordWrap(True)
        self.currentProd_Tab.setCornerButtonEnabled(True)
        self.currentProd_Tab.setRowCount(0)
        self.currentProd_Tab.setColumnCount(4)
        self.currentProd_Tab.horizontalHeader().setVisible(True)
        self.currentProd_Tab.horizontalHeader().setCascadingSectionResizes(True)
        self.currentProd_Tab.horizontalHeader().setMinimumSectionSize(0)
        self.currentProd_Tab.horizontalHeader().setDefaultSectionSize(160)
        self.currentProd_Tab.horizontalHeader().setHighlightSections(False)
        self.currentProd_Tab.horizontalHeader().setStretchLastSection(False)
        self.currentProd_Tab.verticalHeader().setVisible(False)
        self.currentProd_Tab.verticalHeader().setMinimumSectionSize(25)
        self.currentProd_Tab.verticalHeader().setDefaultSectionSize(30)
        self.currentProd_Tab.verticalHeader().setHighlightSections(False)
        self.currentProd_Tab.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_33.addWidget(self.currentProd_Tab)


        self.verticalLayout_32.addWidget(self.listProductContainer)

        self.productButtonContainer = QFrame(self.frame_12)
        self.productButtonContainer.setObjectName(u"productButtonContainer")
        self.productButtonContainer.setMinimumSize(QSize(0, 0))
        self.productButtonContainer.setMaximumSize(QSize(16777215, 62))
        self.productButtonContainer.setFrameShape(QFrame.StyledPanel)
        self.productButtonContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.productButtonContainer)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.addProductBtn = QPushButton(self.productButtonContainer)
        self.addProductBtn.setObjectName(u"addProductBtn")
        self.addProductBtn.setMinimumSize(QSize(150, 50))
        self.addProductBtn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_15.addWidget(self.addProductBtn)

        self.editProductBtn = QPushButton(self.productButtonContainer)
        self.editProductBtn.setObjectName(u"editProductBtn")
        self.editProductBtn.setEnabled(False)
        self.editProductBtn.setMinimumSize(QSize(150, 50))
        self.editProductBtn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_15.addWidget(self.editProductBtn)

        self.deleteProductBtn = QPushButton(self.productButtonContainer)
        self.deleteProductBtn.setObjectName(u"deleteProductBtn")
        self.deleteProductBtn.setEnabled(False)
        self.deleteProductBtn.setMinimumSize(QSize(150, 50))
        self.deleteProductBtn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_15.addWidget(self.deleteProductBtn)


        self.verticalLayout_32.addWidget(self.productButtonContainer, 0, Qt.AlignHCenter)

        self.editProductContainer = QFrame(self.frame_12)
        self.editProductContainer.setObjectName(u"editProductContainer")
        sizePolicy9.setHeightForWidth(self.editProductContainer.sizePolicy().hasHeightForWidth())
        self.editProductContainer.setSizePolicy(sizePolicy9)
        self.editProductContainer.setMaximumSize(QSize(16777215, 0))
        self.editProductContainer.setFrameShape(QFrame.StyledPanel)
        self.editProductContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.editProductContainer)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.editProductContainer)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_32)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.productNameUpdate = QLineEdit(self.frame_33)
        self.productNameUpdate.setObjectName(u"productNameUpdate")
        sizePolicy6.setHeightForWidth(self.productNameUpdate.sizePolicy().hasHeightForWidth())
        self.productNameUpdate.setSizePolicy(sizePolicy6)

        self.horizontalLayout_27.addWidget(self.productNameUpdate)


        self.verticalLayout_43.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.productGTINeditUpdate = QLineEdit(self.frame_34)
        self.productGTINeditUpdate.setObjectName(u"productGTINeditUpdate")
        sizePolicy6.setHeightForWidth(self.productGTINeditUpdate.sizePolicy().hasHeightForWidth())
        self.productGTINeditUpdate.setSizePolicy(sizePolicy6)

        self.horizontalLayout_28.addWidget(self.productGTINeditUpdate)


        self.verticalLayout_43.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.productCountEditUpdate = QLineEdit(self.frame_35)
        self.productCountEditUpdate.setObjectName(u"productCountEditUpdate")
        sizePolicy6.setHeightForWidth(self.productCountEditUpdate.sizePolicy().hasHeightForWidth())
        self.productCountEditUpdate.setSizePolicy(sizePolicy6)

        self.horizontalLayout_29.addWidget(self.productCountEditUpdate)


        self.verticalLayout_43.addWidget(self.frame_35)


        self.horizontalLayout_30.addWidget(self.frame_32)

        self.frame_36 = QFrame(self.editProductContainer)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy10)
        self.frame_36.setStyleSheet(u"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_36)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.updateProductConfirmBtn = QPushButton(self.frame_36)
        self.updateProductConfirmBtn.setObjectName(u"updateProductConfirmBtn")
        self.updateProductConfirmBtn.setMinimumSize(QSize(150, 50))
        self.updateProductConfirmBtn.setMaximumSize(QSize(150, 16777215))
        self.updateProductConfirmBtn.setStyleSheet(u"")

        self.verticalLayout_44.addWidget(self.updateProductConfirmBtn)

        self.updateProductCanselBtn = QPushButton(self.frame_36)
        self.updateProductCanselBtn.setObjectName(u"updateProductCanselBtn")
        self.updateProductCanselBtn.setMinimumSize(QSize(0, 50))
        self.updateProductCanselBtn.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_44.addWidget(self.updateProductCanselBtn)


        self.horizontalLayout_30.addWidget(self.frame_36)


        self.verticalLayout_32.addWidget(self.editProductContainer)

        self.addProductContainer = QFrame(self.frame_12)
        self.addProductContainer.setObjectName(u"addProductContainer")
        sizePolicy9.setHeightForWidth(self.addProductContainer.sizePolicy().hasHeightForWidth())
        self.addProductContainer.setSizePolicy(sizePolicy9)
        self.addProductContainer.setMaximumSize(QSize(16777215, 0))
        self.addProductContainer.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(66, 66, 66);\n"
"	selection-color: rgb(255, 0, 255);\n"
"}\n"
"")
        self.addProductContainer.setFrameShape(QFrame.StyledPanel)
        self.addProductContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.addProductContainer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.addProductContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.productNameEdit = QLineEdit(self.frame_16)
        self.productNameEdit.setObjectName(u"productNameEdit")
        sizePolicy6.setHeightForWidth(self.productNameEdit.sizePolicy().hasHeightForWidth())
        self.productNameEdit.setSizePolicy(sizePolicy6)

        self.horizontalLayout_12.addWidget(self.productNameEdit)


        self.verticalLayout_34.addWidget(self.frame_16)

        self.frame_18 = QFrame(self.frame_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.productGTINedit = QLineEdit(self.frame_18)
        self.productGTINedit.setObjectName(u"productGTINedit")
        sizePolicy6.setHeightForWidth(self.productGTINedit.sizePolicy().hasHeightForWidth())
        self.productGTINedit.setSizePolicy(sizePolicy6)

        self.horizontalLayout_13.addWidget(self.productGTINedit)


        self.verticalLayout_34.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.productCountEdit = QLineEdit(self.frame_19)
        self.productCountEdit.setObjectName(u"productCountEdit")
        sizePolicy6.setHeightForWidth(self.productCountEdit.sizePolicy().hasHeightForWidth())
        self.productCountEdit.setSizePolicy(sizePolicy6)

        self.horizontalLayout_14.addWidget(self.productCountEdit)


        self.verticalLayout_34.addWidget(self.frame_19)


        self.horizontalLayout_9.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.addProductContainer)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy10.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy10)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_4)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.addProductConfirmBtn = QPushButton(self.frame_4)
        self.addProductConfirmBtn.setObjectName(u"addProductConfirmBtn")
        self.addProductConfirmBtn.setMinimumSize(QSize(150, 50))
        self.addProductConfirmBtn.setMaximumSize(QSize(150, 16777215))
        self.addProductConfirmBtn.setStyleSheet(u"")

        self.verticalLayout_35.addWidget(self.addProductConfirmBtn)

        self.addProductCanselBtn = QPushButton(self.frame_4)
        self.addProductCanselBtn.setObjectName(u"addProductCanselBtn")
        self.addProductCanselBtn.setMinimumSize(QSize(0, 50))
        self.addProductCanselBtn.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_35.addWidget(self.addProductCanselBtn)


        self.horizontalLayout_9.addWidget(self.frame_4)


        self.verticalLayout_32.addWidget(self.addProductContainer)


        self.verticalLayout_23.addWidget(self.frame_12)


        self.horizontalLayout_8.addWidget(self.settingProduct_Frame)

        self.addLine_Frame = QFrame(self.settingPage)
        self.addLine_Frame.setObjectName(u"addLine_Frame")
        sizePolicy1.setHeightForWidth(self.addLine_Frame.sizePolicy().hasHeightForWidth())
        self.addLine_Frame.setSizePolicy(sizePolicy1)
        self.addLine_Frame.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(66, 66, 66);\n"
"	selection-color: rgb(255, 0, 255);\n"
"}\n"
"")
        self.addLine_Frame.setFrameShape(QFrame.StyledPanel)
        self.addLine_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.addLine_Frame)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_13 = QFrame(self.addLine_Frame)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy6.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy6)
        self.frame_13.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_13)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_30.addWidget(self.label_7, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_31.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.addLine_Frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_14)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.listLineContainer = QFrame(self.frame_14)
        self.listLineContainer.setObjectName(u"listLineContainer")
        self.listLineContainer.setFrameShape(QFrame.StyledPanel)
        self.listLineContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.listLineContainer)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.currentLine_Tab = QTableWidget(self.listLineContainer)
        if (self.currentLine_Tab.columnCount() < 3):
            self.currentLine_Tab.setColumnCount(3)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setFont(font5);
        self.currentLine_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setFont(font2);
        self.currentLine_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setFont(font2);
        self.currentLine_Tab.setHorizontalHeaderItem(2, __qtablewidgetitem69)
        self.currentLine_Tab.setObjectName(u"currentLine_Tab")
        self.currentLine_Tab.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.currentLine_Tab.sizePolicy().hasHeightForWidth())
        self.currentLine_Tab.setSizePolicy(sizePolicy4)
        self.currentLine_Tab.setMinimumSize(QSize(0, 0))
        self.currentLine_Tab.setMaximumSize(QSize(16777215, 16777215))
        self.currentLine_Tab.setFrameShape(QFrame.NoFrame)
        self.currentLine_Tab.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.currentLine_Tab.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.currentLine_Tab.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.currentLine_Tab.setAutoScroll(True)
        self.currentLine_Tab.setAutoScrollMargin(16)
        self.currentLine_Tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.currentLine_Tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.currentLine_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.currentLine_Tab.setShowGrid(True)
        self.currentLine_Tab.setGridStyle(Qt.SolidLine)
        self.currentLine_Tab.setWordWrap(True)
        self.currentLine_Tab.setCornerButtonEnabled(True)
        self.currentLine_Tab.setRowCount(0)
        self.currentLine_Tab.setColumnCount(3)
        self.currentLine_Tab.horizontalHeader().setVisible(True)
        self.currentLine_Tab.horizontalHeader().setCascadingSectionResizes(True)
        self.currentLine_Tab.horizontalHeader().setMinimumSectionSize(0)
        self.currentLine_Tab.horizontalHeader().setDefaultSectionSize(160)
        self.currentLine_Tab.horizontalHeader().setHighlightSections(False)
        self.currentLine_Tab.horizontalHeader().setStretchLastSection(False)
        self.currentLine_Tab.verticalHeader().setVisible(False)
        self.currentLine_Tab.verticalHeader().setMinimumSectionSize(25)
        self.currentLine_Tab.verticalHeader().setDefaultSectionSize(30)
        self.currentLine_Tab.verticalHeader().setHighlightSections(False)
        self.currentLine_Tab.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_37.addWidget(self.currentLine_Tab)


        self.verticalLayout_36.addWidget(self.listLineContainer)

        self.lineButtonContainer = QFrame(self.frame_14)
        self.lineButtonContainer.setObjectName(u"lineButtonContainer")
        self.lineButtonContainer.setFrameShape(QFrame.StyledPanel)
        self.lineButtonContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.lineButtonContainer)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.addLineBtn = QPushButton(self.lineButtonContainer)
        self.addLineBtn.setObjectName(u"addLineBtn")
        self.addLineBtn.setMinimumSize(QSize(150, 50))
        self.addLineBtn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_16.addWidget(self.addLineBtn)

        self.editLineBtn = QPushButton(self.lineButtonContainer)
        self.editLineBtn.setObjectName(u"editLineBtn")
        self.editLineBtn.setEnabled(False)
        self.editLineBtn.setMinimumSize(QSize(150, 50))
        self.editLineBtn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_16.addWidget(self.editLineBtn)

        self.deleteLineBtn = QPushButton(self.lineButtonContainer)
        self.deleteLineBtn.setObjectName(u"deleteLineBtn")
        self.deleteLineBtn.setEnabled(False)
        self.deleteLineBtn.setMinimumSize(QSize(150, 50))
        self.deleteLineBtn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_16.addWidget(self.deleteLineBtn)


        self.verticalLayout_36.addWidget(self.lineButtonContainer, 0, Qt.AlignHCenter)

        self.editLineContainer = QFrame(self.frame_14)
        self.editLineContainer.setObjectName(u"editLineContainer")
        sizePolicy9.setHeightForWidth(self.editLineContainer.sizePolicy().hasHeightForWidth())
        self.editLineContainer.setSizePolicy(sizePolicy9)
        self.editLineContainer.setMaximumSize(QSize(16777215, 0))
        self.editLineContainer.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	color: rgb(66, 66, 66);\n"
"}")
        self.editLineContainer.setFrameShape(QFrame.StyledPanel)
        self.editLineContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.editLineContainer)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.editLineContainer)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_37)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lineNameUpdate = QLineEdit(self.frame_38)
        self.lineNameUpdate.setObjectName(u"lineNameUpdate")
        sizePolicy6.setHeightForWidth(self.lineNameUpdate.sizePolicy().hasHeightForWidth())
        self.lineNameUpdate.setSizePolicy(sizePolicy6)

        self.horizontalLayout_31.addWidget(self.lineNameUpdate)


        self.verticalLayout_45.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lineIPUpdate = QLineEdit(self.frame_39)
        self.lineIPUpdate.setObjectName(u"lineIPUpdate")
        sizePolicy6.setHeightForWidth(self.lineIPUpdate.sizePolicy().hasHeightForWidth())
        self.lineIPUpdate.setSizePolicy(sizePolicy6)

        self.horizontalLayout_32.addWidget(self.lineIPUpdate)


        self.verticalLayout_45.addWidget(self.frame_39)


        self.horizontalLayout_33.addWidget(self.frame_37)

        self.frame_40 = QFrame(self.editLineContainer)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy10.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy10)
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_40)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.editLineConfirmBtn = QPushButton(self.frame_40)
        self.editLineConfirmBtn.setObjectName(u"editLineConfirmBtn")
        self.editLineConfirmBtn.setMinimumSize(QSize(150, 50))
        self.editLineConfirmBtn.setMaximumSize(QSize(150, 16777215))
        self.editLineConfirmBtn.setStyleSheet(u"")

        self.verticalLayout_46.addWidget(self.editLineConfirmBtn)

        self.editLineCanselBtn = QPushButton(self.frame_40)
        self.editLineCanselBtn.setObjectName(u"editLineCanselBtn")
        self.editLineCanselBtn.setMinimumSize(QSize(0, 50))
        self.editLineCanselBtn.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_46.addWidget(self.editLineCanselBtn)


        self.horizontalLayout_33.addWidget(self.frame_40)


        self.verticalLayout_36.addWidget(self.editLineContainer)

        self.addLineContainer = QFrame(self.frame_14)
        self.addLineContainer.setObjectName(u"addLineContainer")
        self.addLineContainer.setMaximumSize(QSize(16777215, 0))
        self.addLineContainer.setFrameShape(QFrame.StyledPanel)
        self.addLineContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.addLineContainer)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.addLineContainer)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_24)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lineNameEdit = QLineEdit(self.frame_25)
        self.lineNameEdit.setObjectName(u"lineNameEdit")
        sizePolicy6.setHeightForWidth(self.lineNameEdit.sizePolicy().hasHeightForWidth())
        self.lineNameEdit.setSizePolicy(sizePolicy6)

        self.horizontalLayout_17.addWidget(self.lineNameEdit)


        self.verticalLayout_38.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lineIPEdit = QLineEdit(self.frame_26)
        self.lineIPEdit.setObjectName(u"lineIPEdit")
        sizePolicy6.setHeightForWidth(self.lineIPEdit.sizePolicy().hasHeightForWidth())
        self.lineIPEdit.setSizePolicy(sizePolicy6)

        self.horizontalLayout_18.addWidget(self.lineIPEdit)


        self.verticalLayout_38.addWidget(self.frame_26)


        self.horizontalLayout_20.addWidget(self.frame_24, 0, Qt.AlignVCenter)

        self.frame_28 = QFrame(self.addLineContainer)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy10.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy10)
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_28)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.addLineConfirmBtn = QPushButton(self.frame_28)
        self.addLineConfirmBtn.setObjectName(u"addLineConfirmBtn")
        self.addLineConfirmBtn.setMinimumSize(QSize(150, 50))
        self.addLineConfirmBtn.setMaximumSize(QSize(150, 16777215))
        self.addLineConfirmBtn.setStyleSheet(u"")

        self.verticalLayout_39.addWidget(self.addLineConfirmBtn)

        self.addLineCanselBtn = QPushButton(self.frame_28)
        self.addLineCanselBtn.setObjectName(u"addLineCanselBtn")
        self.addLineCanselBtn.setMinimumSize(QSize(0, 50))
        self.addLineCanselBtn.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_39.addWidget(self.addLineCanselBtn)


        self.horizontalLayout_20.addWidget(self.frame_28)


        self.verticalLayout_36.addWidget(self.addLineContainer)


        self.verticalLayout_31.addWidget(self.frame_14)


        self.horizontalLayout_8.addWidget(self.addLine_Frame)

        self.stackedWidget.addWidget(self.settingPage)
        self.searchePage = QWidget()
        self.searchePage.setObjectName(u"searchePage")
        self.searchePage.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	text-align: center;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 246, 250);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	border-bottom: 0px solid rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(66, 66, 66);\n"
"	border-color: rgb(36, 149, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(245, 246, 250);\n"
"	text-align: center;\n"
"}\n"
"QTableWidg"
                        "et::item:selected{\n"
"	background-color: rgb(36, 149, 255);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color: rgb(66, 66, 66);\n"
"	background-color: rgb(36, 149, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(36, 149, 255);\n"
"	background-color: rgb(36, 149, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;}\n"
"\n"
"/*LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(245, 246, 250);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLine"
                        "Edit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.verticalLayout_52 = QVBoxLayout(self.searchePage)
        self.verticalLayout_52.setSpacing(6)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(-1, -1, -1, 9)
        self.searchFrame = QFrame(self.searchePage)
        self.searchFrame.setObjectName(u"searchFrame")
        sizePolicy.setHeightForWidth(self.searchFrame.sizePolicy().hasHeightForWidth())
        self.searchFrame.setSizePolicy(sizePolicy)
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.searchFrame)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_47 = QFrame(self.searchFrame)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_47)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(10, 0, 0, 0)
        self.label_9 = QLabel(self.frame_47)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_54.addWidget(self.label_9)


        self.verticalLayout_53.addWidget(self.frame_47, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_48 = QFrame(self.searchFrame)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy9.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy9)
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.searchLine = QLineEdit(self.frame_48)
        self.searchLine.setObjectName(u"searchLine")
        self.searchLine.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_25.addWidget(self.searchLine)

        self.startSearchBtn = QPushButton(self.frame_48)
        self.startSearchBtn.setObjectName(u"startSearchBtn")
        self.startSearchBtn.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_25.addWidget(self.startSearchBtn)

        self.advancedSearchBtn = QPushButton(self.frame_48)
        self.advancedSearchBtn.setObjectName(u"advancedSearchBtn")
        self.advancedSearchBtn.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_25.addWidget(self.advancedSearchBtn)


        self.verticalLayout_53.addWidget(self.frame_48)

        self.advancedSearch_container = QFrame(self.searchFrame)
        self.advancedSearch_container.setObjectName(u"advancedSearch_container")
        sizePolicy2.setHeightForWidth(self.advancedSearch_container.sizePolicy().hasHeightForWidth())
        self.advancedSearch_container.setSizePolicy(sizePolicy2)
        self.advancedSearch_container.setMinimumSize(QSize(0, 0))
        self.advancedSearch_container.setMaximumSize(QSize(16777215, 0))
        self.advancedSearch_container.setFrameShape(QFrame.StyledPanel)
        self.advancedSearch_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.advancedSearch_container)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.archive_checkBox = QCheckBox(self.advancedSearch_container)
        self.archive_checkBox.setObjectName(u"archive_checkBox")
        self.archive_checkBox.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_55.addWidget(self.archive_checkBox)


        self.verticalLayout_53.addWidget(self.advancedSearch_container, 0, Qt.AlignTop)


        self.verticalLayout_52.addWidget(self.searchFrame, 0, Qt.AlignTop)

        self.RollcodeResult_container = QFrame(self.searchePage)
        self.RollcodeResult_container.setObjectName(u"RollcodeResult_container")
        sizePolicy2.setHeightForWidth(self.RollcodeResult_container.sizePolicy().hasHeightForWidth())
        self.RollcodeResult_container.setSizePolicy(sizePolicy2)
        self.RollcodeResult_container.setMinimumSize(QSize(0, 0))
        self.RollcodeResult_container.setMaximumSize(QSize(16777215, 0))
        self.RollcodeResult_container.setFrameShape(QFrame.StyledPanel)
        self.RollcodeResult_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.RollcodeResult_container)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_59 = QFrame(self.RollcodeResult_container)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy2.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy2)
        self.frame_59.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(10, 0, 0, 0)
        self.label_14 = QLabel(self.frame_59)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_34.addWidget(self.label_14, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_40.addWidget(self.frame_59)

        self.frame_58 = QFrame(self.RollcodeResult_container)
        self.frame_58.setObjectName(u"frame_58")
        sizePolicy.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy)
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_58)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.RollSearchData_Tab = QTableWidget(self.frame_58)
        if (self.RollSearchData_Tab.columnCount() < 3):
            self.RollSearchData_Tab.setColumnCount(3)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setFont(font5);
        self.RollSearchData_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setFont(font5);
        self.RollSearchData_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setFont(font5);
        self.RollSearchData_Tab.setHorizontalHeaderItem(2, __qtablewidgetitem72)
        if (self.RollSearchData_Tab.rowCount() < 1):
            self.RollSearchData_Tab.setRowCount(1)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem73.setFont(font6);
        self.RollSearchData_Tab.setItem(0, 0, __qtablewidgetitem73)
        self.RollSearchData_Tab.setObjectName(u"RollSearchData_Tab")
        sizePolicy3.setHeightForWidth(self.RollSearchData_Tab.sizePolicy().hasHeightForWidth())
        self.RollSearchData_Tab.setSizePolicy(sizePolicy3)
        self.RollSearchData_Tab.setMaximumSize(QSize(16777215, 100))
        self.RollSearchData_Tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.RollSearchData_Tab.setSelectionMode(QAbstractItemView.NoSelection)
        self.RollSearchData_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.RollSearchData_Tab.setShowGrid(True)
        self.RollSearchData_Tab.setSortingEnabled(False)
        self.RollSearchData_Tab.setRowCount(1)
        self.RollSearchData_Tab.setColumnCount(3)
        self.RollSearchData_Tab.horizontalHeader().setVisible(True)
        self.RollSearchData_Tab.horizontalHeader().setCascadingSectionResizes(False)
        self.RollSearchData_Tab.horizontalHeader().setMinimumSectionSize(50)
        self.RollSearchData_Tab.horizontalHeader().setDefaultSectionSize(130)
        self.RollSearchData_Tab.horizontalHeader().setHighlightSections(False)
        self.RollSearchData_Tab.horizontalHeader().setStretchLastSection(False)
        self.RollSearchData_Tab.verticalHeader().setVisible(False)
        self.RollSearchData_Tab.verticalHeader().setMinimumSectionSize(35)
        self.RollSearchData_Tab.verticalHeader().setDefaultSectionSize(35)
        self.RollSearchData_Tab.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_62.addWidget(self.RollSearchData_Tab, 0, Qt.AlignTop)


        self.verticalLayout_40.addWidget(self.frame_58)


        self.verticalLayout_52.addWidget(self.RollcodeResult_container, 0, Qt.AlignBottom)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_8)

        self.BatchResult_Container = QFrame(self.searchePage)
        self.BatchResult_Container.setObjectName(u"BatchResult_Container")
        sizePolicy.setHeightForWidth(self.BatchResult_Container.sizePolicy().hasHeightForWidth())
        self.BatchResult_Container.setSizePolicy(sizePolicy)
        self.BatchResult_Container.setMinimumSize(QSize(0, 0))
        self.BatchResult_Container.setMaximumSize(QSize(16777215, 0))
        self.BatchResult_Container.setFrameShape(QFrame.StyledPanel)
        self.BatchResult_Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.BatchResult_Container)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_52 = QFrame(self.BatchResult_Container)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(10, 0, 0, 0)
        self.label_10 = QLabel(self.frame_52)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_39.addWidget(self.label_10, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_56.addWidget(self.frame_52, 0, Qt.AlignTop)

        self.frame_53 = QFrame(self.BatchResult_Container)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy)
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_53)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.batchData_Tab_2 = QTableWidget(self.frame_53)
        if (self.batchData_Tab_2.columnCount() < 10):
            self.batchData_Tab_2.setColumnCount(10)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(2, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(3, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(4, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(5, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(6, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(7, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(8, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setFont(font5);
        self.batchData_Tab_2.setHorizontalHeaderItem(9, __qtablewidgetitem83)
        if (self.batchData_Tab_2.rowCount() < 1):
            self.batchData_Tab_2.setRowCount(1)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem84.setFont(font6);
        self.batchData_Tab_2.setItem(0, 1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab_2.setItem(0, 2, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab_2.setItem(0, 3, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab_2.setItem(0, 4, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        self.batchData_Tab_2.setItem(0, 5, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem89.setFont(font6);
        self.batchData_Tab_2.setItem(0, 7, __qtablewidgetitem89)
        self.batchData_Tab_2.setObjectName(u"batchData_Tab_2")
        sizePolicy1.setHeightForWidth(self.batchData_Tab_2.sizePolicy().hasHeightForWidth())
        self.batchData_Tab_2.setSizePolicy(sizePolicy1)
        self.batchData_Tab_2.setMaximumSize(QSize(16777215, 100))
        self.batchData_Tab_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.batchData_Tab_2.setSelectionMode(QAbstractItemView.NoSelection)
        self.batchData_Tab_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.batchData_Tab_2.setShowGrid(True)
        self.batchData_Tab_2.setSortingEnabled(False)
        self.batchData_Tab_2.setRowCount(1)
        self.batchData_Tab_2.setColumnCount(10)
        self.batchData_Tab_2.horizontalHeader().setVisible(True)
        self.batchData_Tab_2.horizontalHeader().setCascadingSectionResizes(False)
        self.batchData_Tab_2.horizontalHeader().setMinimumSectionSize(50)
        self.batchData_Tab_2.horizontalHeader().setDefaultSectionSize(130)
        self.batchData_Tab_2.horizontalHeader().setHighlightSections(False)
        self.batchData_Tab_2.horizontalHeader().setStretchLastSection(True)
        self.batchData_Tab_2.verticalHeader().setVisible(False)
        self.batchData_Tab_2.verticalHeader().setMinimumSectionSize(35)
        self.batchData_Tab_2.verticalHeader().setDefaultSectionSize(35)
        self.batchData_Tab_2.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_59.addWidget(self.batchData_Tab_2, 0, Qt.AlignTop)


        self.verticalLayout_56.addWidget(self.frame_53)


        self.verticalLayout_52.addWidget(self.BatchResult_Container, 0, Qt.AlignBottom)

        self.AggregatResult_container = QFrame(self.searchePage)
        self.AggregatResult_container.setObjectName(u"AggregatResult_container")
        sizePolicy.setHeightForWidth(self.AggregatResult_container.sizePolicy().hasHeightForWidth())
        self.AggregatResult_container.setSizePolicy(sizePolicy)
        self.AggregatResult_container.setMinimumSize(QSize(0, 0))
        self.AggregatResult_container.setMaximumSize(QSize(16777215, 0))
        self.AggregatResult_container.setFrameShape(QFrame.StyledPanel)
        self.AggregatResult_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.AggregatResult_container)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_54 = QFrame(self.AggregatResult_container)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(10, 0, 0, 0)
        self.label_11 = QLabel(self.frame_54)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_38.addWidget(self.label_11, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_57.addWidget(self.frame_54, 0, Qt.AlignTop)

        self.frame_55 = QFrame(self.AggregatResult_container)
        self.frame_55.setObjectName(u"frame_55")
        sizePolicy.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy)
        self.frame_55.setMinimumSize(QSize(0, 300))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_55)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.aggSearchData_Tab = QTableWidget(self.frame_55)
        if (self.aggSearchData_Tab.columnCount() < 4):
            self.aggSearchData_Tab.setColumnCount(4)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setFont(font5);
        self.aggSearchData_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setFont(font5);
        self.aggSearchData_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setFont(font5);
        self.aggSearchData_Tab.setHorizontalHeaderItem(2, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setFont(font5);
        self.aggSearchData_Tab.setHorizontalHeaderItem(3, __qtablewidgetitem93)
        if (self.aggSearchData_Tab.rowCount() < 20):
            self.aggSearchData_Tab.setRowCount(20)
        self.aggSearchData_Tab.setObjectName(u"aggSearchData_Tab")
        sizePolicy3.setHeightForWidth(self.aggSearchData_Tab.sizePolicy().hasHeightForWidth())
        self.aggSearchData_Tab.setSizePolicy(sizePolicy3)
        self.aggSearchData_Tab.setMinimumSize(QSize(0, 700))
        self.aggSearchData_Tab.setMaximumSize(QSize(16777215, 700))
        self.aggSearchData_Tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.aggSearchData_Tab.setSelectionMode(QAbstractItemView.NoSelection)
        self.aggSearchData_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.aggSearchData_Tab.setShowGrid(True)
        self.aggSearchData_Tab.setSortingEnabled(False)
        self.aggSearchData_Tab.setRowCount(20)
        self.aggSearchData_Tab.setColumnCount(4)
        self.aggSearchData_Tab.horizontalHeader().setVisible(True)
        self.aggSearchData_Tab.horizontalHeader().setCascadingSectionResizes(False)
        self.aggSearchData_Tab.horizontalHeader().setMinimumSectionSize(30)
        self.aggSearchData_Tab.horizontalHeader().setDefaultSectionSize(130)
        self.aggSearchData_Tab.horizontalHeader().setHighlightSections(False)
        self.aggSearchData_Tab.horizontalHeader().setStretchLastSection(True)
        self.aggSearchData_Tab.verticalHeader().setVisible(False)
        self.aggSearchData_Tab.verticalHeader().setMinimumSectionSize(30)
        self.aggSearchData_Tab.verticalHeader().setDefaultSectionSize(30)
        self.aggSearchData_Tab.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_60.addWidget(self.aggSearchData_Tab, 0, Qt.AlignTop)


        self.verticalLayout_57.addWidget(self.frame_55)


        self.verticalLayout_52.addWidget(self.AggregatResult_container, 0, Qt.AlignBottom)

        self.KIresult_container = QFrame(self.searchePage)
        self.KIresult_container.setObjectName(u"KIresult_container")
        self.KIresult_container.setMinimumSize(QSize(0, 0))
        self.KIresult_container.setMaximumSize(QSize(16777215, 0))
        self.KIresult_container.setFrameShape(QFrame.StyledPanel)
        self.KIresult_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.KIresult_container)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_57 = QFrame(self.KIresult_container)
        self.frame_57.setObjectName(u"frame_57")
        sizePolicy2.setHeightForWidth(self.frame_57.sizePolicy().hasHeightForWidth())
        self.frame_57.setSizePolicy(sizePolicy2)
        self.frame_57.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"	font: 20pt \"Segoe UI\";")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(10, 0, 0, 0)
        self.label_13 = QLabel(self.frame_57)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_26.addWidget(self.label_13, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_58.addWidget(self.frame_57, 0, Qt.AlignTop)

        self.frame_56 = QFrame(self.KIresult_container)
        self.frame_56.setObjectName(u"frame_56")
        sizePolicy.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy)
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_56)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.KiSearchData_Tab = QTableWidget(self.frame_56)
        if (self.KiSearchData_Tab.columnCount() < 8):
            self.KiSearchData_Tab.setColumnCount(8)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setFont(font5);
        self.KiSearchData_Tab.setHorizontalHeaderItem(0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setFont(font5);
        self.KiSearchData_Tab.setHorizontalHeaderItem(1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setFont(font5);
        self.KiSearchData_Tab.setHorizontalHeaderItem(2, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setFont(font5);
        self.KiSearchData_Tab.setHorizontalHeaderItem(3, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setFont(font5);
        self.KiSearchData_Tab.setHorizontalHeaderItem(4, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setFont(font5);
        self.KiSearchData_Tab.setHorizontalHeaderItem(5, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setFont(font5);
        self.KiSearchData_Tab.setHorizontalHeaderItem(6, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setFont(font5);
        self.KiSearchData_Tab.setHorizontalHeaderItem(7, __qtablewidgetitem101)
        if (self.KiSearchData_Tab.rowCount() < 1):
            self.KiSearchData_Tab.setRowCount(1)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem102.setFont(font6);
        self.KiSearchData_Tab.setItem(0, 3, __qtablewidgetitem102)
        self.KiSearchData_Tab.setObjectName(u"KiSearchData_Tab")
        sizePolicy3.setHeightForWidth(self.KiSearchData_Tab.sizePolicy().hasHeightForWidth())
        self.KiSearchData_Tab.setSizePolicy(sizePolicy3)
        self.KiSearchData_Tab.setMaximumSize(QSize(16777215, 100))
        self.KiSearchData_Tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.KiSearchData_Tab.setSelectionMode(QAbstractItemView.NoSelection)
        self.KiSearchData_Tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.KiSearchData_Tab.setShowGrid(True)
        self.KiSearchData_Tab.setSortingEnabled(False)
        self.KiSearchData_Tab.setRowCount(1)
        self.KiSearchData_Tab.setColumnCount(8)
        self.KiSearchData_Tab.horizontalHeader().setVisible(True)
        self.KiSearchData_Tab.horizontalHeader().setCascadingSectionResizes(False)
        self.KiSearchData_Tab.horizontalHeader().setMinimumSectionSize(50)
        self.KiSearchData_Tab.horizontalHeader().setDefaultSectionSize(130)
        self.KiSearchData_Tab.horizontalHeader().setHighlightSections(False)
        self.KiSearchData_Tab.horizontalHeader().setProperty("showSortIndicator", False)
        self.KiSearchData_Tab.horizontalHeader().setStretchLastSection(True)
        self.KiSearchData_Tab.verticalHeader().setVisible(False)
        self.KiSearchData_Tab.verticalHeader().setMinimumSectionSize(35)
        self.KiSearchData_Tab.verticalHeader().setDefaultSectionSize(35)
        self.KiSearchData_Tab.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_61.addWidget(self.KiSearchData_Tab, 0, Qt.AlignTop)


        self.verticalLayout_58.addWidget(self.frame_56)


        self.verticalLayout_52.addWidget(self.KIresult_container, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.searchePage)

        self.verticalLayout_16.addWidget(self.stackedWidget)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 20))
        self.bottomBar.setFrameShape(QFrame.StyledPanel)
        self.bottomBar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.bottomBar)


        self.verticalLayout_15.addWidget(self.contentBottom)

        self.contentBottom.raise_()
        self.topCentralContainer.raise_()

        self.horizontalLayout.addWidget(self.centralMenuContainer)


        self.verticalLayout.addWidget(self.MainContainer)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.loginForm.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(2)
        self.comboBox.setCurrentIndex(-1)
        self.toolBox_2.setCurrentIndex(0)
        self.template_combobox.setCurrentIndex(-1)
        self.template_combobox_2.setCurrentIndex(-1)
        self.template_combobox_3.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.userButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"    \u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
        self.createOrderButton.setText(QCoreApplication.translate("MainWindow", u"    \u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.ordersButton.setText(QCoreApplication.translate("MainWindow", u"    \u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.lineButton.setText(QCoreApplication.translate("MainWindow", u"    \u041b\u0438\u043d\u0438\u0438", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"    \u041f\u043e\u0438\u0441\u043a", None))
        self.printFrameButton.setText(QCoreApplication.translate("MainWindow", u"    \u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.rollFrameButton.setText(QCoreApplication.translate("MainWindow", u"    \u0420\u0443\u043b\u043e\u043d\u044b", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"    \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.closeAccButton.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.changeWindowLogButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.changeWindowRegButton.setText(QCoreApplication.translate("MainWindow", u"\u043a \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.titleRightInfo.setText("")
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        ___qtablewidgetitem = self.lineData_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0438\u044f", None));
        ___qtablewidgetitem1 = self.lineData_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None));
        self.refreshLineButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        ___qtablewidgetitem2 = self.batchOnLine_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437", None));
        ___qtablewidgetitem3 = self.batchOnLine_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0432\u0442\u043e", None));
        ___qtablewidgetitem4 = self.batchOnLine_Tab.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0438\u0442\u0430\u043d\u043e", None));
        ___qtablewidgetitem5 = self.batchOnLine_Tab.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0431\u0440\u0430\u043a\u043e\u0432\u0430\u043d\u043e", None));
        ___qtablewidgetitem6 = self.batchOnLine_Tab.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        self.New_lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d ", None))
        self.New_lineEdit.setPlaceholderText("")
        self.Work_lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435  ", None))
        self.Work_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435", None))
        self.End_lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d ", None))
        self.End_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d", None))
        self.deleteOrderButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.closeOrderButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u043b\u043e\u043d\u044b", None))
        self.rollCode_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0440\u0443\u043b\u043e\u043d\u0430", None))
        self.rollButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        ___qtablewidgetitem7 = self.rollTable.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem8 = self.rollTable.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438", None));
        ___qtablewidgetitem9 = self.rollTable.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem10 = self.rollTable.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0440\u0443\u043b\u043e\u043d\u0430", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.startCreateButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.startOrdersButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.startLineButton.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0438\u0438", None))
        self.startSearchButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.serchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0437\u0430\u043a\u0430\u0437\u0430", None))
        ___qtablewidgetitem11 = self.activOrder_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem12 = self.activOrder_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437", None));
        ___qtablewidgetitem13 = self.activOrder_Tab.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem14 = self.activOrder_Tab.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u0436\u0438\u0437\u043d\u0438", None));
        self.refreshBatch_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.printHouse_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b: \u0422\u0438\u043f\u043e\u0433\u0440\u0430\u0444\u0438\u044f", None))
        self.mabufacture_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b: \u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e", None))
        ___qtablewidgetitem15 = self.batchData_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem16 = self.batchData_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u0438\u044f", None));
        ___qtablewidgetitem17 = self.batchData_Tab.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e", None));
        ___qtablewidgetitem18 = self.batchData_Tab.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c", None));
        ___qtablewidgetitem19 = self.batchData_Tab.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043d\u0435\u0441\u0435\u043d\u043e", None));
        ___qtablewidgetitem20 = self.batchData_Tab.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u044b\u0445", None));
        ___qtablewidgetitem21 = self.batchData_Tab.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u0430\u043a", None));
        ___qtablewidgetitem22 = self.batchData_Tab.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None));
        ___qtablewidgetitem23 = self.batchData_Tab.horizontalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u0433\u043e\u0434\u043d\u043e\u0441\u0442\u0438 \u041a\u041c", None));
        ___qtablewidgetitem24 = self.batchData_Tab.horizontalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None));

        __sortingEnabled = self.batchData_Tab.isSortingEnabled()
        self.batchData_Tab.setSortingEnabled(False)
        self.batchData_Tab.setSortingEnabled(__sortingEnabled)

        self.closeBatch_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.deleteBatch_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.showKM_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u041a\u041c", None))
        self.showKITU.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u041a\u0418\u0413\u0423", None))
        self.sendBatchOnLine_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u043b\u0438\u043d\u0438\u044e", None))
        self.exportBatch_btn.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.printButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.KITUsendPrint_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c", None))
        ___qtablewidgetitem25 = self.orderKITU_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem26 = self.orderKITU_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u043e\u0439 \u043a\u043e\u0434", None));
        ___qtablewidgetitem27 = self.orderKITU_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem28 = self.ki_from_KITU_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem29 = self.ki_from_KITU_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438", None));
        ___qtablewidgetitem30 = self.ki_from_KITU_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem31 = self.sendLine_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem32 = self.sendLine_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem33 = self.sendLine_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None));
        self.sendOrder_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.canselOrder_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        ___qtablewidgetitem34 = self.orderKM_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem35 = self.orderKM_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem36 = self.orderKM_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem37 = self.orderKM_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438", None));
        ___qtablewidgetitem38 = self.orderKM_tab.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem39 = self.orderKM_tab.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434  \u0440\u0443\u043b\u043e\u043d\u0430", None));
        ___qtablewidgetitem40 = self.orderKM_tab.horizontalHeaderItem(6)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0430\u0433\u0433\u0440\u0435\u0433\u0430\u0442\u0430", None));
        ___qtablewidgetitem41 = self.orderKM_tab.horizontalHeaderItem(7)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u0430", None));
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.createOrderBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u044b\u0435 \u0437\u0430\u043a\u0430\u0437\u044b", None))
        ___qtablewidgetitem42 = self.lastOrder_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem43 = self.lastOrder_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem44 = self.lastOrder_Tab.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem45 = self.lastOrder_Tab.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"GTIN", None));
        ___qtablewidgetitem46 = self.lastOrder_Tab.horizontalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        self.startPrint_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.allPrint_rbtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0432\u0441\u0435\u0445 \u044d\u0442\u0438\u043a\u0435\u0442\u043e\u043a", None))
        self.countPrint_rbtn.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u044d\u0442\u0438\u043a\u0435\u0442\u043e\u043a", None))
        self.countPrint_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u044d\u0442\u0438\u043a\u0435\u0442\u043e\u043a", None))
        self.save_rbtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0444\u0430\u0439\u043b", None))
        self.saveCodeInFile_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem47 = self.kmPrint_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem48 = self.kmPrint_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438", None));
        ___qtablewidgetitem49 = self.kmPrint_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        self.allCountLabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e \u0434\u043b\u044f \u043f\u0435\u0447\u0430\u0442\u0438 \u044d\u0442\u0438\u043a\u0435\u0442\u043e\u043a: ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u044d\u0442\u0438\u043a\u0435\u0442\u043e\u043a \u0434\u043b\u044f \u043f\u0435\u0447\u0430\u0442\u0438", None))
        self.startLabelPrint_Edit.setInputMask("")
        self.startLabelPrint_Edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e \u043f\u0435\u0447\u0430\u0442\u0438", None))
        self.endLabelPrint_Edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0446 \u043f\u0435\u0447\u0430\u0442\u0438", None))
        ___qtablewidgetitem50 = self.listPrinter_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem51 = self.listPrinter_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0442\u0435\u0440", None));
        ___qtablewidgetitem52 = self.listPrinter_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        self.Label_8.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435:", None))
        self.selectedBatchForPrint_label.setText(QCoreApplication.translate("MainWindow", u"\"\"", None))
        self.Label_9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.SelectedNameForPrint_label.setText(QCoreApplication.translate("MainWindow", u"\"\"", None))
        self.selectedImageDM.setText(QCoreApplication.translate("MainWindow", u"DataMatrix", None))
        self.Label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435:", None))
        self.batchForPrint_label_1.setText("")
        self.Label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.nameForPrint_label_1.setText("")
        self.imageDM_printer_1.setText(QCoreApplication.translate("MainWindow", u"DataMatrix", None))
        self.rollNumberEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0440\u0443\u043b\u043e\u043d\u0430", None))
        self.dateEdit_1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.template_combobox.setCurrentText("")
        self.template_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.pausePrint_btn_1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.endPrint_btn_1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.Label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e \u043d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c:", None))
        self.countFromPrint_line_1.setPlaceholderText("")
        self.Label_11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043c\u0435\u0440\u0430", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.printer1_page), QCoreApplication.translate("MainWindow", u"Novex 64-04", None))
        self.Label_6.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435:", None))
        self.batchForPrint_label_2.setText("")
        self.Label_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.nameForPrint_label_2.setText("")
        self.imageDM_printer_2.setText(QCoreApplication.translate("MainWindow", u"DataMatrix", None))
        self.rollNumberEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0440\u0443\u043b\u043e\u043d\u0430", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.template_combobox_2.setCurrentText("")
        self.template_combobox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.pausePrint_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.endPrint_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.Label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e \u043d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c:", None))
        self.countFromPrint_line_2.setPlaceholderText("")
        self.Label_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043c\u0435\u0440\u0430", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.printer2_page), QCoreApplication.translate("MainWindow", u"Novex 64-06", None))
        self.Label_12.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435:", None))
        self.batchForPrint_label_3.setText("")
        self.Label_13.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.nameForPrint_label_3.setText("")
        self.imageDM_printer_3.setText(QCoreApplication.translate("MainWindow", u"DataMatrix", None))
        self.rollNumberEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0440\u0443\u043b\u043e\u043d\u0430", None))
        self.dateEdit_3.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.template_combobox_3.setCurrentText("")
        self.template_combobox_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.pausePrint_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.endPrint_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.Label_14.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e \u043d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c:", None))
        self.countFromPrint_line_3.setPlaceholderText("")
        self.Label_15.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043c\u0435\u0440\u0430", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.printer3_page), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0442\u0435\u0440 \u043d\u0435 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430", None))
        ___qtablewidgetitem53 = self.currentProd_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem54 = self.currentProd_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442", None));
        ___qtablewidgetitem55 = self.currentProd_Tab.horizontalHeaderItem(2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"GTIN", None));
        ___qtablewidgetitem56 = self.currentProd_Tab.horizontalHeaderItem(3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0432\u0442\u043e", None));
        self.addProductBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.editProductBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.deleteProductBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.productNameUpdate.setInputMask("")
        self.productNameUpdate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430", None))
        self.productGTINeditUpdate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"GTIN", None))
        self.productCountEditUpdate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432 \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0435", None))
        self.updateProductConfirmBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.updateProductCanselBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.productNameEdit.setInputMask("")
        self.productNameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430", None))
        self.productGTINedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"GTIN", None))
        self.productCountEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432 \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0435", None))
        self.addProductConfirmBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.addProductCanselBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043b\u0438\u043d\u0438\u0438", None))
        ___qtablewidgetitem57 = self.currentLine_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem58 = self.currentLine_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0438\u044f", None));
        ___qtablewidgetitem59 = self.currentLine_Tab.horizontalHeaderItem(2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"IP \u0410\u0434\u0440\u0435\u0441", None));
        self.addLineBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.editLineBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.deleteLineBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.lineNameUpdate.setInputMask("")
        self.lineNameUpdate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u043d\u0438\u0438", None))
        self.lineIPUpdate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP \u0430\u0434\u0440\u0435\u0441", None))
        self.editLineConfirmBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.editLineCanselBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.lineNameEdit.setInputMask("")
        self.lineNameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u043d\u0438\u0438", None))
        self.lineIPEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP \u0430\u0434\u0440\u0435\u0441", None))
        self.addLineConfirmBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.addLineCanselBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.startSearchBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.advancedSearchBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439", None))
        self.archive_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0432 \u0430\u0440\u0445\u0438\u0432\u0435", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0440\u0443\u043b\u043b\u043e\u043d\u0430", None))
        ___qtablewidgetitem60 = self.RollSearchData_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u0438\u044f", None));
        ___qtablewidgetitem61 = self.RollSearchData_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0440\u0443\u043b\u043e\u043d\u0430", None));
        ___qtablewidgetitem62 = self.RollSearchData_Tab.horizontalHeaderItem(2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u041a\u041c", None));

        __sortingEnabled1 = self.RollSearchData_Tab.isSortingEnabled()
        self.RollSearchData_Tab.setSortingEnabled(False)
        self.RollSearchData_Tab.setSortingEnabled(__sortingEnabled1)

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437", None))
        ___qtablewidgetitem63 = self.batchData_Tab_2.horizontalHeaderItem(0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem64 = self.batchData_Tab_2.horizontalHeaderItem(1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u0438\u044f", None));
        ___qtablewidgetitem65 = self.batchData_Tab_2.horizontalHeaderItem(2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e", None));
        ___qtablewidgetitem66 = self.batchData_Tab_2.horizontalHeaderItem(3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c", None));
        ___qtablewidgetitem67 = self.batchData_Tab_2.horizontalHeaderItem(4)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043d\u0435\u0441\u0435\u043d\u043e", None));
        ___qtablewidgetitem68 = self.batchData_Tab_2.horizontalHeaderItem(5)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u044b\u0445", None));
        ___qtablewidgetitem69 = self.batchData_Tab_2.horizontalHeaderItem(6)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u0430\u043a", None));
        ___qtablewidgetitem70 = self.batchData_Tab_2.horizontalHeaderItem(7)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None));
        ___qtablewidgetitem71 = self.batchData_Tab_2.horizontalHeaderItem(8)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u0433\u043e\u0434\u043d\u043e\u0441\u0442\u0438 \u041a\u041c", None));
        ___qtablewidgetitem72 = self.batchData_Tab_2.horizontalHeaderItem(9)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None));

        __sortingEnabled2 = self.batchData_Tab_2.isSortingEnabled()
        self.batchData_Tab_2.setSortingEnabled(False)
        self.batchData_Tab_2.setSortingEnabled(__sortingEnabled2)

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0433\u0433\u0440\u0435\u0433\u0430\u0442", None))
        ___qtablewidgetitem73 = self.aggSearchData_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem74 = self.aggSearchData_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u0438\u044f", None));
        ___qtablewidgetitem75 = self.aggSearchData_Tab.horizontalHeaderItem(2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0418\u0413\u0423", None));
        ___qtablewidgetitem76 = self.aggSearchData_Tab.horizontalHeaderItem(3)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041c", None))
        ___qtablewidgetitem77 = self.KiSearchData_Tab.horizontalHeaderItem(0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem78 = self.KiSearchData_Tab.horizontalHeaderItem(1)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem79 = self.KiSearchData_Tab.horizontalHeaderItem(2)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u0433\u043e\u0434\u043d\u043e\u0441\u0442\u0438 \u041a\u041c", None));
        ___qtablewidgetitem80 = self.KiSearchData_Tab.horizontalHeaderItem(3)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u0438\u044f", None));
        ___qtablewidgetitem81 = self.KiSearchData_Tab.horizontalHeaderItem(4)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0430\u0433\u0433\u0440\u0435\u0433\u0430\u0442\u0430", None));
        ___qtablewidgetitem82 = self.KiSearchData_Tab.horizontalHeaderItem(5)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0440\u0443\u043b\u043e\u043d\u0430", None));
        ___qtablewidgetitem83 = self.KiSearchData_Tab.horizontalHeaderItem(6)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem84 = self.KiSearchData_Tab.horizontalHeaderItem(7)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041c", None));

        __sortingEnabled3 = self.KiSearchData_Tab.isSortingEnabled()
        self.KiSearchData_Tab.setSortingEnabled(False)
        self.KiSearchData_Tab.setSortingEnabled(__sortingEnabled3)

    # retranslateUi

