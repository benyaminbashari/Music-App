# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setObjectName("login_form")
        login_form.resize(800, 600)
        self.login_widget = QtWidgets.QWidget(login_form)
        self.login_widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.login_widget.setStyleSheet("background-color: rgb(255,255,255);")
        self.login_widget.setObjectName("login_widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.login_widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(270, 310, 231, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sign_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sign_button.setStyleSheet("color: rgb(255,255,255); \n"
"background-color: rgb(0, 0, 0)\n"
"\n"
"\n"
"")
        self.sign_button.setObjectName("sign_button")
        self.gridLayout.addWidget(self.sign_button, 1, 0, 1, 1)
        self.register_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.register_button.setStyleSheet("color: rgb(255,255,255); \n"
"background-color: rgb(0, 0, 0)\n"
"\n"
"")
        self.register_button.setObjectName("register_button")
        self.gridLayout.addWidget(self.register_button, 1, 1, 1, 1)
        self.forgot_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.forgot_button.setStyleSheet("color: rgb(255,255,255); \n"
"background-color: rgb(0, 0, 0)\n"
"\n"
"")
        self.forgot_button.setObjectName("forgot_button")
        self.gridLayout.addWidget(self.forgot_button, 2, 0, 1, 2)
        self.error_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.gridLayout.addWidget(self.error_label, 0, 0, 1, 2)
        self.formLayoutWidget = QtWidgets.QWidget(self.login_widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(230, 70, 193, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.user_number_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.user_number_label.setText("")
        self.user_number_label.setObjectName("user_number_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.user_number_label)
        self.songs_number_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.songs_number_label.setText("")
        self.songs_number_label.setObjectName("songs_number_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.songs_number_label)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.login_widget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(270, 230, 231, 81))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.password_line = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.password_line.setStyleSheet("")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_line)
        self.username_line = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.username_line.setStyleSheet("")
        self.username_line.setObjectName("username_line")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_line)
        self.label_5 = QtWidgets.QLabel(self.login_widget)
        self.label_5.setGeometry(QtCore.QRect(270, 10, 401, 51))
        self.label_5.setObjectName("label_5")
        self.image_label = QtWidgets.QLabel(self.login_widget)
        self.image_label.setGeometry(QtCore.QRect(10, 10, 211, 201))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)

    def retranslateUi(self, login_form):
        _translate = QtCore.QCoreApplication.translate
        login_form.setWindowTitle(_translate("login_form", "Form"))
        self.sign_button.setText(_translate("login_form", "Sign In"))
        self.register_button.setText(_translate("login_form", "Register"))
        self.forgot_button.setText(_translate("login_form", "I forgot my password"))
        self.label.setText(_translate("login_form", "Number of Users"))
        self.label_3.setText(_translate("login_form", "Number of Songs"))
        self.label_2.setText(_translate("login_form", "Username"))
        self.label_4.setText(_translate("login_form", "Passoword"))
        self.label_5.setText(_translate("login_form", "Music Spot\n"
"- You can Register, and follow your favourite songs and singers.\n"
"- Create your own playlists and share it with your friends."))

