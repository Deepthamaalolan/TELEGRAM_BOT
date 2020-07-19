import urllib

import telebot
import telegram
import requests
import json
import datetime


Token='1026085102:AAHKemyVdc-LxWLsw7eniMEaXobIVlxTt6k'
bot = telebot.TeleBot(Token)
URL = "https://api.telegram.org/bot{}/"
def get_json_from_url(url):
    #content = get_telegram_url(url)
    response = requests.get(url)
    content = response.content.decode("utf8")
    js = json.loads(content)
    return js
def get_telegram_update(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js
def get_json_from_url(url):
    #content = get_telegram_url(url)
    response = requests.get(url)
    content = response.content.decode("utf8")
    js = json.loads(content)
    return js


def get_telegram_update(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)
def echo_all(updates):
    for update in updates["result"]:

        last_chat_text = (update["message"]["text"])
        last_chat_name = update['message']['chat']['first_name']
        last_chat_id = update["message"]["chat"]["id"]
        greetings = ('hello', 'hi', 'greetings', 'sup')
        now = datetime.datetime.now()
        new_offset = None
        today = now.day
        hour = now.hour
        print(last_chat_text)
        print(last_chat_name)
    if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
        text = 'I am deepbot !! Good Morning  {}'.format(last_chat_name)
        send_telegram_message(text, last_chat_id)
        today += 1
    elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
        text = 'Good Afternoon {}'.format(last_chat_name)
        send_telegram_message(text, last_chat_id)
        today += 1

    elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
        text = 'Good Evening  {}'.format(last_chat_name)
        send_telegram_message(text, last_chat_id)
        today += 1


    if bot.get_last_updates():
        chat_id = bot.get_updates()[-1].last_chat_id

    # send chat action typing
        bot.send_chat_action(chat_id=chat_id, action=telegram.chataction.ChatAction.TYPING)

    else:
        print("Empty list. Please, chat with the bot")

    if bot.get_last_updates():
        chat_id = bot.get_updates()[-1].last_chat_id

        location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
        contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
        custom_keyboard = [[location_keyboard, contact_keyboard]]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

        bot.send_message(chat_id=chat_id, text="Would you mind sharing your contact and location with me?",
                     reply_markup=reply_markup)

    else:
        print("Empty list. Please, chat with the bot")

    text = "this is a telegram bot - replying back to your message: " + update["message"]["text"]
    print(text)
    chat = update["message"]["chat"]["id"]
    print(chat)
    send_telegram_message(text, chat)
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_telegram_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    #get_telegram_url(url)
    response = requests.get(url)
    content = response.content.decode("utf8")
def main():
    last_update_id = None
    print(URL)

    while True:
        updates = get_telegram_update(last_update_id)
        if len(updates['result']) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
    time.sleep(0.5)

greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()
if __name__ == '__main__':
    main()
