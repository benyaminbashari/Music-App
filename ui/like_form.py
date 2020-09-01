# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'like.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_like_form(object):
    def setupUi(self, like_form):
        like_form.setObjectName("like_form")
        like_form.resize(800, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(like_form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(108, 160, 561, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.music_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.music_list.setObjectName("music_list")
        self.gridLayout.addWidget(self.music_list, 0, 1, 1, 1)
        self.liked_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.liked_list.setObjectName("liked_list")
        self.gridLayout.addWidget(self.liked_list, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.like_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.like_button.setObjectName("like_button")
        self.gridLayout.addWidget(self.like_button, 1, 1, 1, 1)
        self.music_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.music_combo.setObjectName("music_combo")
        self.gridLayout.addWidget(self.music_combo, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.back_button = QtWidgets.QPushButton(like_form)
        self.back_button.setGeometry(QtCore.QRect(560, 40, 89, 25))
        self.back_button.setObjectName("back_button")

        self.retranslateUi(like_form)
        QtCore.QMetaObject.connectSlotsByName(like_form)

    def retranslateUi(self, like_form):
        _translate = QtCore.QCoreApplication.translate
        like_form.setWindowTitle(_translate("like_form", "Form"))
        self.label.setText(_translate("like_form", "Musics"))
        self.like_button.setText(_translate("like_form", "Like"))
        self.label_2.setText(_translate("like_form", "Liked Musics"))
        self.back_button.setText(_translate("like_form", "Back"))

