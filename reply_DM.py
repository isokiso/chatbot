# -*- coding:utf-8 -*-
import json
import config
from requests_oauthlib import OAuth1Session
import reply_message as rp
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #Twitter認証

url_get = "https://api.twitter.com/1.1/direct_messages.json" #DM取得エンドポイント
#url_post = "https://api.twitter.com/1.1/direct_messages/new.json" #DM送信エンドポイント

params ={'count' : 3} #DM取得数 //最新のだけ取得できるようにする
res = twitter.get(url_get, params = params)

if res.status_code == 200: #OKの場合
    messages = json.loads(res.text) #メッセージリスト取得
    for message in messages: #メッセージリストをループ処理
        rp.reply(twitter, message)#特定のワードに対して返信

else: #NGの場合
    print("Failed: %d" % res.status_code)
