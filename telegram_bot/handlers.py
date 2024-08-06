from telebot import types
from utils import get_catalog, create_order


def setup_handlers(bot):

    # Пример обработчика команд
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id,
                         "Добро пожаловать в бот цветочного магазина! Используйте меню ниже для навигации.",
                         reply_markup=create_menu())

    # Обработчик для выбора цветка из каталога
    @bot.message_handler(func=lambda message: message.text == "Заказать цветы")
    def order_flowers(message):
        items = get_catalog()
        markup = types.InlineKeyboardMarkup()
        for item in items:
            markup.add(types.InlineKeyboardButton(text=f"{item[1]}: {item[2]} руб.", callback_data=f"order_{item[0]}"))
        bot.send_message(message.chat.id, "Выберите цветок:", reply_markup=markup)

    # Обработчик для адреса доставки
    def handle_address(message, product_id):
        user_id = message.from_user.id
        address = message.text
        create_order(user_id, product_id, address)
        bot.send_message(message.chat.id, "Ваш заказ успешно оформлен!")

    # Обработчик для обработки нажатий на кнопки каталога
    @bot.callback_query_handler(func=lambda call: call.data.startswith("order_"))
    def callback_order(call):
        product_id = int(call.data.split("_")[1])
        bot.send_message(call.message.chat.id, "Пожалуйста, укажите адрес доставки в формате:\nАдрес доставки: [ваш адрес]")
        bot.register_next_step_handler(call.message, handle_address, product_id)

    # Создание клавиатуры
    def create_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Просмотр каталога")
        item2 = types.KeyboardButton("Заказать цветы")
        item3 = types.KeyboardButton("Отследить заказ")
        item4 = types.KeyboardButton("Мои заказы")
        markup.add(item1, item2, item3, item4)
        return markup
