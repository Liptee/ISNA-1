import telebot
import config
from post import poster

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lele():
    poster(message.text)

bot.polling(none_stop = True)