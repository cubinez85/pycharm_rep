import telebot
from telebot import types
token="7436641437:AAGh0BE9r3jjB4MsE4ySdZFTJbl8_aGvJ0g"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
@bot.message_handler(commands=['button'])
def button_message(message):
  markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1=types.KeyboardButton("Кнопка")
  markup.add(item1)
  bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
bot.infinity_polling()