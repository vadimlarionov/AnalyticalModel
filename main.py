# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from ui_analyticalmodel import Ui_AnalyticalModel
from parameters import *
from conf import *


class AnalyticalModelView(QDialog, Ui_AnalyticalModel):
    count = 0

    def __init__(self):
        super(AnalyticalModelView, self).__init__()
        self.setupUi(self)
        self.init_table(5)
        self.addVariantButton.clicked.connect(self.add_variant)
        self.deleteVariantButton.clicked.connect(self.delete_variant)

    def init_table(self, number_variants):
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem(' '))
        for x in range(number_variants):
            self.add_variant()

        for row, param in input_params.items():
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(param.text))
            column = 1
            for value in param.values:
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(value)))
                column += 1

    def add_variant(self):
        column = self.tableWidget.columnCount()
        if column <= max_variants:
            self.tableWidget.insertColumn(column)
            self.tableWidget.setHorizontalHeaderItem(column, QTableWidgetItem('В' + str(column)))

    def delete_variant(self):
        column = self.tableWidget.columnCount()
        if column > 1:
            self.tableWidget.removeColumn(column - 1)

    def get_data(self, param, variant):
        return self.tableWidget.item(param.row, variant).text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnalyticalModelView()
    window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowMinimizeButtonHint |
                          QtCore.Qt.WindowMaximizeButtonHint)
    window.show()
    sys.exit(app.exec_())
