import telebot
import config
from telebot import types
import time

API_TOKEN = config.API_KEY
bot = telebot.TeleBot(API_TOKEN)

main_menu_keyboard = types.ReplyKeyboardMarkup(row_width=3).row(
    types.KeyboardButton('🔦 Подземелье'),
    types.KeyboardButton('🌲 Лес')
).row(
    types.KeyboardButton('🤑 Казино'),
    types.KeyboardButton('🌇 Город')
).row(
    types.KeyboardButton('📋 Статус'),
    types.KeyboardButton('⚔️ РЕЙД')
)

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.chat.id,
                     'Приветствую тебя, путник!'
                     '')

@bot.message_handler(content_types=['text'])
def send_welcome_message(message):
    bot.send_message(chat_id=message.chat.id,
                     text='Выбери место своего назначения в нижем меню, путник!',
                     reply_markup=main_menu_keyboard
                     )


# polling cycle
if __name__ == '__main__':
    while True:
        # noinspection PyBroadException
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)
