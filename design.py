from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateCompanyWindow(object):
    def setupUi(self, CreateCompanyWindow):
        CreateCompanyWindow.setObjectName("CreateCompanyWindow")
        CreateCompanyWindow.setFixedSize(228, 55)
        self.centralwidget = QtWidgets.QWidget(CreateCompanyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.company_name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.company_name_line.setGeometry(QtCore.QRect(10, 10, 113, 25))
        self.company_name_line.setObjectName("company_name_line")
        self.create_company_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_company_button.setGeometry(QtCore.QRect(130, 10, 89, 25))
        self.create_company_button.setObjectName("create_company_button")
        self.menubar = QtWidgets.QMenuBar(CreateCompanyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        CreateCompanyWindow.setMenuBar(self.menubar)

        CreateCompanyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateCompanyWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateCompanyWindow)

    def retranslateUi(self, CreateCompanyWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateCompanyWindow.setWindowTitle(_translate("CreateCompanyWindow", " "))
        self.company_name_line.setPlaceholderText(_translate("CreateCompanyWindow", "Название"))
        self.create_company_button.setText(_translate("CreateCompanyWindow", "Добавить"))


class Ui_PeopleSearchWindow(object):
    def setupUi(self, PeopleSearchWindow):
        PeopleSearchWindow.setObjectName("PeopleSearchWindow")
        PeopleSearchWindow.setFixedSize(471, 461)
        self.centralwidget = QtWidgets.QWidget(PeopleSearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.first_name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name_line.setGeometry(QtCore.QRect(10, 10, 151, 25))
        self.first_name_line.setObjectName("first_name_line")
        self.last_name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name_line.setGeometry(QtCore.QRect(170, 10, 151, 25))
        self.last_name_line.setObjectName("last_name_line")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(330, 10, 131, 25))
        self.search_button.setObjectName("search_button")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(10, 290, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(130, 70, 209, 191))
        self.picture_label.setText("")
        self.picture_label.setObjectName("picture_label")
        self.company_label = QtWidgets.QLabel(self.centralwidget)
        self.company_label.setGeometry(QtCore.QRect(10, 330, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.company_label.setFont(font)
        self.company_label.setAlignment(QtCore.Qt.AlignCenter)
        self.company_label.setObjectName("company_label")
        self.group_label = QtWidgets.QLabel(self.centralwidget)
        self.group_label.setGeometry(QtCore.QRect(10, 370, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_label.setFont(font)
        self.group_label.setAlignment(QtCore.Qt.AlignCenter)
        self.group_label.setObjectName("group_label")
        self.menubar = QtWidgets.QMenuBar(PeopleSearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 22))
        self.menubar.setObjectName("menubar")
        PeopleSearchWindow.setMenuBar(self.menubar)
        PeopleSearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PeopleSearchWindow)
        QtCore.QMetaObject.connectSlotsByName(PeopleSearchWindow)

    def retranslateUi(self, PeopleSearchWindow):
        _translate = QtCore.QCoreApplication.translate
        PeopleSearchWindow.setWindowTitle(_translate("PeopleSearchWindow", "Records"))
        self.first_name_line.setPlaceholderText(_translate("PeopleSearchWindow", "Имя"))
        self.last_name_line.setPlaceholderText(_translate("PeopleSearchWindow", "Фамилия"))
        self.search_button.setText(_translate("PeopleSearchWindow", "Поиск"))
        self.name_label.setText(_translate("PeopleSearchWindow", ""))
        self.company_label.setText(_translate("PeopleSearchWindow", ""))
        self.group_label.setText(_translate("PeopleSearchWindow", ""))


class Ui_Alert(object):
    def setupUi(self, Alert):
        Alert.setObjectName("Alert")
        Alert.setFixedSize(293, 139)
        self.alert_label = QtWidgets.QLabel(Alert)
        self.alert_label.setGeometry(QtCore.QRect(10, 10, 271, 71))
        self.alert_label.setTextFormat(QtCore.Qt.AutoText)
        self.alert_label.setScaledContents(False)
        self.alert_label.setAlignment(QtCore.Qt.AlignCenter)
        self.alert_label.setWordWrap(True)
        self.alert_label.setObjectName("alert_label")
        self.ok_button = QtWidgets.QPushButton(Alert)
        self.ok_button.setGeometry(QtCore.QRect(100, 90, 89, 25))
        self.ok_button.setObjectName("pushButton")

        self.retranslateUi(Alert)
        QtCore.QMetaObject.connectSlotsByName(Alert)

    def retranslateUi(self, Alert):
        _translate = QtCore.QCoreApplication.translate
        Alert.setWindowTitle(_translate("Alert", " "))
        self.alert_label.setText(_translate("Alert", " "))
        self.ok_button.setText(_translate("Alert", "Ок"))


class Ui_AddPerson(object):
    def setupUi(self, AddPerson):
        AddPerson.setObjectName("AddPerson")
        AddPerson.setFixedSize(631, 310)
        self.centralwidget = QtWidgets.QWidget(AddPerson)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 611, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.first_name_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.first_name_line.setText("")
        self.first_name_line.setObjectName("first_name_line")
        self.horizontalLayout.addWidget(self.first_name_line)
        self.last_name_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.last_name_line.setObjectName("last_name_line")
        self.horizontalLayout.addWidget(self.last_name_line)
        self.companies_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.companies_box.setCurrentText("")
        self.companies_box.setObjectName("companies_box")
        self.horizontalLayout.addWidget(self.companies_box)
        self.groups_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.groups_box.setObjectName("groups_box")
        self.horizontalLayout.addWidget(self.groups_box)
        self.picture_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.picture_line.setObjectName("picture_line")
        self.horizontalLayout.addWidget(self.picture_line)
        self.open_image = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.open_image.setObjectName("open_image")
        self.horizontalLayout.addWidget(self.open_image)
        self.add_person_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_person_button.setObjectName("add_person_button")
        self.horizontalLayout.addWidget(self.add_person_button)
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(210, 70, 209, 191))
        self.picture_label.setText("")
        self.picture_label.setObjectName("picture_label")
        self.take_snapshot_button = QtWidgets.QPushButton(AddPerson)
        self.take_snapshot_button.setGeometry(QtCore.QRect(self.rect().center().x() - 75, 270, 150, 25))
        self.take_snapshot_button.setText("Сделать снимок")
        self.menubar = QtWidgets.QMenuBar(AddPerson)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        AddPerson.setMenuBar(self.menubar)

        AddPerson.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddPerson)
        QtCore.QMetaObject.connectSlotsByName(AddPerson)

    def retranslateUi(self, AddPerson):
        _translate = QtCore.QCoreApplication.translate
        AddPerson.setWindowTitle(_translate("AddPerson", " "))
        self.first_name_line.setPlaceholderText(_translate("AddPerson", "Имя"))
        self.last_name_line.setPlaceholderText(_translate("AddPerson", "Фамилия"))
        self.picture_line.setPlaceholderText(_translate("AddPerson", "Фото"))
        self.open_image.setText(_translate("AddPerson", "..."))
        self.add_person_button.setText(_translate("AddPerson", "Добавить"))


class Ui_AddGroupWindow(object):
    def setupUi(self, AddGroupWindow):
        AddGroupWindow.setObjectName("AddGroupWindow")
        AddGroupWindow.setFixedSize(351, 84)
        self.centralwidget = QtWidgets.QWidget(AddGroupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.companies_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.companies_box.setObjectName("companies_box")
        self.horizontalLayout.addWidget(self.companies_box)
        self.group_name_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.group_name_line.setObjectName("group_name_line")
        self.horizontalLayout.addWidget(self.group_name_line)
        self.add_group_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_group_button.setObjectName("add_group_button")
        self.horizontalLayout.addWidget(self.add_group_button)
        self.menubar = QtWidgets.QMenuBar(AddGroupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        AddGroupWindow.setMenuBar(self.menubar)

        AddGroupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddGroupWindow)
        QtCore.QMetaObject.connectSlotsByName(AddGroupWindow)

    def retranslateUi(self, AddGroupWindow):
        _translate = QtCore.QCoreApplication.translate
        AddGroupWindow.setWindowTitle(_translate("AddGroupWindow", " "))
        self.group_name_line.setPlaceholderText(_translate("AddGroupWindow", "Название"))
        self.add_group_button.setText(_translate("AddGroupWindow", "Добавить"))


class Ui_ChoosePersonWindow(object):
    def setupUi(self, ChoosePersonWindow):
        ChoosePersonWindow.setObjectName("ChoosePersonWindow")
        ChoosePersonWindow.setFixedSize(311, 320)
        self.centralwidget = QtWidgets.QWidget(ChoosePersonWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 291, 231))
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setObjectName("listWidget")
        ChoosePersonWindow.setCentralWidget(self.centralwidget)
        self.choose_person_button = QtWidgets.QPushButton(ChoosePersonWindow)
        self.choose_person_button.setGeometry(QtCore.QRect(self.rect().center().x() - 75, 250, 150, 25))
        self.choose_person_button.setText("Выбрать")
        self.menubar = QtWidgets.QMenuBar(ChoosePersonWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        ChoosePersonWindow.setMenuBar(self.menubar)

        self.retranslateUi(ChoosePersonWindow)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(ChoosePersonWindow)

    def retranslateUi(self, ChoosePersonWindow):
        _translate = QtCore.QCoreApplication.translate
        ChoosePersonWindow.setWindowTitle(_translate("ChoosePersonWindow", " "))


class Ui_DeletePersonWindow(object):
    def setupUi(self, DeletePersonWindow):
        DeletePersonWindow.setObjectName("DeletePersonWindow")
        DeletePersonWindow.setFixedSize(393, 91)
        self.centralwidget = QtWidgets.QWidget(DeletePersonWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.first_name_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.first_name_line.setObjectName("first_name_line")
        self.horizontalLayout.addWidget(self.first_name_line)
        self.last_name_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.last_name_line.setObjectName("last_name_line")
        self.horizontalLayout.addWidget(self.last_name_line)
        self.delete_person_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_person_button.setObjectName("delete_person_button")
        self.horizontalLayout.addWidget(self.delete_person_button)
        DeletePersonWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DeletePersonWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        DeletePersonWindow.setMenuBar(self.menubar)


        self.retranslateUi(DeletePersonWindow)
        QtCore.QMetaObject.connectSlotsByName(DeletePersonWindow)

    def retranslateUi(self, DeletePersonWindow):
        _translate = QtCore.QCoreApplication.translate
        DeletePersonWindow.setWindowTitle(_translate("DeletePersonWindow", " "))
        self.first_name_line.setPlaceholderText(_translate("DeletePersonWindow", "Имя"))
        self.last_name_line.setPlaceholderText(_translate("DeletePersonWindow", "Фамилия"))
        self.delete_person_button.setText(_translate("DeletePersonWindow", "Удалить"))


class Ui_DeleteCompanyWindow(object):
    def setupUi(self, DeleteCompanyWindow):
        DeleteCompanyWindow.setObjectName("DeleteCompanyWindow")
        DeleteCompanyWindow.setFixedSize(393, 91)
        self.centralwidget = QtWidgets.QWidget(DeleteCompanyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.delete_company_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_company_button.setObjectName("delete_company_button")
        self.horizontalLayout.addWidget(self.delete_company_button)
        DeleteCompanyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DeleteCompanyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        DeleteCompanyWindow.setMenuBar(self.menubar)

        self.retranslateUi(DeleteCompanyWindow)
        QtCore.QMetaObject.connectSlotsByName(DeleteCompanyWindow)

    def retranslateUi(self, DeleteCompanyWindow):
        _translate = QtCore.QCoreApplication.translate
        DeleteCompanyWindow.setWindowTitle(_translate("DeleteCompanyWindow", " "))
        self.delete_company_button.setText(_translate("DeleteCompanyWindow", "Удалить"))


class Ui_DeleteGroupWindow(object):
    def setupUi(self, DeleteGroupWindow):
        DeleteGroupWindow.setObjectName("DeleteGroupWindow")
        DeleteGroupWindow.setFixedSize(393, 91)
        self.centralwidget = QtWidgets.QWidget(DeleteGroupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.companies_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.companies_box.setObjectName("companies_box")
        self.horizontalLayout.addWidget(self.companies_box)
        self.groups_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.groups_box.setObjectName("groups_box")
        self.horizontalLayout.addWidget(self.groups_box)
        self.delete_group_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_group_button.setObjectName("delete_group_button")
        self.horizontalLayout.addWidget(self.delete_group_button)
        DeleteGroupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DeleteGroupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        DeleteGroupWindow.setMenuBar(self.menubar)


        self.retranslateUi(DeleteGroupWindow)
        QtCore.QMetaObject.connectSlotsByName(DeleteGroupWindow)

    def retranslateUi(self, DeleteGroupWindow):
        _translate = QtCore.QCoreApplication.translate
        DeleteGroupWindow.setWindowTitle(_translate("DeleteGroupWindow", " "))
        self.delete_group_button.setText(_translate("DeleteGroupWindow", "Удалить"))


class Ui_ChoosePersonToChangeWindow(object):
    def setupUi(self, ChoosePersonToChangeWindow):
        ChoosePersonToChangeWindow.setObjectName("ChoosePersonToChangeWindow")
        ChoosePersonToChangeWindow.setFixedSize(378, 55)
        self.centralwidget = QtWidgets.QWidget(ChoosePersonToChangeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.first_name_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.first_name_line.setObjectName("first_name_line")
        self.horizontalLayout.addWidget(self.first_name_line)
        self.last_name_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.last_name_line.setObjectName("last_name_line")
        self.horizontalLayout.addWidget(self.last_name_line)
        self.change_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.change_button.setObjectName("change_button")
        self.horizontalLayout.addWidget(self.change_button)
        ChoosePersonToChangeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChoosePersonToChangeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        ChoosePersonToChangeWindow.setMenuBar(self.menubar)


        self.retranslateUi(ChoosePersonToChangeWindow)
        QtCore.QMetaObject.connectSlotsByName(ChoosePersonToChangeWindow)

    def retranslateUi(self, ChoosePersonToChangeWindow):
        _translate = QtCore.QCoreApplication.translate
        ChoosePersonToChangeWindow.setWindowTitle(_translate("ChoosePersonToChangeWindow", " "))
        self.first_name_line.setPlaceholderText(_translate("ChoosePersonToChangeWindow", "Имя"))
        self.last_name_line.setPlaceholderText(_translate("ChoosePersonToChangeWindow", "Фамилия"))
        self.change_button.setText(_translate("ChoosePersonToChangeWindow", "Изменить"))


class Ui_ChangePersonWindow(object):
    def setupUi(self, ChangePersonWindow):
        ChangePersonWindow.setObjectName("ChangePersonWindow")
        ChangePersonWindow.setFixedSize(581, 95)
        self.centralwidget = QtWidgets.QWidget(ChangePersonWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.first_name_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.first_name_line.setObjectName("first_name_line")
        self.first_name_line.setPlaceholderText("Имя")
        self.first_name_line.setReadOnly(True)
        self.horizontalLayout.addWidget(self.first_name_line)
        self.last_name_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.last_name_line.setObjectName("last_name_line")
        self.last_name_line.setPlaceholderText("Фамилия")
        self.last_name_line.setReadOnly(True)
        self.horizontalLayout.addWidget(self.last_name_line)
        self.companies_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.companies_box.setObjectName("companies_box")
        self.horizontalLayout.addWidget(self.companies_box)
        self.groups_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.groups_box.setObjectName("groups_box")
        self.horizontalLayout.addWidget(self.groups_box)
        self.save_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        ChangePersonWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChangePersonWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        ChangePersonWindow.setMenuBar(self.menubar)


        self.retranslateUi(ChangePersonWindow)
        QtCore.QMetaObject.connectSlotsByName(ChangePersonWindow)

    def retranslateUi(self, ChangePersonWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangePersonWindow.setWindowTitle(_translate("ChangePersonWindow", " "))
        self.save_button.setText(_translate("ChangePersonWindow", "Сохранить"))


class Ui_StartFaceRecognitionWindow(object):
    def setupUi(self, StartFaceRecognitionWindow):
        StartFaceRecognitionWindow.setObjectName("StartFaceRecognitionWindow")
        StartFaceRecognitionWindow.setFixedSize(610, 55)
        self.centralwidget = QtWidgets.QWidget(StartFaceRecognitionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.companies_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.companies_box.setObjectName("companies_box")
        self.horizontalLayout.addWidget(self.companies_box)
        self.groups_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.groups_box.setObjectName("groups_box")
        self.horizontalLayout.addWidget(self.groups_box)
        self.speed_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.speed_box.setObjectName("speed_box")
        self.horizontalLayout.addWidget(self.speed_box)
        self.start_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        StartFaceRecognitionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartFaceRecognitionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
        self.menubar.setObjectName("menubar")
        StartFaceRecognitionWindow.setMenuBar(self.menubar)


        self.retranslateUi(StartFaceRecognitionWindow)
        QtCore.QMetaObject.connectSlotsByName(StartFaceRecognitionWindow)

    def retranslateUi(self, StartFaceRecognitionWindow):
        _translate = QtCore.QCoreApplication.translate
        StartFaceRecognitionWindow.setWindowTitle(_translate("StartFaceRecognitionWindow", " "))
        self.start_button.setText(_translate("StartFaceRecognitionWindow", "Начать"))
