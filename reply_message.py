# -*- coding:utf-8 -*-

def reply(twitter, message):
    url_post = "https://api.twitter.com/1.1/direct_messages/new.json" #DM送信エンドポイント

    print('name      : ' + message['sender']['name'])
    print('text      : ' + message['text'])
    print('created_at: ' + message['created_at'])

    if message['text'].find('DM') > 0:
        params = {'user_id' : message['sender']['id'],
                  'text' : 'thanks'}
        res = twitter.post(url_post, params = params)
        if res.status_code == 200:
            print('sent succesfully.')
        else:
            print("Failed: %d" % res.status_code)

    else:
        print('cannot find requested word')

    print('*******************************************')
