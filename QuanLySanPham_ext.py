from time import sleep

from PyQt6.QtWidgets import QPushButton
from jedi.plugins.stdlib import functools_partial
import functools
from QuanLySanPham import Ui_MainWindow

class QuanLySanPham_ext(Ui_MainWindow):
    def __init__(self):
        self.product = []
    def dataSimulation(self):
        self.product.append({"Ma": "SP1","Ten":"Coca","Gia":15,"Loai SP":True})
        self.product.append({"Ma": "SP2", "Ten": "Pepsi", "Gia": 10, "Loai SP": False})
        self.product.append({"Ma": "SP3", "Ten": "Redbull", "Gia": 20, "Loai SP": False})
        self.product.append({"Ma": "SP4", "Ten": "Ken", "Gia": 17, "Loai SP": True})
        self.product.append({"Ma": "SP5", "Ten": "Sting", "Gia": 18, "Loai SP": False})
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_save.clicked.connect(self.process_save)

    def process_save(self):
        ma = self.lineEdit_ma.text()
        ten = self.lineEdit_ten.text()
        gia = self.lineEdit_gia.text()
        loai = self.checkBox_caocap.isChecked()
        self.product.append({"Ma": f"{ma}", "Ten": f"{ten}", "Gia": gia, "Loai SP": loai})
        for i in reversed(range(self.verticalLayout_product.count())):
            self.verticalLayout_product.itemAt(i).widget().setParent(None)
        self.HienThiSanPhamLenGiaoDien()





    def show(self):
        self.MainWindow.show()
    def HienThiSanPhamLenGiaoDien(self):
        for product in self.product:
            #trich xuat du lieu
            ma = product["Ma"]
            ten = product["Ten"]
            gia = product["Gia"]
            loai = product["Loai SP"]
            #nut hien thi
            buttonProduct = QPushButton()
            infor = f"Ma = {ma}, Ten = {ten}, Gia = {gia}"
            buttonProduct.setText(infor)
            buttonProduct.setFixedHeight(50)
            style = "background-color: pink; font-size: 15pt"
            if loai == True:
                style = "background-color: yellow; font-size: 15pt"
            buttonProduct.setStyleSheet(style)
            self.verticalLayout_product.addWidget(buttonProduct)
            buttonProduct.clicked.connect(functools.partial(self.hienthi_chitiet, product))
    def hienthi_chitiet(self, product):
        ma = product["Ma"]
        ten = product["Ten"]
        gia = product["Gia"]
        loai = product["Loai SP"]
        self.lineEdit_ma.setText(ma)
        self.lineEdit_ten.setText(ten)
        self.lineEdit_gia.setText(f"{gia}")
        self.checkBox_caocap.setChecked(loai)