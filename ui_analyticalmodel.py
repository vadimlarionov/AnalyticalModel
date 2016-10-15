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
        AnalyticalModel.resize(1160, 792)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("analytics.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AnalyticalModel.setWindowIcon(icon)
        AnalyticalModel.setSizeGripEnabled(True)
        AnalyticalModel.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(AnalyticalModel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.inputTableWidget = QtWidgets.QTableWidget(AnalyticalModel)
        self.inputTableWidget.setObjectName("inputTableWidget")
        self.inputTableWidget.setColumnCount(0)
        self.inputTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.inputTableWidget, 1, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(AnalyticalModel)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.calculateButton = QtWidgets.QPushButton(AnalyticalModel)
        self.calculateButton.setObjectName("calculateButton")
        self.gridLayout.addWidget(self.calculateButton, 2, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
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
        self.outputTableWidget = QtWidgets.QTableWidget(AnalyticalModel)
        self.outputTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.outputTableWidget.setObjectName("outputTableWidget")
        self.outputTableWidget.setColumnCount(0)
        self.outputTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.outputTableWidget, 4, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(AnalyticalModel)
        QtCore.QMetaObject.connectSlotsByName(AnalyticalModel)

    def retranslateUi(self, AnalyticalModel):
        _translate = QtCore.QCoreApplication.translate
        AnalyticalModel.setWindowTitle(_translate("AnalyticalModel", "Аналитическая модель"))
        self.label_2.setText(_translate("AnalyticalModel", "Результаты моделирования"))
        self.calculateButton.setText(_translate("AnalyticalModel", "Моделирование"))
        self.addVariantButton.setText(_translate("AnalyticalModel", "Добавить вариант"))
        self.deleteVariantButton.setText(_translate("AnalyticalModel", "Удалить вариант"))
        self.label.setText(_translate("AnalyticalModel", "Исходные данные"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnalyticalModel = QtWidgets.QDialog()
    ui = Ui_AnalyticalModel()
    ui.setupUi(AnalyticalModel)
    AnalyticalModel.show()
    sys.exit(app.exec_())

