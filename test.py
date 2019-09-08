# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ui_translator(object):
    def setupUi(self, Ui_translator):
        Ui_translator.setObjectName("Ui_translator")
        Ui_translator.resize(400, 380)
        self.pushButton = QtWidgets.QPushButton(Ui_translator)
        self.pushButton.setGeometry(QtCore.QRect(140, 90, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Ui_translator)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 361, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Ui_translator)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Ui_translator)
        self.textBrowser.setGeometry(QtCore.QRect(20, 160, 361, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Ui_translator)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 71, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Ui_translator)
        QtCore.QMetaObject.connectSlotsByName(Ui_translator)

    def retranslateUi(self, Ui_translator):
        _translate = QtCore.QCoreApplication.translate
        Ui_translator.setWindowTitle(_translate("Ui_translator", "有道翻译"))
        self.pushButton.setText(_translate("Ui_translator", "翻译"))
        self.label.setText(_translate("Ui_translator", "请输入要翻译的单词："))
        self.label_2.setText(_translate("Ui_translator", "翻译结果："))

