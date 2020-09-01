# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_first_page_form(object):
    def setupUi(self, first_page_form):
        first_page_form.setObjectName("first_page_form")
        first_page_form.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(first_page_form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 140, 761, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.album_line = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.album_line.setObjectName("album_line")
        self.horizontalLayout.addWidget(self.album_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.music_line = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.music_line.setObjectName("music_line")
        self.horizontalLayout_2.addWidget(self.music_line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.playlist_line = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.playlist_line.setObjectName("playlist_line")
        self.horizontalLayout_3.addWidget(self.playlist_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.back_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)

        self.retranslateUi(first_page_form)
        QtCore.QMetaObject.connectSlotsByName(first_page_form)

    def retranslateUi(self, first_page_form):
        _translate = QtCore.QCoreApplication.translate
        first_page_form.setWindowTitle(_translate("first_page_form", "Form"))
        self.label.setText(_translate("first_page_form", "Album:"))
        self.label_2.setText(_translate("first_page_form", "Music:"))
        self.label_3.setText(_translate("first_page_form", "Playlist:"))
        self.back_button.setText(_translate("first_page_form", "Back"))

