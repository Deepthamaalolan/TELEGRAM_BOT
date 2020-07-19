import os

import  telebot
from flask import Flask, request
token='1026085102:AAHKemyVdc-LxWLsw7eniMEaXobIVlxTt6k'
secret='abcdefgh'
bot=telebot.TeleBot(token,threaded=False)
app=Flask(__name__)
@app. route('/'+secret,methods=['Post'])
def getmessage():
    bot.process_new_updates(telebot.types.update.de_json[request.stream.read().decode('utf-8')]
    return 'ok',200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url+token)
    return 'ok',200

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,'hello welcome to our bot')
@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id,'how can i help you')
@bot.message_handler(content_types=['text'])
def echo(m):
    bot.send_message(m.chat.id,m.text)
@bot.message_handler(content_types=['photo'])
def photo(m):
    bot.send_message(m.chat.id,"COOL")


if __name__=="main":
    app.run(host="0.0.0.0",port=int(os.environ.get('PO
