# WeChatHandler: Using wxpy module to handle WeChat operation

from wxpy import *
class MessageHandler():
    def __init__(self):
        def qr_callback(uuid, status, qrcode):
            print("UUID:" + uuid + "\nStatus:" + status + "\n" + qrcode)
        # bot = Bot(qr_path="/home/xiangyi/Desktop/PyWeChat-GUI/",qr_callback=qr_callback)
        bot = Bot()

if __name__ == '__main__':
    msgHandler = MessageHandler()