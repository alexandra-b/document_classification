# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classify_popup.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 650)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 30, 231, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 50, 181, 151))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(40, 50, 181, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.close)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 240, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self._cancel_tags)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 300, 121, 16))
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 330, 491, 201))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Algorithm classified tags"))
        self.label_3.setText(_translate("Dialog", "Assign new tags, separated by commas"))
        self.pushButton.setText(_translate("Dialog", "Classify"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Document summary"))

    def set_summary(self, summary):
        self.textBrowser_2.setText(summary)

    def _cancel_tags(self, Dialog):
        self.textEdit_2.clear()
        Dialog.close()

    def set_classified_tags(self, tags_list):
        for tag in tags_list:
            self.textBrowser.append(tag)


