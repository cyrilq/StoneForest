import telebot
import config
from telebot import types
import time

API_TOKEN = config.API_KEY
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.chat.id,
                     'Приветствую тебя, путник!'
                     '')

@bot.message_handler(content_types=['text'])
def send_welcome_message(message):
    bot.send_message('Выбери место своего назначения в нижем меню, путник!')


# polling cycle
if __name__ == '__main__':
    while True:
        # noinspection PyBroadException
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)
