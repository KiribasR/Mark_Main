from main import *
from modules import ui_settings


# GLOBALS
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    def returStatus(self):
        return GLOBAL_STATE

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        if ui_settings.Settings.ENABLE_CUSTOM_TITLE_BAR:
            # STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

            self.ui.titleRightInfo.mouseMoveEvent = moveWindow


        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        """self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)"""

        # RESIZE WINDOW
        #self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        #self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        """# MINIMIZE
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.restoreButton.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeButton.clicked.connect(lambda: self.close())"""



    def resize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restoreButton.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
        else:
            self.showMaximized()
            self.ui.restoreButton.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))

    #Переключатель расширения левого меню
    def toggleMenu(self):
        enable = True
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuContainer.width()
            maxExtend = ui_settings.Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuContainer, b"minimumWidth")
            self.animation.setDuration(ui_settings.Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # Переключатель расширения окна КМ при выборе КИТУ

    def ki_Window(self):
        enable = True
        if enable:
            # GET WIDTH
            width = self.ui.KI_from_KITU_Container.width()
            maxExtend = 550
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.KI_from_KITU_Container, b"minimumWidth")
            self.animation.setDuration(ui_settings.Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # Переключатель расширенного поиска
    def advancedSearchMenu(self):
        enable = True
        print('сработал')
        if enable:
            # GET WIDTH
            height = self.ui.advancedSearch_container.height()
            maxExtend = ui_settings.Settings.ADVANCE_SEARCH_HEIGHT
            standard = 0

            # SET MAX WIDTH
            if height == 0:
                heightExtended = maxExtend
            else:
                heightExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.advancedSearch_container, b"minimumHeight")
            self.animation.setDuration(ui_settings.Settings.TIME_ANIMATION)
            self.animation.setStartValue(height)
            self.animation.setEndValue(heightExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    ###################### Анимация поиска ####################################
    def resultSearchBatchWindow(self):
        """Поиск по номеру заказа"""
        print('кнопка сработала')
        enable = True
        if enable:
            # GET WIDTH
            height = self.ui.BatchResult_Container.height()
            heightKIResultContainer = self.ui.KIresult_container.height()
            heightAggregatResultContainer = self.ui.AggregatResult_container.height()
            heightRollResultContainer = self.ui.RollcodeResult_container.height()
            maxExtend = ui_settings.Settings.DM_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            if height == 0:
                UIFunctions.start_SearchBox_animation(self, height, heightKIResultContainer, heightAggregatResultContainer,
                                                      heightRollResultContainer, "left")

    def resultSearchKIWindow(self):
        enable = True
        if enable:
            # GET WIDTH
            height = self.ui.KIresult_container.height()
            heightBatchResultContainer = self.ui.BatchResult_Container.height()
            heightAggregatResultContainer = self.ui.AggregatResult_container.height()
            heightRollResultContainer = self.ui.RollcodeResult_container.height()
            maxExtend = ui_settings.Settings.DM_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            if height == 0:
                UIFunctions.start_SearchBox_animation(self, heightBatchResultContainer, height, heightAggregatResultContainer,
                                                      heightRollResultContainer, "right")

    def resultSearchAggregatWindow(self):
        enable = True
        if enable:
            # GET WIDTH
            heightBatchResultContainer = self.ui.BatchResult_Container.height()
            heightKIResultContainer = self.ui.KIresult_container.height()
            height = self.ui.AggregatResult_container.height()
            heightRollResultContainer = self.ui.RollcodeResult_container.height()

            maxExtend = ui_settings.Settings.DM_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            if height == 0:
                UIFunctions.start_SearchBox_animation(self, heightBatchResultContainer, heightKIResultContainer, height,
                                                      heightRollResultContainer, "bottom")


    def resultSearchRollCodeWindow(self):
        enable = True
        if enable:
            # GET WIDTH
            heightBatchResultContainer = self.ui.BatchResult_Container.height()
            heightKIResultContainer = self.ui.KIresult_container.height()
            height = self.ui.RollcodeResult_container.height()
            heightAggregatResultContainer = self.ui.AggregatResult_container.height()

            maxExtend = ui_settings.Settings.DM_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            if height == 0:
                UIFunctions.start_SearchBox_animation(self, heightBatchResultContainer, heightKIResultContainer, heightAggregatResultContainer,
                                                      height, "top")


    def start_SearchBox_animation(self, BatchResultWindow_height, KIresult_containerWindow_heigh, AggregatResultWindow_height, RollcodeResultWindow_height, direction):
        right_width = 0
        left_width = 0
        bottom_width = 0
        top_width = 0

        # Check values
        if BatchResultWindow_height == 0 and direction == "left":
            left_width = 800
        else:
            left_width = 0

        # Check values
        if KIresult_containerWindow_heigh == 0 and direction == "right":
            right_width = 800
        else:
            right_width = 0

        # Check values
        if AggregatResultWindow_height == 0 and direction == "bottom":
            bottom_width = 800
        else:
            bottom_width = 0

        # Check values
        if RollcodeResultWindow_height == 0 and direction == "top":
            top_width = 800
        else:
            top_width = 0

        # ANIMATION LEFT BOX
        self.BATCH_box = QPropertyAnimation(self.ui.BatchResult_Container, b"minimumHeight")
        self.BATCH_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.BATCH_box.setStartValue(BatchResultWindow_height)
        self.BATCH_box.setEndValue(left_width)
        self.BATCH_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.KI_box = QPropertyAnimation(self.ui.KIresult_container, b"minimumHeight")
        self.KI_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.KI_box.setStartValue(KIresult_containerWindow_heigh)
        self.KI_box.setEndValue(right_width)
        self.KI_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION BOTTOM BOX
        self.AGG_box = QPropertyAnimation(self.ui.AggregatResult_container, b"minimumHeight")
        self.AGG_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.AGG_box.setStartValue(AggregatResultWindow_height)
        self.AGG_box.setEndValue(bottom_width)
        self.AGG_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION TOP BOX
        self.ROLL_box = QPropertyAnimation(self.ui.RollcodeResult_container, b"minimumHeight")
        self.ROLL_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.ROLL_box.setStartValue(RollcodeResultWindow_height)
        self.ROLL_box.setEndValue(top_width)
        self.ROLL_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.BATCH_box)
        self.group.addAnimation(self.KI_box)
        self.group.addAnimation(self.AGG_box)
        self.group.addAnimation(self.ROLL_box)
        self.group.start()

    def closeResultSearchWindow(self):
        """
        Закрытие окна результата поиска"""
        enable = True
        if enable:
            if self.ui.BatchResult_Container.height() > 0:
                height = self.ui.BatchResult_Container.height()
                self.animation = QPropertyAnimation(self.ui.BatchResult_Container, b"minimumHeight")
            elif self.ui.RollcodeResult_container.height() > 0:
                height = self.ui.RollcodeResult_container.height()
                self.animation = QPropertyAnimation(self.ui.RollcodeResult_container, b"minimumHeight")
            elif self.ui.AggregatResult_container.height() > 0:
                height = self.ui.AggregatResult_container.height()
                self.animation = QPropertyAnimation(self.ui.AggregatResult_container, b"minimumHeight")
            elif self.ui.KIresult_container.height() > 0:
                height = self.ui.KIresult_container.height()
                self.animation = QPropertyAnimation(self.ui.KIresult_container, b"minimumHeight")
            else:
                self.animation = QPropertyAnimation(self.ui.KIresult_container, b"minimumHeight")
                height = 0
            maxExtend = ui_settings.Settings.RESULT_SEARCH_CONTAINER
            standard = 0

            # ANIMATION
            # self.animation = QPropertyAnimation(self.ui.BatchResult_Container, b"minimumHeight")
            self.animation.setDuration(ui_settings.Settings.TIME_ANIMATION2)
            self.animation.setStartValue(height)
            self.animation.setEndValue(standard)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    #Вызов Субменю авторизации
    def userMenu(self):
        enable = True
        if enable:
            # GET WIDTH
            width = self.ui.accMenuContainer.width()
            maxExtend = ui_settings.Settings.LEFT_BOX_WIDTH
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.accMenuContainer, b"minimumWidth")
            self.animation.setDuration(ui_settings.Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # Вызов всплывающего окна всех КМ заказа
    def dmWindow(self):
        print('кнопка сработала')
        enable = True
        if enable:

            # GET WIDTH
            height = self.ui.codeContainer.height()
            heightLineContainer = self.ui.sendLineContainer.height()
            heightkituContainer = self.ui.KITUContainer.height()
            maxExtend = ui_settings.Settings.DM_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            UIFunctions.start_box_animation(self, height, heightLineContainer, heightkituContainer, "left")

    # Вызов всплывающего окна доступных линий
    def sendLineWindow(self):
        print('кнопка2 сработала')
        enable = True

        if enable:

            # GET WIDTH
            height = self.ui.sendLineContainer.height()
            heightcodeContainer = self.ui.codeContainer.height()
            heightkituContainer = self.ui.KITUContainer.height()
            maxExtend = ui_settings.Settings.LINE_BOX_HEIGHT
            standard = 0

            UIFunctions.start_box_animation(self, heightcodeContainer, height, heightkituContainer, "right")

    # Вызов всплывающего окна доступных КИТУ
    def kituWindow(self):
        print('кнопка3 сработала')
        enable = True

        if enable:
            # GET WIDTH
            height = self.ui.KITUContainer.height()
            heightcodeContainer = self.ui.codeContainer.height()
            heightlineContainer = self.ui.sendLineContainer.height()
            maxExtend = ui_settings.Settings.KITU_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            UIFunctions.start_box_animation(self, heightcodeContainer, heightlineContainer, height,  "bottom")

    def start_box_animation(self, DMwindow_heigh, line_window_heigh, kitu_window_height, direction):
        right_width = 0
        left_width = 0
        top_width = 0

        # Check values
        if DMwindow_heigh == 0 and direction == "left":
            left_width = 800
        else:
            left_width = 0
        # Check values
        if line_window_heigh == 0 and direction == "right":
            right_width = 800
        else:
            right_width = 0
        # Check values
        if kitu_window_height == 0 and direction == "bottom":
            top_width = 800
        else:
            top_width = 0
        # ANIMATION LEFT BOX
        self.DM_box = QPropertyAnimation(self.ui.codeContainer, b"maximumHeight")
        self.DM_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.DM_box.setStartValue(DMwindow_heigh)
        self.DM_box.setEndValue(left_width)
        self.DM_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.line_box = QPropertyAnimation(self.ui.sendLineContainer, b"maximumHeight")
        self.line_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.line_box.setStartValue(line_window_heigh)
        self.line_box.setEndValue(right_width)
        self.line_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION TOP BOX
        self.kitu_box = QPropertyAnimation(self.ui.KITUContainer, b"maximumHeight")
        self.kitu_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.kitu_box.setStartValue(kitu_window_height)
        self.kitu_box.setEndValue(top_width)
        self.kitu_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.DM_box)
        self.group.addAnimation(self.line_box)
        self.group.addAnimation(self.kitu_box)
        self.group.start()

    # Вызов всплывающего окна созданния продукта
    def addProductWindow(self):
        print('22кнопка сработала, показываю окно22')
        enable = True
        # GET WIDTH
        if enable:
            height = self.ui.addProductContainer.height()
            heightProductButtonContainer = self.ui.productButtonContainer.height()

            maxExtend = ui_settings.Settings.PROD_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            UIFunctions.start_setting_animation(self, height, heightProductButtonContainer, "left")

    # Вызов всплывающего окна кнопок редактирования продуктов
    def hideProductButton(self):
        print('кнопка2 сработала, показываю окно')
        enable = True

        if enable:
            height = self.ui.productButtonContainer.height()
            heightAddProductContainer = self.ui.addProductContainer.height()

            maxExtend = ui_settings.Settings.PROD_BUTTON_HEIGHT
            standard = 0

            # SET MAX WIDTH
            UIFunctions.start_setting_animation(self, height, heightAddProductContainer, "right")

    def editProductWindow(self):
        enable = True
        # GET WIDTH
        if enable:
            height = self.ui.editProductContainer.height()
            heightProductButtonContainer = self.ui.productButtonContainer.height()

            maxExtend = ui_settings.Settings.PROD_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            UIFunctions.start_edit_animation(self, height, heightProductButtonContainer, "left")

    def start_edit_animation(self, editProductWindow_height, hideProductButton_height, direction):
        right_width = 0
        left_width = 0

        # Check values
        if editProductWindow_height == 0 and direction == "left":
            left_width = 400
        else:
            left_width = 0
        # Check values
        if hideProductButton_height == 0 and direction == "left":
            right_width = 62
        else:
            right_width = 0

        # ANIMATION bottom BOX
        self.prod_box = QPropertyAnimation(self.ui.editProductContainer, b"maximumHeight")
        self.prod_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.prod_box.setStartValue(editProductWindow_height)
        self.prod_box.setEndValue(left_width)
        self.prod_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION bottom BOX
        self.btn_box = QPropertyAnimation(self.ui.productButtonContainer, b"maximumHeight")
        self.btn_box.setDuration(ui_settings.Settings.TIME_ANIMATION3)
        self.btn_box.setStartValue(hideProductButton_height)
        self.btn_box.setEndValue(right_width)
        self.btn_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.prod_box)
        self.group.addAnimation(self.btn_box)
        self.group.start()

    def start_setting_animation(self, addProductWindow_height, hideProductButton_height, direction):
        right_width = 0
        left_width = 0

        # Check values
        if addProductWindow_height == 0 and direction == "left":
            left_width = 400
        else:
            left_width = 0
        # Check values
        if hideProductButton_height == 0 and direction == "left":
            right_width = 62
        else:
            right_width = 0

        # ANIMATION bottom BOX
        self.prod_box = QPropertyAnimation(self.ui.addProductContainer, b"maximumHeight")
        self.prod_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.prod_box.setStartValue(addProductWindow_height)
        self.prod_box.setEndValue(left_width)
        self.prod_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION bottom BOX
        self.btn_box = QPropertyAnimation(self.ui.productButtonContainer, b"maximumHeight")
        self.btn_box.setDuration(ui_settings.Settings.TIME_ANIMATION3)
        self.btn_box.setStartValue(hideProductButton_height)
        self.btn_box.setEndValue(right_width)
        self.btn_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.prod_box)
        self.group.addAnimation(self.btn_box)
        self.group.start()

    # Вызов всплывающего окна созданния линии
    def addLineWindow(self):
        print('33кнопка сработала, показываю окно33')
        enable = True
        # GET WIDTH
        if enable:
            self.ui.lineIPEdit.setInputMask('000.000.000.000;_')
            height = self.ui.addLineContainer.height()
            heightLineButtonContainer = self.ui.lineButtonContainer.height()

            maxExtend = ui_settings.Settings.PROD_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            UIFunctions.start_LineSetting_animation(self, height, heightLineButtonContainer, "left")

        # Вызов всплывающего окна кнопок редактирования продуктов

    def hideLineButton(self):
        print('кнопка33 сработала, показываю окно')
        enable = True

        if enable:
            height = self.ui.lineButtonContainer.height()
            heightAddLineContainer = self.ui.addLineContainer.height()

            maxExtend = ui_settings.Settings.PROD_BUTTON_HEIGHT
            standard = 0

            # SET MAX WIDTH
            UIFunctions.start_LineSetting_animation(self, height, heightAddLineContainer, "right")

    def editLineWindow(self):
        enable = True
        # GET WIDTH
        if enable:
            height = self.ui.editLineContainer.height()
            heightLineButtonContainer = self.ui.lineButtonContainer.height()

            maxExtend = ui_settings.Settings.PROD_BOX_HEIGHT
            standard = 0

            # SET MAX WIDTH
            UIFunctions.start_lineEdit_animation(self, height, heightLineButtonContainer, "left")

    def start_lineEdit_animation(self, editLineWindow_height, hideLineButton_height, direction):
        right_width = 0
        left_width = 0

        # Check values
        if editLineWindow_height == 0 and direction == "left":
            left_width = 400
        else:
            left_width = 0
        # Check values
        if hideLineButton_height == 0 and direction == "left":
            right_width = 62
        else:
            right_width = 0

        # ANIMATION bottom BOX
        self.prod_box = QPropertyAnimation(self.ui.editLineContainer, b"maximumHeight")
        self.prod_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.prod_box.setStartValue(editLineWindow_height)
        self.prod_box.setEndValue(left_width)
        self.prod_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION bottom BOX
        self.btn_box = QPropertyAnimation(self.ui.lineButtonContainer, b"maximumHeight")
        self.btn_box.setDuration(ui_settings.Settings.TIME_ANIMATION3)
        self.btn_box.setStartValue(hideLineButton_height)
        self.btn_box.setEndValue(right_width)
        self.btn_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.prod_box)
        self.group.addAnimation(self.btn_box)
        self.group.start()

    def start_LineSetting_animation(self, addLineWindow_height, hideLineButton_height, direction):
        right_width = 0
        left_width = 0

        # Check values
        if addLineWindow_height == 0 and direction == "left":
            left_width = 400
        else:
            left_width = 0
        # Check values
        if hideLineButton_height == 0 and direction == "left":
            right_width = 62
        else:
            right_width = 0

        # ANIMATION bottom BOX
        self.line_box = QPropertyAnimation(self.ui.addLineContainer, b"maximumHeight")
        self.line_box.setDuration(ui_settings.Settings.TIME_ANIMATION2)
        self.line_box.setStartValue(addLineWindow_height)
        self.line_box.setEndValue(left_width)
        self.line_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION bottom BOX
        self.btnLine_box = QPropertyAnimation(self.ui.lineButtonContainer, b"maximumHeight")
        self.btnLine_box.setDuration(ui_settings.Settings.TIME_ANIMATION3)
        self.btnLine_box.setStartValue(hideLineButton_height)
        self.btnLine_box.setEndValue(right_width)
        self.btnLine_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.line_box)
        self.group.addAnimation(self.btnLine_box)
        self.group.start()


    """def resize_grips(self):
        if ui_settings.Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)"""
