import os
import telebot

hostname = "google.com"
channel = '@test'
token = '6317382509:AAGtGah2YXXoI-6f-KazHxUKWijDXsMUVJE'

response = os.system('ping ' + hostname)
bot = telebot.TeleBot(token)


if response == 0:
  print(hostname + ' is up!')
else:
  print(hostname + ' is down!')
  bot.send_message(channel, hostname + ' is down!')