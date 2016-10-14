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
        AnalyticalModel.resize(590, 355)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("analytics.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AnalyticalModel.setWindowIcon(icon)
        AnalyticalModel.setSizeGripEnabled(True)
        AnalyticalModel.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(AnalyticalModel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(AnalyticalModel)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(AnalyticalModel)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(AnalyticalModel)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(AnalyticalModel)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(AnalyticalModel)
        QtCore.QMetaObject.connectSlotsByName(AnalyticalModel)

    def retranslateUi(self, AnalyticalModel):
        _translate = QtCore.QCoreApplication.translate
        AnalyticalModel.setWindowTitle(_translate("AnalyticalModel", "Аналитическая модель"))
        self.pushButton.setText(_translate("AnalyticalModel", "PushButton"))
        self.pushButton_2.setText(_translate("AnalyticalModel", "PushButton"))
        self.pushButton_3.setText(_translate("AnalyticalModel", "PushButton"))
        self.pushButton_4.setText(_translate("AnalyticalModel", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnalyticalModel = QtWidgets.QDialog()
    ui = Ui_AnalyticalModel()
    ui.setupUi(AnalyticalModel)
    AnalyticalModel.show()
    sys.exit(app.exec_())

