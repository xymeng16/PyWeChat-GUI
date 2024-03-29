# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import sys
from MessageHandler import *
from MsgListItemWidget import *
test = [("1.jpg", "a", "aaaaaaaaa", "14:30"), ("1.jpg", "a", "aaaaaaaaa", "14:30"), ("1.jpg", "b", "aaaaaaaaa", "14:30")]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.msgListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.msgListWidget.setGeometry(QtCore.QRect(70, 0, 191, 631))
        self.msgListWidget.setObjectName("msgListWidget")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 470, 431, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")



        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyWeChat"))

        # self.msgListItemWidget = MsgListItemWidget(parent=self.msgListWidget)
            # msgListItemWidget.setAllInfo(img, name, msg)
            #
            # msgListWidgetItem = QtWidgets.QListWidgetItem(self.msgListWidget) # As a container
            # msgListWidgetItem.setSizeHint(msgListItemWidget.sizeHint())
            #
            # self.msgListWidget.addItem(msgListWidgetItem)
            # self.msgListWidget.setItemWidget(msgListWidgetItem, msgListItemWidget)
class MessageThread(QThread):
    newMessage = pyqtSignal(Message, list)

    def __init__(self):
        super(MessageThread,self).__init__()

    def run(self):
        msgHandler = MessageHandler()
        # self.trigger.emit(msgHandler)
        @msgHandler.bot.register()
        def addMessage(msg):

            print("Msg:\"" + msg.text + "\" received from " +
                  msg.sender.remark_name + " is gonna pass to the main thread.")
            # msgListItemWidget = MsgListItemWidget(parent=ui.msgListWidget)
            # msgListItemWidget.setAllInfo("1.jpg", msg.sender.remark_name, msg.text)
            # msgListWidgetItem = QtWidgets.QListWidgetItem(ui.msgListWidget)  # As a container
            # msgListWidgetItem.setSizeHint(msgListItemWidget.sizeHint())
            #
            # ui.msgListWidget.addItem(msgListWidgetItem)
            # ui.msgListWidget.setItemWidget(msgListWidgetItem, msgListItemWidget)
            self.newMessage.emit(msg, msgHandler.bot.messages)

        msgHandler.botJoin()

def updateMsg(msg, messages):
    print("Msg:\"" + msg.text + "\" received from " +
                  msg.sender.remark_name + " is added to the list widget.")
    # TODO: Checking if msg.sender is in messages and add profile photos.
    msgListItemWidget = MsgListItemWidget(parent=ui.msgListWidget)
    msgListItemWidget.setAllInfo("1.jpg", msg.sender.remark_name, msg.text)
    msgListWidgetItem = QtWidgets.QListWidgetItem(ui.msgListWidget) # As a container
    msgListWidgetItem.setSizeHint(msgListItemWidget.sizeHint())

    ui.msgListWidget.addItem(msgListWidgetItem)
    ui.msgListWidget.setItemWidget(msgListWidgetItem, msgListItemWidget)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # msgHandler = MessageHandler()
    # MainWindow.show()
    # MainWindow.hide()
    msgThread = MessageThread()
    msgThread.newMessage.connect(updateMsg)

    MainWindow.show()

    msgThread.start()

    sys.exit(app.exec_())
