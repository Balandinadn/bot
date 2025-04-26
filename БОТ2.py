import telebot
from datetime import datetime
import random

BOT_TOKEN = "7228133589:AAFET8AkD_TMdStA0D4xeZ0ltXGZbXMH3mw"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    time_button = types.KeyboardButton("Будь добр, сказать time")
    number_button = types.KeyboardButton("Рандомыш")
    id_button = types.KeyboardButton("IDшчка")
    markup.add(time_button,number_button, id_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы узнать время, число от 1 до 100 или получить ид.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == 'Будь добр, сказать time':
        current_time = datetime.now().strftime('%H:%M:%S')
        bot.send_message(message.chat.id, f"Текущее время: {current_time}")
    elif message.text == 'Рандомыш':
        rand_num = random.randint(1, 100)
        bot.send_message(message.chat.id, f"Случайное число: {rand_num}")
    elif message.text == 'IDшчка':
        bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}")
    else:
        bot.send_message(message.chat.id, "Команда не распознана.")
        
print("Всё готово!")
bot.polling()
