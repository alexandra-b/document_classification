import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
# from first_gui import Ui_Dialog
from menu import Ui_MainWindow
from simple_parse import *

app = QApplication(sys.argv)
ex = Ui_MainWindow()
w = QMainWindow()
ex.setupUi(w)
w.setWindowTitle('Document classifier')
w.show()
app.exec_()
ex.dump_to_file()
sys.exit()

# class AppWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.show()
#
#
# app = QApplication(sys.argv)
# w = AppWindow()
# w.show()
# sys.exit(app.exec_())


# import sys
# import random
# from PySide2 import QtCore, QtWidgets, QtGui
#
#
# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#
#         self.button = QtWidgets.QPushButton("Click me!")
#         self.text = QtWidgets.QLabel("Hello World")
#         self.text.setAlignment(QtCore.Qt.AlignCenter)
#
#         self.layout = QtWidgets.QVBoxLayout()
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)
#         self.setLayout(self.layout)
#
#         self.button.clicked.connect(self.magic)
#
#     def magic(self):
#         self.text.setText(random.choice(self.hello))


