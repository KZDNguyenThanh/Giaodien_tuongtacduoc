# Form implementation generated from reading ui file 'D:\rebuild\ProductMng\QuanLySanPham.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 788)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 641, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 70, 881, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_ma = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_ma.setGeometry(QtCore.QRect(140, 40, 551, 41))
        self.lineEdit_ma.setStyleSheet("background-color: rgb(234, 234, 58);")
        self.lineEdit_ma.setObjectName("lineEdit_ma")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_ten = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_ten.setGeometry(QtCore.QRect(140, 100, 551, 41))
        self.lineEdit_ten.setStyleSheet("background-color: rgb(234, 234, 58);")
        self.lineEdit_ten.setObjectName("lineEdit_ten")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_gia = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_gia.setGeometry(QtCore.QRect(140, 160, 551, 41))
        self.lineEdit_gia.setStyleSheet("background-color: rgb(234, 234, 58);")
        self.lineEdit_gia.setObjectName("lineEdit_gia")
        self.checkBox_caocap = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_caocap.setGeometry(QtCore.QRect(140, 220, 161, 41))
        self.checkBox_caocap.setObjectName("checkBox_caocap")
        self.pushButton_new = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_new.setGeometry(QtCore.QRect(160, 270, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_new.setFont(font)
        self.pushButton_new.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_new.setObjectName("pushButton_new")
        self.pushButton_save = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_save.setGeometry(QtCore.QRect(370, 270, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_sort = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_sort.setGeometry(QtCore.QRect(570, 270, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_sort.setFont(font)
        self.pushButton_sort.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_sort.setObjectName("pushButton_sort")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(130, 470, 891, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 851, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_product = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_product.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_product.setObjectName("verticalLayout_product")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 21, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 19, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1176, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.checkBox_caocap.stateChanged['int'].connect(self.label.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Quản lý sản phẩm"))
        self.groupBox.setTitle(_translate("MainWindow", "Chi tiết sản phẩm"))
        self.label_2.setText(_translate("MainWindow", "Mã:"))
        self.label_3.setText(_translate("MainWindow", "Tên:"))
        self.label_4.setText(_translate("MainWindow", "Giá:"))
        self.checkBox_caocap.setText(_translate("MainWindow", "Hàng cao cấp"))
        self.pushButton_new.setText(_translate("MainWindow", "New"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_sort.setText(_translate("MainWindow", "Sort"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Danh sách sản phẩm"))