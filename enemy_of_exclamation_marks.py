import telebot as tb

bot = tb.TeleBot('5614927499:AAHPORVnMSJ9CISJ45soNvP-md2tqiHGB5E')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'I hate exclamation marks!')

@bot.message_handler(content_types=['text'])
def deleter(message):
    if message.text.startswith('!'):
        bot.delete_message(message.chat.id, message.id)

bot.polling(none_stop=True, interval = 0)