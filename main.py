import telebot
bot = telebot.TeleBot('6984930983:AAHViXHEe1hdJ57CWj4pJTSj3Yw_8NFpDvc')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'hello')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'this \n[first help haha](https://ru.pinterest.com/pin/3166662230854339/) \n[second help hehe](https://ru.pinterest.com/pin/605382374931681145/)', parse_mode='Markdown')

@bot.message_handler(commands=['thanks'])
def main(message):
    bot.send_message(message.chat.id, '*you are welcome!;)*', parse_mode='Markdown')

bot.infinity_polling()



