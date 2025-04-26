import telebot
import requests
import random
from telebot import types


BOT_TOKEN = "7564145261:AAFfCBws88DyiKM0OCdS9hNZZNflRyXicRc"
bot = telebot.TeleBot(BOT_TOKEN)

WEATHER_API_KEY = "bd6e0267940684a51406d6dfc5d46c1b"
CITY = "Москва"

sticker_ids = [
    "CAACAgQAAxkBAAEOSYhn-iLuHZiCEjcuRfm4NBtG7020NgACERYAArdEWVCc76Seal43mTYE",
    "CAACAgIAAxkBAAEOSXpn-iIaKR5y5OrsJZTod93INZESMQACQCIAAnq2YEur-eo2cza__jYE",
    "CAACAgIAAxkBAAEOSZBn-iMaqebw5sxdOinnGWpbzeXSgAACQQADPIpXGiCbHYE8KiBgNgQ",
    "CAACAgIAAxkBAAEOSZJn-iM36Yxxo0fxzW4riIRPa-emYQACrk8AAswiUEiExmpV7rw1rzYE",
    "CAACAgQAAxkBAAEOSZRn-iNrnquJVZoIdOb1d4WSVfS2AgAC-xAAAkygCFDk5D2wrBuTYjYE",
    "CAACAgQAAxkBAAEOSZZn-iN-T34Jz0EdG-myhNloKC1F9wACFhUAAm6nmVCiDpSHyOWEWTYE",
    "CAACAgQAAxkBAAEOSZhn-iOS_RblO9-ME3j7Us3Tg-K9XwAC1Q4AAnNUKFIJ7Z7kNVKseTYE",
    "CAACAgIAAxkBAAEOPoRn99sFr5XmBWypgRfendW3vxQU7gAC0BUAAsHN6Etz9xIa14yPYDYE",
    "CAACAgIAAxkBAAEOSaZn-iUO57gmVEtx9rySqBvAGwluOAACohUAAtur6EuM1lH9XVvkKjYE",
    "CAACAgIAAxkBAAEOSahn-iUjgPcY8Bp-9G04ezsHh5t8fQACFhoAAnYMEEuTnXNSuJzunzYE",
]

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return temperature, description
    except requests.exceptions.RequestException as e:
        return None, str(e)
    except (KeyError, TypeError):
        return None, "Ошибка получения данных о погоде"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weather_button = types.KeyboardButton("Текущая погода")
    sticker_button = types.KeyboardButton("Стикер")
    markup.add(weather_button, sticker_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы узнать погоду или получить стикер.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def hello(message):
    bot.reply_to(message, "Привет, человек!!!")

@bot.message_handler(func=lambda message: message.text == "Текущая погода")
def weather(message):
    temperature, description = get_weather(CITY)
    if temperature is not None:
        bot.send_message(message.chat.id, f"Погода в городе {CITY}: {temperature:.1f}°C, {description}")
    else:
        bot.send_message(message.chat.id, description)

@bot.message_handler(func=lambda message: message.text == "Стикер")
def sticker(message):
    random_sticker = random.choice(sticker_ids)
    bot.send_sticker(message.chat.id, random_sticker)

bot.infinity_polling()
