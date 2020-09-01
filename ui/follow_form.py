# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'follow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_follow_form(object):
    def setupUi(self, follow_form):
        follow_form.setObjectName("follow_form")
        follow_form.resize(800, 600)
        self.back_button = QtWidgets.QPushButton(follow_form)
        self.back_button.setGeometry(QtCore.QRect(700, 10, 89, 25))
        self.back_button.setObjectName("back_button")
        self.gridLayoutWidget = QtWidgets.QWidget(follow_form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(28, 70, 771, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.users_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.users_list.setObjectName("users_list")
        self.gridLayout.addWidget(self.users_list, 0, 1, 1, 1)
        self.followers_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.followers_list.setObjectName("followers_list")
        self.gridLayout.addWidget(self.followers_list, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.followings_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.followings_list.setObjectName("followings_list")
        self.gridLayout.addWidget(self.followings_list, 1, 1, 1, 1)
        self.follow_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.follow_button.setObjectName("follow_button")
        self.gridLayout.addWidget(self.follow_button, 1, 3, 1, 1)
        self.followable_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.followable_combo.setObjectName("followable_combo")
        self.gridLayout.addWidget(self.followable_combo, 1, 2, 1, 1)

        self.retranslateUi(follow_form)
        QtCore.QMetaObject.connectSlotsByName(follow_form)

    def retranslateUi(self, follow_form):
        _translate = QtCore.QCoreApplication.translate
        follow_form.setWindowTitle(_translate("follow_form", "Form"))
        self.back_button.setText(_translate("follow_form", "Back"))
        self.label.setText(_translate("follow_form", "Users"))
        self.label_2.setText(_translate("follow_form", "Followers"))
        self.label_3.setText(_translate("follow_form", "Followings"))
        self.follow_button.setText(_translate("follow_form", "Follow"))

