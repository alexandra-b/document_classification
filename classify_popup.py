# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classify_popup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(553, 332)
        self.d_label_2 = QtWidgets.QLabel(Dialog)
        self.d_label_2.setGeometry(QtCore.QRect(40, 30, 171, 16))
        self.d_label_2.setObjectName("d_label_2")
        self.d_label_3 = QtWidgets.QLabel(Dialog)
        self.d_label_3.setGeometry(QtCore.QRect(280, 30, 231, 16))
        self.d_label_3.setObjectName("d_label_3")
        self.d_textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.d_textEdit_2.setGeometry(QtCore.QRect(280, 50, 191, 151))
        self.d_textEdit_2.setObjectName("d_textEdit_2")
        self.d_textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.d_textBrowser.setGeometry(QtCore.QRect(40, 50, 181, 151))
        self.d_textBrowser.setObjectName("d_textBrowser")
        self.d_pushButton = QtWidgets.QPushButton(Dialog)
        self.d_pushButton.setGeometry(QtCore.QRect(130, 250, 93, 28))
        self.d_pushButton.setObjectName("d_pushButton")
        self.d_pushButton.clicked.connect(Dialog.close)
        self.d_pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.d_pushButton_2.setGeometry(QtCore.QRect(270, 250, 93, 28))
        self.d_pushButton_2.setObjectName("d_pushButton_2")
        self.d_pushButton_2.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.d_label_2.setText(_translate("Dialog", "Algorithm classified tags"))
        self.d_label_3.setText(_translate("Dialog", "Assign new tags, separated by commas"))
        self.d_pushButton.setText(_translate("Dialog", "Classify"))
        self.d_pushButton_2.setText(_translate("Dialog", "Cancel"))


# #if __name__ == "__main__":
# def init_dialog(self):
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

