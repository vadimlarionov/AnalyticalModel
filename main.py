# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from ui_analyticalmodel import Ui_AnalyticalModel


class AnalyticalModelView(QDialog, Ui_AnalyticalModel):

    def __init__(self):
        super(AnalyticalModelView, self).__init__()
        self.setupUi(self)
        self.foo()

    def foo(self):
        # button = QPushButton('Hello')
        # self.gridLayout.addWidget(button)
        # button1 = QPushButton('Run!')
        # self.gridLayout.addWidget(button1)
        #
        # button2 = QPushButton('Run 2!')
        # self.gridLayout.addWidget(button2, 1, 0)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnalyticalModelView()
    window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowMinimizeButtonHint |
                          QtCore.Qt.WindowMaximizeButtonHint)
    window.show()
    sys.exit(app.exec_())
