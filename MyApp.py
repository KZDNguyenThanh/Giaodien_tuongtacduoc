from PyQt6.QtWidgets import QApplication, QMainWindow

from QuanLySanPham_ext import QuanLySanPham_ext

app=QApplication([])

qMainWindow=QMainWindow()

myWindow=QuanLySanPham_ext()

myWindow.setupUi(qMainWindow)
myWindow.dataSimulation()
myWindow.HienThiSanPhamLenGiaoDien()
qMainWindow.show()

app.exec()
