# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_name.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_search_name_form(object):
    def setupUi(self, search_name_form):
        search_name_form.setObjectName("search_name_form")
        search_name_form.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(search_name_form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 30, 711, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.username_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username_line.setObjectName("username_line")
        self.horizontalLayout.addWidget(self.username_line)
        self.search_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout.addWidget(self.search_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.error_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.result_line = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.result_line.setObjectName("result_line")
        self.horizontalLayout_2.addWidget(self.result_line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.back_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)

        self.retranslateUi(search_name_form)
        QtCore.QMetaObject.connectSlotsByName(search_name_form)

    def retranslateUi(self, search_name_form):
        _translate = QtCore.QCoreApplication.translate
        search_name_form.setWindowTitle(_translate("search_name_form", "Form"))
        self.label.setText(_translate("search_name_form", "Username:"))
        self.search_button.setText(_translate("search_name_form", "Search"))
        self.error_label.setText(_translate("search_name_form", "Error"))
        self.label_2.setText(_translate("search_name_form", "Result:"))
        self.back_button.setText(_translate("search_name_form", "Back"))

