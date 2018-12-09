# -*- coding:utf-8 -*-
import json
import config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #Twitter認証

url = "https://api.twitter.com/1.1/direct_messages.json" #エンドポイント

params ={'count' : 3} #DM取得数
res = twitter.get(url, params = params)

if res.status_code == 200: #OKの場合
    messages = json.loads(res.text) #タイムラインリスト取得
    for message in messages: #タイムラインリストをループ処理
        print('name      : ' + tweet['sender']['name'])
        print('text      : ' + tweet['text'])
        print('created_at: ' + tweet['created_at'])
        print('*******************************************')
else: #NGの場合
    print("Failed: %d" % res.status_code)
