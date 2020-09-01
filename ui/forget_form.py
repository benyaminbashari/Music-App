# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_forget_form(object):
    def setupUi(self, forget_form):
        forget_form.setObjectName("forget_form")
        forget_form.resize(800, 600)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(forget_form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(210, 120, 338, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.definition = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.definition.setObjectName("definition")
        self.verticalLayout_3.addWidget(self.definition)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.personal_question = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.personal_question.setObjectName("personal_question")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.personal_question)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.personal_answer = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.personal_answer.setObjectName("personal_answer")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.personal_answer)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button)
        self.ok_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.username_label = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.username_label.setObjectName("username_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.username_label)
        self.error_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.error_label)
        self.verticalLayout_3.addLayout(self.formLayout)

        self.retranslateUi(forget_form)
        QtCore.QMetaObject.connectSlotsByName(forget_form)

    def retranslateUi(self, forget_form):
        _translate = QtCore.QCoreApplication.translate
        forget_form.setWindowTitle(_translate("forget_form", "Form"))
        self.definition.setHtml(_translate("forget_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose your personal question, answer it and then press the OK button otherwise by pressing the back button go to the login page.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("forget_form", "Personal Question: "))
        self.label_2.setText(_translate("forget_form", "Answer: "))
        self.back_button.setText(_translate("forget_form", "Back"))
        self.ok_button.setText(_translate("forget_form", "OK"))
        self.label_3.setText(_translate("forget_form", "Username: "))

