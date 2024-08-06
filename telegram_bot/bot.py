from telebot import TeleBot
from config import API_TOKEN
from handlers import setup_handlers

bot = TeleBot(API_TOKEN)
setup_handlers(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)
