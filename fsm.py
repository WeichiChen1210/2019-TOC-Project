import sys

from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_img_message
from utils import send_button_message
from utils import quick_reply_button
#import utils

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
################# is going to #################
    def is_going_to_menu(self, event):
        text = ''
        # if event.get("postback"):
        #     if event["postback"].get("payload"):
        #         text = event['postback']['payload']
        #     return text == 'sreturn'
                    #print(text)
        if event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == 'hi' or text == 'Hi'
        else: return False

    def is_going_to_signup_info(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'signup'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '報名資訊' or text == '報名'
        else: return False

    def is_going_to_introduction(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'introduction'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '營隊介紹' or text == '介紹'
        else: return False

    def is_going_to_download(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'download'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '附件下載' or text == '下載'
        else: return False

    def is_going_to_calendar(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'calendar'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '行事曆'
        else: return False

    def is_going_to_contact(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'contact_info'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '聯絡資訊'
        else: return False

    def is_going_to_question(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'other'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '其他問題'
        else: return False

    def is_going_to_inform(self, event):
        text = ''
        if event.get("message"):
            if event["message"].get("quick_reply"):
                if event["message"]["quick_reply"].get("payload"):
                    text = event['message']['quick_reply']['payload']
                return text == 'inform'
            elif event["message"].get("text"):
                text = event['message']['text']
                return text == '營前通知' or text == '通知'
        else: return False
    
    def is_going_to_leave(self, event):
        text = ''
        if event.get("message"):
            if event["message"].get("quick_reply"):
                if event["message"]["quick_reply"].get("payload"):
                    text = event['message']['quick_reply']['payload']
                return text == 'leave'
            elif event["message"].get("text"):
                text = event['message']['text']
                return text == '離營切結書' or text == '切結書'
        else: return False

    def is_going_to_step(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'step'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '填報名表'
        else: return False

    def is_going_to_money(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'money'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '匯款資訊'
        else: return False

    def is_going_to_email(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'email'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '寄信'
        else: return False

    def back_to_menu(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'sreturn'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '返回'
        else: return False

    def back_to_download(self, event):
        text = ''
        if event.get("postback"):
            if event["postback"].get("payload"):
                text = event['postback']['payload']
            return text == 'dreturn'
        elif event.get("message"):
            if event["message"].get("text"):
                text = event['message']['text']
            return text == '返回下載'
        else: return False
            
################# on entert #################

    def on_enter_menu(self, event):
        print("I'm entering menu")

        sender_id = event['sender']['id']
        #send_text_message(sender_id, "this is menu")
        button = [
            # {
            #     "type":"postback",
            #     "title":"附件下載",
            #     "payload":"download"
            # },
            {
                "type":"postback",
                "title":"行事曆",
                "payload":"calendar"
            },
            {
                "type":"postback",
                "title":"聯絡資訊",
                "payload":"contact_info"
            },
            {
                "type":"postback",
                "title":"其他問題",
                "payload":"other"
            }
        ]
        send_img_message(sender_id, "https://i.imgur.com/TvjzlFP.png")
        send_button_message(sender_id, "這裡是2019成大資工營，歡迎使用聊天機器人！\n如果想知道報名相關的資訊，請輸入「報名資訊」。\n想知道更多我們的活動內容，請輸入「營隊介紹」。\n想要下載相關的檔案附件，請輸入「附件下載」。\n或是點選按鈕進入其他功能～", button)
        #self.go_back()

    def on_enter_signup_info(self, event):
        print("I'm entering 報名資訊")
        button = [
            {
                "type":"postback",
                "title":"第一步：填寫報名表",
                "payload":"step"
            },
            {
                "type":"postback",
                "title":"返回主目錄",
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        #send_text_message(sender_id, "報名資訊")
        #send_img_message(sender_id, "https://i.imgur.com/lG6fUoB.jpg")
        send_button_message(sender_id, "非常歡迎報名成大資訊營！\n以下是報名的相關資訊以及步驟，請按第一步開始教學。\n**報名完成後不一定代表會錄取，因人數有上限，我們會根據報名表內容進行篩選！**", button)
        #self.go_back(event)

    def on_enter_introduction(self, event):
        print("I'm entering 營隊介紹")
        button = [
            {
                "type":"postback",
                "title":"返回主目錄",
                "payload":"sreturn"
            },
            {
                "type":"web_url",
                "url":"http://www.csie.ncku.edu.tw/ncku_csie/",
                "title":"成大資訊工程學系",
                "webview_height_ratio": "full"
            }
        ]
        sender_id = event['sender']['id']
        #send_text_message(sender_id, "營隊介紹")
        send_button_message(sender_id, "成大資訊營是由成功大學資訊系所舉辦的營隊，於暑假期間舉辦，為期七天，為一面對所有高中生的營隊。\n活動宗旨是帶領高中生體驗精彩的大學生活、認識資工系學生平時所學，以及探索各資訊相關領域和未來發展趨勢。\n在營期間將會有各式室內及戶外活動和基礎的程式課程，在營期的最後會讓學員們利用這些天所學舉行一個屬於自己的成果發表，適合對於寫程式有興趣但沒有經驗、不知該從何學起，以及想體驗大學生活的高中生參加！\n主要課程內容：\n1. C++:從0開始把程式的基礎概念交給你！\n2. Unity遊戲製作：自己動手做一個簡單的遊戲！\n3. 領域探索：讓學長姐用淺顯易懂的語言來解釋大數據，人工智慧等熱門的名詞！\n若想更深入了解本系，請點擊下面的按鈕。", button)
        
        #self.go_back(event)

    def on_enter_download(self, event):
        print("I'm entering 附件下載")
        button = [
            {
                "type":"postback",
                "title":"返回主目錄",
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        #send_text_message(sender_id, "附件下載")
        #send_file_message(sender_id, "https://docs.google.com/document/d/1XQ-mJVqlHaw_xtw96p7kjV8L9FOIPTpSr-Ganr_pYdc/edit")
        send_button_message(sender_id, "總共有兩個檔案：\n1. 營前通知\n2. 離營切結書\n請輸入或點擊下載\n", button)
        quick_reply_button(sender_id, "請選擇")
        #self.go_back(event)

    def on_enter_calendar(self, event):
        print("I'm entering 行事曆")
        button = [
            {
                "type":"postback",
                "title":"返回主目錄",
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        #send_text_message(sender_id, "行事曆")
        send_button_message(sender_id, "以下是今年成大資工營的行事曆：\n4/1\t\t開始報名\n4/24\t\t第一階段報名截止\n5/8\t\t第一階段匯款截止\n5/14\t\t第二階段報名截止\n5/30\t\t第二階段匯款截止\n6/11\t\t備取匯款截止\n6/13\t\t公布最終錄取名單\n7/12~7/17\t營期\n", button)

    def on_enter_contact(self, event):
        print("I'm entering 聯絡方式")
        button = [
            {
                "type":"postback",
                "title":"返回主目錄",
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_button_message(sender_id, "2019成大資訊營-福爾摩資\n總召：梁竣傑\nhttps://www.facebook.com/profile.php?id=100000616770247 \n電話：0978682869\n地址：台南市東區大學路1號\n網站：https://2018nckucsiecamp.wixsite.com/2018nckucsiecamp \n信箱：2018nckucsiecamp@gmail.com", button)

    def on_enter_question(self, event):
        print("I'm entering 其他問題")
        button = [
            {
                "type":"postback",
                "title":"返回主目錄",
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_button_message(sender_id, "如果有其他的問題，請在這裡發問，我們會盡快回覆您。", button)

    def on_enter_inform(self, event):
        print("I'm entering 營前通知")
        button = [
            {
                "type":"postback",
                "title":"返回下載",
                "payload":"dreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_button_message(sender_id, "營前通知：\nhttps://docs.google.com/document/d/1XQ-mJVqlHaw_xtw96p7kjV8L9FOIPTpSr-Ganr_pYdc/edit", button)

    def on_enter_leave(self, event):
        print("I'm entering 離營切結書")
        button = [
            {
                "type":"postback",
                "title":"返回下載",
                "payload":"dreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_button_message(sender_id, "離營切結書：\nhttps://docs.google.com/document/d/1lUYx301-YGoZgzdM04mwEsAUyJL3tglnMVZr0B7mspg/edit", button)
    
    def on_enter_step(self, event):
        print("I'm entering 填報名表")
        button = [
            {
                "type":"postback",
                "title":"下一步：匯款",
                "payload":"money"
            },
            {
                "type":"postback",
                "title":"返回主目錄",
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_button_message(sender_id, "***報名步驟***\n報名日期：\n4/1~4/24\t\t第一階段報名\n4/24~5/14\t第二階段報名\n1. 請至以下網址填寫報名表單：\nhttps://www.surveycake.com/s/24nrA \n報名完成後，請靜待我們公佈錄取名單。\n若確定您錄取了，請在期限內進行匯款。", button)

    def on_enter_money(self, event):
        print("I'm entering 匯款")
        button = [
            {
                "type":"postback",
                "title":"最後一步：寄信",
                "payload":"email"
            },
            {
                "type":"postback",
                "title":"返回主目錄",
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_button_message(sender_id, "2. 匯款：\n匯款期限：\n5/8\t第一階段匯款截止\n5/30\t第二階段匯款截止\n郵局代號：700\n存簿帳號：0123456789123\n戶名：國立成功大學資訊營歐子毓\n郵局：台南成功大學郵局\n金額：個人報名5300\n兩人團報5100/人\n三人團報5000/人\n*轉帳完請務必妥善留存轉帳明細\n*請務必確認轉帳帳號與金額，若因個人疏失造成匯款失敗，本營隊概不負責，敬請見諒", button)
    
    def on_enter_email(self, event):
        print("I'm entering 寄信")
        button = [
            {
                "type":"postback",
                "title":"返回主目錄",
                "payload":"sreturn"
            }
        ]
        sender_id = event['sender']['id']
        send_button_message(sender_id, "3. 寄信\n請完成匯款的同學務必要依照下列格式寄信到我們的信箱，以便核對資料。\n***如果沒有寄信造成我們無法核對資料，也視同放棄錄取***\n收件人：2018nckucsiecamp@gmail.com\n主旨：小隊員姓名-就讀學校-聯絡電話\n(e.g 金城武-建國中學-0900123456)\n信件內容：\n*匯款人姓名\n*繳費日期\n*帳戶銀行/郵局代碼\n*帳號末五碼\n當我們確認繳費資料無誤之後會回信通知，敬請留意自己的信箱\n另外如果完成繳費之後因個人因素無法參加營隊，我們會在Email裡面釋出相關規定，再請需要退費者留意自己報名時填的信箱", button)

################# on exit #################
    def on_exit_signup_info(self, event):
        print('Leaving 報名資訊')

    def on_exit_introduction(self, event):
        print('Leaving 營隊介紹')

    def on_exit_calendar(self, event):
        print('Leaving 行事曆')

    def on_exit_download(self, event):
        print('Leaving 附件下載')

    def on_exit_contact(self, event):
        print('Leaving 聯絡方式')
    
    def on_exit_inform(self, event):
        print('Leaving 通知書')

    def on_exit_leave(self, event):
        print('Leaving 離營')

    def on_exit_money(self, event):
        print('Leaving 填報名表')

    def on_exit_money(self, event):
        print('Leaving 匯款')

    def on_exit_money(self, event):
        print('Leaving 寄信')

