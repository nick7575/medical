

# Grain_Merchant.py
import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

# address_to_coordinate.py
import requests
import urllib.parse
import json
import time

from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from addresstoGeocodev2 import *
from linebot.models import *

# line_bot_api = LineBotApi('你的 CHANNEL_ACCESS_TOKEN')
# handler = WebhookHandler('你的 CHANNEL_SECRET')

line_bot_api = LineBotApi('d+QKBbeW72agoZL35FpXUAftsdaaiv4XIBuYT8qoBpj5/HR2WLd/GipDYgwx/JbJbzHEGbTaMHZHZ1nPtefUOZPOUDMKdFh2lhKFAfOUowX1rXe1oxM1JxJ2KB2g2QM7kO97A4YZnqe22Mm+tEjBQgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('41bf2bb242c4b64e443c83f6ab5ad342')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=(TextMessage, LocationMessage))
def handle_message(event):
    # if event.message.text == "2":
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到您上傳的照片囉!\n將為您進行分析'))
    # elif event.message.text == "3":
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
    # elif event.message.text == "查附近醫院":
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入您的所在區域'))
    # elif event.message.text == "文山區":
    #     pass
    if event.message.type == 'location':
        #  {
        #     "events": [
        #         {
        #             "type": "message",
        #             "replyToken": "1904e4f5f7ce455da107bafae7b7fc73",
        #             "source": {
        #                 "userId": "Ub4adef4cf175e81f72f2f9ba65ea245d",
        #                 "type": "user"
        #             },
        #             "timestamp": 1602346694743,
        #             "mode": "active",
        #             "message": {
        #                 "type": "location",
        #                 "id": "12830230301657",
        #                 "title": "臺北車站",
        #                 "address": "台灣台北市中正區北平西路3號100臺灣",
        #                 "latitude": 25.047702,
        #                 "longitude": 121.517373
        #             }
        #         }

        a = get_latitude_longtitude(event.message.latitude, event.message.longitude)
        # print(a)
        # line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入您的所在區域'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text='您收到相關推薦', contents=a))
    return ("ok")

        # GOOGLE_API_KEY = "AIzaSyBC9OXMvpGIVJ5FVakJ00oQXEPq9j5E804"
        # '放入自己的google api key'
        # line_bot_api.reply_message(event.reply_token, message)



if __name__ == '__main__':
    app.run()



