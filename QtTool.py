#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtTool.py'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from test import Ui_Ui_translator
from YouDaoDictSpider import *

class UsingTest(QMainWindow,Ui_Ui_translator):
    def __init__(self, *args, **kwargs):
        super(UsingTest, self).__init__(*args,**kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.translate)

    def translate(self):
        word = self.lineEdit.text()
        if not word:
            self.textBrowser.setText("请输入单词！")
            return

        self.textBrowser.clear()
        result = attack_yd(word)
        if result.get('errorCode') == 0:
            trans_couple = result['translateResult'][0][0]
            #self.textBrowser.append(trans_couple.get('src'))
            self.textBrowser.append(trans_couple.get('tgt'))

            if result.get('smartResult'):
                info_list = result['smartResult'].get('entries')
                for info in info_list:
                    if not info:
                        continue
                    self.textBrowser.append(info.strip())

if __name__=='__main__':
    app = QApplication(sys.argv)
    widget = UsingTest()
    widget.show()
    sys.exit(app.exec_())