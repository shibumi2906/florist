import sqlite3
from telebot import TeleBot, types
from config import API_TOKEN

bot = TeleBot(API_TOKEN)


# Функция для подключения к базе данных и получения данных из таблицы catalog_item
def get_catalog_data():
    conn = sqlite3.connect(r'C:\Users\IMOE001\Documents\GitHub\florist\db.sqlite3')
    cursor = conn.cursor()

    # Извлекаем данные из таблицы catalog_item
    cursor.execute("SELECT name, description, price FROM catalog_item")
    items = cursor.fetchall()

    conn.close()

    # Преобразуем список товаров в строку для отправки в сообщении
    catalog_list = "\n\n".join([f"{item[0]} - {item[1]}, Цена: {item[2]} руб." for item in items])
    return catalog_list


# Создание меню с одной кнопкой "Каталог"
def create_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Каталог")
    markup.add(item1)
    return markup


# Обработчик для команды /start, который отправляет меню
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в бот цветочного магазина!", reply_markup=create_menu())


# Обработчик для кнопки "Каталог"
@bot.message_handler(func=lambda message: message.text == "Каталог")
def show_catalog(message):
    catalog_data = get_catalog_data()
    bot.send_message(message.chat.id, f"Вот наш каталог:\n\n{catalog_data}")


# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)

