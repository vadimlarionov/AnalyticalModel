# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyticalmodel.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnalyticalModel(object):
    def setupUi(self, AnalyticalModel):
        AnalyticalModel.setObjectName("AnalyticalModel")
        AnalyticalModel.setWindowModality(QtCore.Qt.NonModal)
        AnalyticalModel.setEnabled(True)
        AnalyticalModel.resize(988, 552)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("analytics.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AnalyticalModel.setWindowIcon(icon)
        AnalyticalModel.setSizeGripEnabled(True)
        AnalyticalModel.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(AnalyticalModel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(AnalyticalModel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.addVariantButton = QtWidgets.QPushButton(AnalyticalModel)
        self.addVariantButton.setObjectName("addVariantButton")
        self.gridLayout.addWidget(self.addVariantButton, 2, 2, 1, 1)
        self.deleteVariantButton = QtWidgets.QPushButton(AnalyticalModel)
        self.deleteVariantButton.setObjectName("deleteVariantButton")
        self.gridLayout.addWidget(self.deleteVariantButton, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(AnalyticalModel)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(AnalyticalModel)
        QtCore.QMetaObject.connectSlotsByName(AnalyticalModel)

    def retranslateUi(self, AnalyticalModel):
        _translate = QtCore.QCoreApplication.translate
        AnalyticalModel.setWindowTitle(_translate("AnalyticalModel", "Аналитическая модель"))
        self.addVariantButton.setText(_translate("AnalyticalModel", "Добавить"))
        self.deleteVariantButton.setText(_translate("AnalyticalModel", "Удалить"))
        self.label.setText(_translate("AnalyticalModel", "Исходные данные"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnalyticalModel = QtWidgets.QDialog()
    ui = Ui_AnalyticalModel()
    ui.setupUi(AnalyticalModel)
    AnalyticalModel.show()
    sys.exit(app.exec_())

