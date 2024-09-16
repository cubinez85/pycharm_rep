# Подключаем библиотеку
import telebot

import urllib
# url = "https://drive.google.com/uc?export=view&id=1aBZnHgsjg7XIVlvpYasOOJ8hurp7V6Ww"
url = "https://drive.google.com/uc?export=view&id=1WDN5RXcYQHiUT4JVujQ2VSwr7pOXLlYX"
# filename = "skillbox_voice_sample.oga"
filename = "skillbox_sticker.webp"
urllib.request.urlretrieve(url, filename)

# Здесь нужно вставить токен, который дал BotFather при регистрации
# Пример: token = '2007628239:AAEF4ZVqLiRKG7j49EC4vaRwXjJ6DN6xng8'
token = '6317382509:AAGtGah2YXXoI-6f-KazHxUKWijDXsMUVJE'  # <<< Ваш токен

# В этой строчке мы заводим бота и даем ему запомнить токен
bot = telebot.TeleBot(token)

# Пишем первую функцию, которая отвечает "Привет" на команду /start
# Все функции общения приложения с ТГ спрятаны в функции под @
@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name)
    sticker = open('skillbox_sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    sticker.close()

# Запускаем бота. Он будет работать до тех пор, пока работает ячейка
# (крутится значок слева).
# Остановим ячейку - остановится бот
bot.polling()

