# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_img_message
from utils import send_button_message
#import utils

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
################# is going to #################
    def is_going_to_menu(self, event):
        # if event.get("postback"):
        #     if event["postback"].get("payload"):
        #         text = event['postback']['payload']
        #     return text == 'sreturn'
                    #print(text)
        if event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text.decode('utf-8') == 'hi'
        else: return False

    def is_going_to_signup_info(self, event):
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'signup'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text.decode('utf-8') == '報名資訊'.decode('utf-8')
        else: return False

    def is_going_to_introduction(self, event):
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'introduction'
                    #print(text)
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text.decode('utf-8') == '營隊介紹'.decode('utf-8')
        else: return False

    def is_going_to_download(self, event):
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'download'
                    #print(text)
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text.decode('utf-8') == '附件下載'.decode('utf-8')
        else: return False

    def back_to_menu(self, event):
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'sreturn'
                    #print(text)
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text.decode('utf-8') == '返回'.decode('utf-8')
        else: return False
    # def is_going_to_traffic(self, event):
    #     if event.get("message"):
    #         if event["message"].get("text"):
    #             text = event['message']['text']
    #         #print(text)
    #         return text.decode('utf-8') == '交通方式'.decode('utf-8')
    #     return False

################# on entert #################

    def on_enter_menu(self, event):
        print("I'm entering menu")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "this is menu")
        button = [
            {
                "type":"postback",
                "title":"報名資訊".decode('utf-8'),
                "payload":"signup"
            },
            {
                "type":"postback",
                "title":"營隊介紹".decode('utf-8'),
                "payload":"introduction"
            },
            {
                "type":"postback",
                "title":"附件下載".decode('utf-8'),
                "payload":"download"
            }
        ]
        send_button_message(sender_id, "這裡是2019成大資工營，歡迎使用聊天機器人！\n如果想知道報名相關的資訊，請輸入「報名資訊」。\n想知道更多我們的活動內容，請輸入「營隊介紹」。\n想要下載相關的檔案附件，請輸入「附件下載」。", button)
        #self.go_back()

    def on_enter_signup_info(self, event):
        print("I'm entering 報名資訊")
        button = [
            {
                "type":"postback",
                "title":"返回".decode('utf-8'),
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_text_message(sender_id, "報名資訊")
        #send_img_message(sender_id, "https://i.imgur.com/lG6fUoB.jpg")
        send_button_message(sender_id, "報名網址".decode('utf-8'), button)
        #self.go_back(event)

    def on_enter_introduction(self, event):
        print("I'm entering 營隊介紹")
        button = [
            {
                "type":"postback",
                "title":"返回".decode('utf-8'),
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_text_message(sender_id, "營隊介紹")
        send_button_message(sender_id, "介紹".decode('utf-8'), button)
        #self.go_back(event)

    def on_enter_download(self, event):
        print("I'm entering 附件下載")
        button = [
            {
                "type":"postback",
                "title":"返回".decode('utf-8'),
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_text_message(sender_id, "附件下載")
        send_button_message(sender_id, "下載".decode('utf-8'), button)
        #self.go_back(event)

    # def on_enter_traffic(self, event):
    #     print("I'm entering 交通方式")

    #     sender_id = event['sender']['id']
    #     send_text_message(sender_id, "交通方式")
    #     self.go_back(event)
################# on exit #################
    def on_exit_signup_info(self, event):
        print('Leaving 報名資訊')

    def on_exit_introduction(self, event):
        print('Leaving 營隊介紹')

    def on_exit_download(self, event):
        print('Leaving 附件下載')

    # def on_exit_traffic(self, event):
    #     print('Leaving 交通方式')
