# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MsgListItemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(400, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 100, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ProfilePhoto = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ProfilePhoto.setObjectName("ProfilePhoto")
        self.horizontalLayout.addWidget(self.ProfilePhoto)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Nickname = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Nickname.setObjectName("Nickname")
        self.verticalLayout.addWidget(self.Nickname)
        self.Message = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Message.setObjectName("Message")
        self.verticalLayout.addWidget(self.Message)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ProfilePhoto.setText(_translate("Form", "TextLabel"))
        self.Nickname.setText(_translate("Form", "TextLabel"))
        self.Message.setText(_translate("Form", "TextLabel"))


