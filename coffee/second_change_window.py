# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_change_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 240, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 240, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 20, 161, 21))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(210, 60, 171, 21))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 171, 31))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(260, 120, 131, 21))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 251, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 171, 31))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(210, 180, 171, 21))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Изменить"))
        self.pushButton_2.setText(_translate("Form", "Выйти"))
        self.label.setText(_translate("Form", "Что хотите изменить?"))
        self.label_2.setText(_translate("Form", "Введите название кофе?"))
        self.label_3.setText(_translate("Form", "Какое поле хотите изменить (номер) ?"))
        self.label_4.setText(_translate("Form", "Что хотите добавить?"))
