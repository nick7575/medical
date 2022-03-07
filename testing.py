from flask import Flask,request, abort, render_template
app = Flask(__name__)
from linebot.models import *
import re
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from urllib.parse import parse_qsl
import string
import model


line_bot_api = LineBotApi('RpNrYYhbu9UtDP5vpYs6wJceOs14I0Sunos1gSe9p7Q/6+cbtf3bb38M58+zWFXyo1DU0Zu4W+Ekfdw5+AaH2dpyTv71RWZPg5ay6WVsagFjRvn2DTeJdNTfEZSmtixuaCbzZoFUCaUCWfAfitcrPwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('81ee9a47b1eab6c88040d2541d1fe94e')
liffid = '1656669589-VqABoK4G'
# liffid1 = ''

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=ImageMessage)
def handle_pic(event):
    # 處理照片
    # print("123")
    if event.message.type == 'image':
    # 設定圖片命名
        image_content = line_bot_api.get_message_content(event.message.id)
        image_name = event.message.id
        path = "./static/" + image_name + ".jpg"
        # 下載圖片檔
        with open(path, 'wb') as fd:
            for chunk in image_content.iter_content():
                fd.write(chunk)
                #linebot回傳圖片給user
        #指定圖片網址

        url = "http://10.2.14.62:5004/" + path[1::]
        # print(url)
        #呼叫方法
        result= model.predict(url)
        #輸出結果
        # print(result)
        # image_message = ImageSendMessage(
        #     original_content_url=path,  #### 靜態檔案的url
        #     preview_image_url=path
        # )
        # 使用replyAPI回傳
        # line_bot_api.reply_message(event.reply_token, image_message)0
        # line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=result))
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)