from flask import Flask,request, abort, render_template
app = Flask(__name__)
from linebot.models import *
import re
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from urllib.parse import parse_qsl
from urllib.parse import parse_qsl
import string
import model
from textpredict import *
test = input()
predicttext(test)

line_bot_api = LineBotApi('RpNrYYhbu9UtDP5vpYs6wJceOs14I0Sunos1gSe9p7Q/6+cbtf3bb38M58+zWFXyo1DU0Zu4W+Ekfdw5+AaH2dpyTv71RWZPg5ay6WVsagFjRvn2DTeJdNTfEZSmtixuaCbzZoFUCaUCWfAfitcrPwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('81ee9a47b1eab6c88040d2541d1fe94e')
liffid = '1656669589-VqABoK4G'
liffida = '1656669589-APB3GvLz'

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


def manageForm(event, mtext):
    try:
        flist = mtext[3:].split('/')
        text1 = '姓名：' + flist[0] + '\n'
        text1 += '身分證：' + flist[1] + '\n'
        text1 += '日期：' + flist[2] + '\n'
        text1 += '地址：' + flist[3]
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    return


def manageHealth(event, mtext):
    try:
        flist = mtext[3:].split('/')
        text1 = '身高：' + flist[0] + '\n'
        text1 += '體重：' + flist[1] + '\n'
        text1 += '血壓：' + flist[2] + '\n'
        text1 += '血糖：' + flist[3]
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    return


#LIFF靜態頁面pip install --upgrade pip
@app.route('/page')
def page():
	return render_template('index.html', liffid = liffid)


#LIFF靜態頁面pip install --upgrade pip
@app.route('/physical')
def physical():
	return render_template('health.html', liffid = liffida)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # print('in')
    mtext = event.message.text
    if mtext[:3] == '###' and len(mtext) > 3:
         manageForm(event, mtext) & manageHealth(event, mtext)
    return



@handler.add(MessageEvent, message=ImageMessage) # 處理照片
def handle_pic(event):
    if event.message.type=='image':
        image_name = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(4))
        image_content = line_bot_api.get_message_content(event.message.id)
        image_name = image_name.upper()+'.jpg'
        path='./static/'+image_name
        with open(path, 'wb') as fd:
            for chunk in image_content.iter_content():
                fd.write(chunk)


# @app.route('/after')
# def hello():
#     return render_template('after.html')
#
#
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#         # 處理訊息
#         if event.message.type == 'text':
#
#             if event.message.text == '同意':
#                 line_bot_api.reply_message(event.reply_token, TextSendMessage(
#                     text='請輸入基本資料\n●身分證 ●生日\n\n格式要求如下:\n關鍵字 您的輸入值\n●身分證(空一格)A123456789\n●生日(空一格)0871231'))
#
#
#
#             elif event.message.text == "開始使用本服務":
#                 Confirm_template = TemplateSendMessage(
#                     alt_text='目錄 template',
#                     template=ConfirmTemplate(
#                         title='這是ConfirmTemplate',
#                         text='本AI 醫療服務由醫療助理團隊提供，在我開始查詢之前，需要請你先詳細閱讀並同意服務條款。',
#                         actions=[
#                             URITemplateAction(  #開啟網頁
#                                 label='同意',
#                                 uri='https://liff.line.me/1656669589-VqABoK4G'
#                             ),
#                             MessageTemplateAction(
#                                 label='不同意',
#                                 text='很抱歉，無法提供後續服務'
#                             )
#                         ]
#                     )
#                 )
#                 line_bot_api.reply_message(event.reply_token, Confirm_template)
#
#
#
#
#
#
#             # elif event.message.text == "8":
#             #     message = TextSendMessage(
#             #         text='請選擇最喜歡的程式語言',
#             #         quick_reply=QuickReply(
#             #             items=[
#             #                 QuickReplyButton(
#             #                     action=MessageAction(label="Python", text="Python")),
#             #                 QuickReplyButton(
#             #                     action=MessageAction(label="Java", text="Java")),
#             #                 QuickReplyButton(
#             #                     action=MessageAction(label="C#", text="C#")),
#             #                 QuickReplyButton(
#             #                     action=MessageAction(label="Basic", text="Basic"))]))
#             #     line_bot_api.reply_message(event.reply_token, message)
#
#
#             elif "身分證" in event.message.text:
#                 tmp = str(event.message.text).split(" ")[1]
#                 if re.fullmatch("^[a-zA-Z][12][0-9]{8}$", tmp):
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請輸入「出生日期」，民國年，範例：生日 0821115"))
#
#             elif "生日" in event.message.text:
#                 tmp = str(event.message.text).split(" ")[1]
#                 if re.fullmatch("[0-9]{7}", tmp):
#                     line_bot_api.reply_message(event.reply_token,
#                                                TextSendMessage(text="恭喜完成基本資料認證，請點選下方生理資訊按鈕以進行基本資料輸入"))
#
#             elif event.message.text == "生理資訊":
#                 line_bot_api.reply_message(event.reply_token, TextSendMessage(
#                     text="請輸入下列相關生理資訊數字，\n格式要求如下:\n\n#文字 數值 單位\n\n●身高 180 cm\n●體重 80 kg\n●血壓 120/85 mmHg\n●血氧 90 %"))
#             # \n其後記錄該項資訊\n●身高(cm)●體重(kg)●血壓(mmHg)●血氧( %)\n
#
#
#             # 身高
#             elif "身高" in event.message.text:
#                 tmp = str(event.message.text).split(" ")[1]
#                 if re.fullmatch("[1-2][0-9]{2}$", tmp):
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(
#                         text="您的輸入為身高:" + tmp + "cm" + "\n請輸入下列相關生理資訊數字，其後記錄該項資訊\n● 體重(kg)\n● 血壓(mmHg)\n● 血氧(%)"))
#                     LineID = event.source.user_id
#                     height = tmp
#                     healthRecord.put_item(Item={'id': LineID,
#                                                 'LineID': LineID,
#                                                 'height': height})
#                 else:
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請重新輸入"))
#
#
#             # 體重
#             elif "體重" in event.message.text:
#                 tmp = str(event.message.text).split(" ")[1]
#                 if re.fullmatch("[0-9]{2}$", tmp):
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(
#                         text="您的輸入為體重:" + tmp + "kg" + "\n請輸入下列相關生理資訊數字，其後記錄該項資訊\n● 血壓(mmHg)\n● 血氧(%)"))
#                     LineID = event.source.user_id
#                     weight = tmp
#                     healthRecord.put_item(Item={'id': LineID,
#                                                 'LineID': LineID,
#                                                 'weight': weight})
#                 else:
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請重新輸入"))
#
#
#             # 血壓
#             elif "血壓" in event.message.text:
#                 tmp = str(event.message.text).split(" ")[1]
#                 if re.fullmatch("[1-2][0-9]{2}/[0-9]{2}$", tmp):
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(
#                         text="您的輸入為血壓:" + tmp + "mmHg" + "\n請輸入下列相關生理資訊數字，其後記錄該項資訊\n● 血氧(%)"))
#                     LineID = event.source.user_id
#                     BP = tmp
#                     healthRecord.put_item(Item={'id': LineID,
#                                                 'LineID': LineID,
#                                                 'BP': BP})
#                 else:
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請重新輸入"))
#
#
#             # 血氧
#             elif "血氧" in event.message.text:
#                 tmp = str(event.message.text).split(" ")[1]
#                 if re.fullmatch("[1][0-9]{2}|[0-9]{2}$", tmp):
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(
#                         text="您的輸入為血氧:" + tmp + "%" + "完成基本資料輸入，可以開始使用本服務囉！\n●皮膚圖像查詢\n●文字症狀查詢\n\n請點選下方按鈕"))
#                     LineID = event.source.user_id
#                     BP = tmp
#                     healthRecord.put_item(Item={'id': LineID,
#                                                 'LineID': LineID,
#                                                 'BP': BP})
#                 else:
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請重新輸入"))
#
#
#
#
#             elif "我想進一步了解我的症狀" in event.message.text:
#                 # symptomtime=datetime.datetime.now()
#                 # if datetime.datetime.timestamp(symptomtime)-datetime.datetime.timestamp(entertime)>20:
#                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text="您好，請輸入病徵，解析後將為您提供相關訊息"))
#                 # elif datetime.datetime.timestamp(symptomtime)-datetime.datetime.timestamp(entertime)<20:
#                 # line_bot_api.reply_message(event.reply_token,TextSendMessage(text="請輸入完整資訊"))
#
#
#             elif "痛" in event.message.text and len(event.message.text) > 5:
#                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text="為您進行診斷"))
#
#             elif len(event.message.text) < 5:
#                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text="我不太明白您的意思，請重新敘述"))
#
#
#
#             elif "我想了解我的皮膚情形" in event.message.text:
#                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text="您好，請上傳圖片，解析後將為您提供相關訊息"))
#
#
#         # # 處理照片
#         # elif event.message.type == 'image':
#         #
#         #     message_content = line_bot_api.get_message_content(event.message.id)
#         #     # message_content=str(message_content)
#         #
#         #     # from smart_open import open
#         #
#         #     b = ""
#         #     for chunk in message_content.iter_content():
#         #         a = str(chunk)
#         #         b = b + a
#         #
#         #     s3 = boto3.resource('s3')
#         #     # object = s3.Object('healthreporterinputimage', '125.json')
#         #     idd = event.source.user_id
#         #     idd = str(idd) + '.jpg'
#         #
#         #     # idd=str(event.source.user_id)+'.json'
#         #
#         #     object = s3.Object('healthreporterinputimage', idd)
#         #     object.put(Body=b)
#         #
#         #     # line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message_content[:5]))
#         #     # with open('s3://healthreporterinputimage/'+ message.source.user_id+ '.json', 'wb') as fd:
#         #     # for chunk in message_content.iter_content():
#         #     #     fd.write(chunk)
#         #     # line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://res.cloudinary.com/jiablog/coffee.png',preview_image_url='https://res.cloudinary.com/jiablog/coffee.png'))
#         #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text='成功將圖片輸入資料庫!!\n將為您進行分析'))
#         #     # line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message_content[:5]))
#         #     import cv2
#         #     import numpy as np
#         #     import json
#         #
#         #     # 要讀取的JSON格式文件
#         #     JSON_NAME = 'https://healthreporterinputimage.s3.ap-northeast-1.amazonaws.com/' + idd
#         #     # 還原為圖片文件
#         #     IMAGE_NAME = 'restore.png'
#         #
#         #     # 讀取文件為字典
#         #     with open(JSON_NAME, "rb") as json_file:
#         #         img_dict = json.load(json_file)
#         #
#         #     # 獲取字典中內容，轉為list
#         #     img_list = img_dict['content']
#         #     # list轉numpy
#         #     img = np.asarray(img_list)
#         #     # 還原圖片
#         #     cv2.imwrite(IMAGE_NAME, img)
#
# @handler.add(PostbackEvent)
# def handle_postback(event):
#         backdata = dict(parse_qsl(event.postback.data))
#         if backdata.get('action') == 'buy':
#             message = TextSendMessage(text='請您上傳照片喔')
#             line_bot_api.reply_message(event.reply_token, message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)