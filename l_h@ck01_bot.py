import os 
import telebot


API_KEY = ----------------------bot-api-key-----------------------------
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['yo'])
def yo(	message):
	bot.reply_to(message,'super_yo')

@bot.message_handler(commands=['hello'])
def yo(	message):
	bot.send_message(message.chat.id,'hie')

bot.polling() 
