# WeChatHandler: Using wxpy module to handle WeChat operation

from wxpy import *


class MessageHandler:

    def __init__(self):
        def qr_callback(uuid, status, qrcode):
            print("UUID:" + uuid + "\nStatus:" + status + "\n" + qrcode)
        # bot = Bot(qr_path="/home/xiangyi/Desktop/PyWeChat-GUI/",qr_callback=qr_callback)
        self.bot = Bot()

    def getChatList(self):
        return self.bot.chats()

    def getFriendList(self):
        return self.bot.friends()

    def getGroupList(self):
        return self.bot.groups()

    def getMPList(self):
        return self.bot.mps()

    def getMsgList(self):
        return self.bot.messages

if __name__ == '__main__':
    msgHandler = MessageHandler()