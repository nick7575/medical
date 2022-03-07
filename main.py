from flask import Flask,request, abort, render_template
app = Flask(__name__)
from linebot.models import *
import re
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from urllib.parse import parse_qsl
import string
import model
import googlemaps
import os

from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv


line_bot_api = LineBotApi('RpNrYYhbu9UtDP5vpYs6wJceOs14I0Sunos1gSe9p7Q/6+cbtf3bb38M58+zWFXyo1DU0Zu4W+Ekfdw5+AaH2dpyTv71RWZPg5ay6WVsagFjRvn2DTeJdNTfEZSmtixuaCbzZoFUCaUCWfAfitcrPwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('81ee9a47b1eab6c88040d2541d1fe94e')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text[0:3] == "隨便吃":
       address = "AIzaSyCHu_G2prNmvGMxLy_VPJ8kwHm6g6FYHZA"
       if lineMes[4:-1] == "":
       address = "台北市內湖區舊宗路二段207號"
    else:
       address = lineMes[4:-1]

    addurl = 'https://maps.googleapis.com/maps/api/geocode/json?key'

if lineMessage[e:3] == "隨便吃":
    address = ""
    lineMes = lineMessage
    if lineMes[4: -1] == "":
        address = "台北市內湖區舊宗路二段207號"
    else:
        address = lineMes[4:-1]

    addurl = 'https://maps.googleapis.com/maps/api/geocode/json?key={}&address={}&sensor=false'.format(GOOGLE_API_KEY, address)

    addressReq = requests.get(addurl)
    addressDoc = addressReq.json()
    lat = addressDoc['results'][0]['geometry']['location']['lat']
    Ing = addressDoc['results'][0]['geometry']['location']['lng']


    foodStoreSearch = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}&location={},{}&rankby=distance&type=restaurant&language=zh-TW"
    .format(GOOGLE_API_KEY, lat, lng)

    foodReq = requests.get(foodStoreSearch)
    nearby_restaurants_dict = foodReq.json()
    top20_restaurants = nearby_restaurants_dict["results"]
    res_num = (len(top20_restaurants))
    #取得評分高於3.9的店家位置
    bravo = []
    for i in range(res_num):
        try:
            if top20_restaurants[i]['rating'] > 3.9:
                print('rate: ', top20_restaurants[i]['rating'])                                                                top20_restaurants[i]['rating'])
                bravo.append(i)
        except:
            KeyError
    if len(bravo) < 0:
        content = "沒東西可以吃"
        # restaurant = random.choice(top20_restaurants) 沒有的話隨便選一間
    #從高於3.9的店家隨便選一間
    restaurant = top20_restaurants[random.choice(bravo)]
    if restaurant.get("photos) is None:
        thumbnail_image_url = None
    else:
        photo_reference - restaurant["
    photos
    "][0["
    photo_reference
    "] photo_width restaurant ["
    photos
    "][0]["
    width
    "] thumbnail_image_url - "
    https: // maps.googleapis.com / maps / api / place / photo?key = {} & photoreference = {} & maxwidth = {}
    " .format (GOOGLE API_KEY, photo_reference, photo_width) rating - "" if restaurant.get("
    rating
    ") is None else restaurant["
    rating
    "] address = "
    iEHE
    " if restaurant.get("
    vicinity
    ") is None else restaurant["
    vicinity
    "] details = "
    Google
    Mapif: {}\nt: (
                      }".format(rating, address) * print(details) * Itz g Google map E map_url - "https: // www.google.com / maps / search / Papi=1 & query=(lat}, {long) & query_place
    id = (place Id)
    " .format (lat=restaurant["
    geometry
    "]["
    location
    "]["
    lat
    "], long-restaurant["
    geometry
    "I"
    location
    "]["
    lng
    "],place_iderestaurant ("
    place_id
    "])
