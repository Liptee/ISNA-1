import telebot
import config
from get_post import getter

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lala(message):
    group_id = int(message.text)
    getter(group_id)

# bot.polling()
bot.polling(none_stop = True)