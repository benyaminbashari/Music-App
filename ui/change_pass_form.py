# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_pass.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_change_pass_form(object):
    def setupUi(self, change_pass_form):
        change_pass_form.setObjectName("change_pass_form")
        change_pass_form.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(change_pass_form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 110, 721, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.curren_pass_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.curren_pass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.curren_pass_line.setObjectName("curren_pass_line")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.curren_pass_line)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.new_pass_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.new_pass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pass_line.setObjectName("new_pass_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.new_pass_line)
        self.verticalLayout.addLayout(self.formLayout)
        self.error_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        self.ok_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ok_button.setObjectName("ok_button")
        self.verticalLayout.addWidget(self.ok_button)
        self.back_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)

        self.retranslateUi(change_pass_form)
        QtCore.QMetaObject.connectSlotsByName(change_pass_form)

    def retranslateUi(self, change_pass_form):
        _translate = QtCore.QCoreApplication.translate
        change_pass_form.setWindowTitle(_translate("change_pass_form", "Form"))
        self.label.setText(_translate("change_pass_form", "Current password:"))
        self.label_2.setText(_translate("change_pass_form", "New password:"))
        self.ok_button.setText(_translate("change_pass_form", "Ok"))
        self.back_button.setText(_translate("change_pass_form", "Back"))

