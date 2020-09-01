# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_rate_form(object):
    def setupUi(self, rate_form):
        rate_form.setObjectName("rate_form")
        rate_form.resize(800, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(rate_form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 63, 621, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.album_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.album_list.setObjectName("album_list")
        self.gridLayout.addWidget(self.album_list, 1, 1, 1, 1)
        self.rate_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rate_button.setObjectName("rate_button")
        self.gridLayout.addWidget(self.rate_button, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.star_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.star_line.setObjectName("star_line")
        self.gridLayout.addWidget(self.star_line, 4, 1, 1, 1)
        self.album_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.album_combo.setObjectName("album_combo")
        self.gridLayout.addWidget(self.album_combo, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.follow_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.follow_button.setObjectName("follow_button")
        self.gridLayout.addWidget(self.follow_button, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.fol_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.fol_list.setObjectName("fol_list")
        self.gridLayout.addWidget(self.fol_list, 1, 3, 1, 1)
        self.back_button = QtWidgets.QPushButton(rate_form)
        self.back_button.setGeometry(QtCore.QRect(630, 10, 89, 25))
        self.back_button.setObjectName("back_button")

        self.retranslateUi(rate_form)
        QtCore.QMetaObject.connectSlotsByName(rate_form)

    def retranslateUi(self, rate_form):
        _translate = QtCore.QCoreApplication.translate
        rate_form.setWindowTitle(_translate("rate_form", "Form"))
        self.rate_button.setText(_translate("rate_form", "Rate"))
        self.label.setText(_translate("rate_form", "Albums and Playlist"))
        self.label_3.setText(_translate("rate_form", "Followings Albums"))
        self.follow_button.setText(_translate("rate_form", "Follow"))
        self.label_2.setText(_translate("rate_form", "Stars:"))
        self.back_button.setText(_translate("rate_form", "Back"))

