# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_error_form(object):
    def setupUi(self, error_form):
        error_form.setObjectName("error_form")
        error_form.resize(300, 101)
        error_form.setStyleSheet("background-color: (255,255,255)")
        self.verticalLayoutWidget = QtWidgets.QWidget(error_form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.error_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        self.ok_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ok_button.setObjectName("ok_button")
        self.verticalLayout.addWidget(self.ok_button)

        self.retranslateUi(error_form)
        QtCore.QMetaObject.connectSlotsByName(error_form)

    def retranslateUi(self, error_form):
        _translate = QtCore.QCoreApplication.translate
        error_form.setWindowTitle(_translate("error_form", "Form"))
        self.ok_button.setText(_translate("error_form", "OK"))

