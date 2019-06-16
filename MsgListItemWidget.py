import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget


class MsgListItemWidget(QWidget):
    def __init__(self, parent=None):
        super(MsgListItemWidget, self).__init__(parent)

        # self.horizontalLayoutWidget = QtWidgets.QWidget(parent)
        # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 100, 160, 80))
        # self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        # self.horizontalLayout = QtWidgets.QHBoxLayout(parent)
        # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout.setObjectName("horizontalLayout")
        #
        # self.ProfilePhoto = QtWidgets.QLabel()
        # self.ProfilePhoto.setObjectName("ProfilePhoto")
        # self.horizontalLayout.addWidget(self.ProfilePhoto)
        #
        # self.verticalLayout = QtWidgets.QVBoxLayout()
        # self.verticalLayout.setObjectName("verticalLayout")
        #
        # self.Nickname = QtWidgets.QLabel()
        # self.Nickname.setObjectName("Nickname")
        # self.verticalLayout.addWidget(self.Nickname)
        #
        # self.Message = QtWidgets.QLabel()
        # self.Message.setObjectName("Message")
        # self.verticalLayout.addWidget(self.Message)
        #
        # self.horizontalLayout.addLayout(self.verticalLayout)

        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.Nickname = QtWidgets.QLabel()
        self.Message = QtWidgets.QLabel()
        self.textQVBoxLayout.addWidget(self.Nickname)
        self.textQVBoxLayout.addWidget(self.Message)
        self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        self.ProfilePhoto = QtWidgets.QLabel()
        # self.ProfilePhoto.resize(100,60)
        self.allQHBoxLayout.addWidget(self.ProfilePhoto, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.Nickname.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.Message.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setProfilePhoto(self, img):
        self.ProfilePhoto.setPixmap(QtGui.QPixmap(img))
        # self.ProfilePhoto.setScaledContents(True)

    def setNickName(self, name):
        self.Nickname.setText(name)

    def setMessage(self, msg):
        self.Message.setText(msg)

    # def setTime(self, time):
    #     self.Time.setText(time)

    def setAllInfo(self, img, name, msg):
        self.setProfilePhoto(img)
        self.setNickName(name)
        self.setMessage(msg)