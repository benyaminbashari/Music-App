# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_search_form(object):
    def setupUi(self, search_form):
        search_form.setObjectName("search_form")
        search_form.resize(800, 600)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(search_form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 731, 441))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name_search_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.name_search_line.setObjectName("name_search_line")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_search_line)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.result_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.result_list.setObjectName("result_list")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.result_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.error_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.error_label)
        self.ok_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ok_button.setObjectName("ok_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ok_button)
        self.back_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.back_button.setObjectName("back_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.back_button)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_name_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.search_name_button.setObjectName("search_name_button")
        self.horizontalLayout.addWidget(self.search_name_button)
        self.search_album_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.search_album_button.setObjectName("search_album_button")
        self.horizontalLayout.addWidget(self.search_album_button)
        self.pushBusearch_music_buttontton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushBusearch_music_buttontton_3.setObjectName("pushBusearch_music_buttontton_3")
        self.horizontalLayout.addWidget(self.pushBusearch_music_buttontton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(search_form)
        QtCore.QMetaObject.connectSlotsByName(search_form)

    def retranslateUi(self, search_form):
        _translate = QtCore.QCoreApplication.translate
        search_form.setWindowTitle(_translate("search_form", "Form"))
        self.label.setText(_translate("search_form", "Simple search:"))
        self.label_2.setText(_translate("search_form", "Result:"))
        self.ok_button.setText(_translate("search_form", "Ok"))
        self.back_button.setText(_translate("search_form", "Back"))
        self.search_name_button.setText(_translate("search_form", "Search with username"))
        self.search_album_button.setText(_translate("search_form", "Search Album"))
        self.pushBusearch_music_buttontton_3.setText(_translate("search_form", "Search music"))

