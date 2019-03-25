# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from simple_parse import *
from obtain_synonym import extract_synonyms
from classify_popup import *
import json
import os

# class TagPopup(QtWidgets.QWidget):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#         self.initUI()
#
#     def initUI(self):
#         label_name = QtWidgets.QLabel(self.name, self)


class Ui_MainWindow(object):
    search_paths = []
    _how_many = 3
    _chosen_tick_treshold = 1
    parsed_files = []
    tag_popup = None
    popup = None
    Dialog = None
    _user_map = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 291, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 81, 21))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 120, 381, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 271, 41))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 230, 381, 61))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 310, 131, 31))
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 310, 241, 71))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 201, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 201, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 490, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.search_files)
        # self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        # self.textBrowser_2.setGeometry(QtCore.QRect(500, 70, 451, 421))
        # self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 20, 121, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 390, 211, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 440, 16, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 440, 16, 21))
        self.label_8.setObjectName("label_8")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.valueChanged.connect(self.value_changed)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 420, 181, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 620, 131, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self._clear_file) # -> TO REMOVE ALL USER DEFINED TAGS
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(500, 60, 691, 241))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self._build_popup)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(500, 320, 161, 16))
        self.label_9.setObjectName("label_9")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(500, 350, 691, 241))
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1260, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuClassify = QtWidgets.QMenu(self.menuBar)
        self.menuClassify.setObjectName("menuClassify")
        self.menuHistory = QtWidgets.QMenu(self.menuBar)
        self.menuHistory.setObjectName("menuHistory")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.actionManual_classifier = QtWidgets.QAction(MainWindow)
        self.actionManual_classifier.setObjectName("actionManual_classifier")
        self.actionAutomatic_classifier = QtWidgets.QAction(MainWindow)
        self.actionAutomatic_classifier.setObjectName("actionAutomatic_classifier")
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionAutomatic = QtWidgets.QAction(MainWindow)
        self.actionAutomatic.setObjectName("actionAutomatic")
        self.actionClear_all_tags = QtWidgets.QAction(MainWindow)
        self.actionClear_all_tags.setObjectName("actionClear_all_tags")
        self.actionTags = QtWidgets.QAction(MainWindow)
        self.actionTags.setObjectName("actionTags")
        self.actionClassified_files = QtWidgets.QAction(MainWindow)
        self.actionClassified_files.setObjectName("actionClassified_files")
        self.menuClassify.addSeparator()
        self.menuClassify.addAction(self.actionManual)
        self.menuClassify.addAction(self.actionAutomatic)
        self.menuHistory.addAction(self.actionClear_all_tags)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionTags)
        self.menuView.addAction(self.actionClassified_files)
        self.menuBar.addAction(self.menuClassify.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHistory.menuAction())
        try:
            fp = open('user_defined_drop.txt', 'r')
            self._user_map = json.load(fp)
            fp.close()
        except:
            pass
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choose the folder in which to search for the tags"))
        self.pushButton.setText(_translate("MainWindow", "Open files and folders"))
        self.pushButton.clicked.connect(self.search_folders_clicked)
        self.label_2.setText(_translate("MainWindow", "Searching in"))
        self.label_4.setText(_translate("MainWindow", "Enter tags to search, separated by commas"))
        self.label_3.setText(_translate("MainWindow", "Choose type of search"))
        self.radioButton.setText(_translate("MainWindow", "Recursive, enter subdirectories"))
        self.radioButton_2.setText(_translate("MainWindow", "Just files in this directory"))
        self.pushButton_2.setText(_translate("MainWindow", "Search "))
        self.label_5.setText(_translate("MainWindow", "Results"))
        self.label_6.setText(_translate("MainWindow", "Treshold - number of synonyms"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "5"))
        self.label_9.setText(_translate("MainWindow", "User classified documents"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset tags"))
        self.menuClassify.setTitle(_translate("MainWindow", "Classify"))
        self.menuHistory.setTitle(_translate("MainWindow", "History"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionManual_classifier.setText(_translate("MainWindow", "Manual classifier"))
        self.actionAutomatic_classifier.setText(_translate("MainWindow", "Automatic classifier"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionAutomatic.setText(_translate("MainWindow", "Automatic"))
        self.actionClear_all_tags.setText(_translate("MainWindow", "Clear all tags"))
        self.actionTags.setText(_translate("MainWindow", "Tags"))
        self.actionClassified_files.setText(_translate("MainWindow", "Classified files"))
        self._refresh_user_defined()

    def value_changed(self):
        self._chosen_tick_treshold = str(self.horizontalSlider.value())
        # print('Tick chosen -> ', self._chosen_tick_treshold)

    def search_folders_clicked(self):
        file_dialog = QtWidgets.QFileDialog()
        # files = file_dialog.getExistingDirectory()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        file_view = file_dialog.findChild(QtWidgets.QListView, 'listView')
        # to make it possible to select multiple directories:
        if file_view:
            file_view.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        f_tree_view = file_dialog.findChild(QtWidgets.QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        if file_dialog.exec():
            paths = file_dialog.selectedFiles()
        else:
            paths = ''
        self.textBrowser.clear()
        self.textEdit_2.clear()
        self.search_paths = []
        for f in paths:
            self.textBrowser.append(f)
        # self.textBrowser.append(files)
        self.search_paths = paths

    def _obtain_synonyms(self, word):
        return extract_synonyms(word, int(self._chosen_tick_treshold))

    @staticmethod
    def _list_from_comma_text(string):
        string_list = string.split(',')
        string_list = [t.lower().strip() for t in string_list]
        return string_list

    def search_files(self):
        tags = self.textEdit_2.toPlainText()
        # print('TAGS TO SEARCH FOR ARE : ', tags)
        tags_list = tags.split(',')
        tags_list = [t.lower().strip() for t in tags_list]
        all_syns = []
        for el in tags_list:
            syn_list = self._obtain_synonyms(el)
            # all_words[el] = syn_list
            all_syns.extend(syn_list)
        all_syns.extend(tags_list)
        # self._chosen_tick_treshold
        if self.radioButton.isChecked():
            # normal search, non recursive
            recursive = True
        elif self.radioButton_2.isChecked():
            recursive = False
        # for t in tags_list:
        #     print('Tag: ', t)
        parser = FolderParser()
        self.parsed_files = []
        for f in self.search_paths:
            self.parsed_files.append(parser.parse(recursive, f, all_syns))
        # mystr = ''
        self._put_algorithm_defined_list()
        # self.textBrowser_2.setText(mystr)

    def _put_algorithm_defined_list(self):
        self.listWidget.clear()
        for folder in self.parsed_files:
            for file in folder:
                toWrite = True
                mystr = ''
                mystr += file+'->'
                no_tags = True
                for tag in folder[file]:
                    if file in self._user_map:
                        toWrite = False
                        continue
                    if folder[file][tag] > 0:
                        no_tags = False
                        mystr += tag + ' '
                        mystr += str(folder[file][tag]) + ' '
                if no_tags:
                    mystr += 'No tags found'
                if toWrite:
                    self.listWidget.addItem(mystr)

    def _get_unclassified(self):
        to_classify = []
        for folder in self.parsed_files:
            for file in folder:
                no_tag = True
                for tag in folder[file]:
                    if folder[file][tag] > 0:
                        no_tag = False
                        break
                if no_tag:
                    to_classify.append(file)
        return to_classify

    def _tag_map_file(self):
        tag_map = {}
        for folder in self.parsed_files:
            for file in folder:
                for tag in folder[file]:
                    if folder[file][tag] > 0:
                        if tag in tag_map:
                            tag_map.append(file)
                        else:
                            tag_map = [file]
        return tag_map

    def _update_user_map(self, file_name, new_tags):
        self._user_map[file_name] = new_tags

    # def update_tags(self, file, new_tags):
    #     for folder in self.parsed_files:

    def _refresh_user_defined(self):
        self.listWidget_2.clear()
        for file_name in self._user_map:
            mystr = ''
            tags = ''
            for tag in self._user_map[file_name]:
                tags += tag + ' '
            mystr = 'File ' + file_name + ' Tags: ' + tags
            self.listWidget_2.addItem(mystr)

    def _refresh_algorithm_defined(self, file_name):
        # print('IN REFRESH  ----> ', file_name)
        for folder in self.parsed_files:
            # print('In folder ', folder)
            if file_name in folder:
                folder.pop(file_name, None)
                # print('AFTER POP ', folder)
        self._put_algorithm_defined_list()

    def _build_popup(self, item):
        # files_to_classify = self._get_unclassified()
        self.popup = Ui_Dialog()
        self.Dialog = QtWidgets.QDialog()
        self.popup.setupUi(self.Dialog)
        self.Dialog.show()
        self.Dialog.setWindowTitle(item.text())
        self.Dialog.exec_()
        print('EDIT TEXT WAS ', self.popup.d_textEdit_2.toPlainText())
        new_tags = self._list_from_comma_text(self.popup.d_textEdit_2.toPlainText())
        file_name_end = item.text().find('->')
        file_name = item.text()[:file_name_end]
        self._update_user_map(file_name, new_tags)
        print('Chosen new tags ', new_tags)
        if new_tags != '':
            self._refresh_algorithm_defined(file_name)
            self._refresh_user_defined()
        # self.tag_popup = TagPopup(' ')
        # self.tag_popup.setGeometry(100, 200, 500, 500)
        # self.tag_popup.setWindowTitle(item.text())
        # self.tag_popup.show()

    def dump_to_file(self):
        fp = open('user_defined_drop.txt', 'w')
        print(json.dumps(self._user_map), file=fp)
        fp.close()

    def _clear_file(self):
        try:
            os.remove('user_defined_drop.txt')
        except:
            self._user_map = {}
            self._refresh_user_defined()
