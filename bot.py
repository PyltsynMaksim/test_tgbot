import config

import telebot

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, """\
Hello there. I'm bot that can mirror your messages\
""")
    
@bot.message_handler(commands=['commands'])
def send_welcome(message):
    bot.reply_to(message, """\
My commands:
    /help
    /info
    /start\
""")
    
    
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

#message.photo[-1].file_id

bot.infinity_polling()

print(config.token)