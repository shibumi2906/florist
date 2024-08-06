import sqlite3

# Функция для получения каталога из базы данных
def get_catalog():
    conn = sqlite3.connect('C:/Users/IMOE001/Documents/GitHub/florist/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM catalog_item")
    items = cursor.fetchall()
    conn.close()
    return items

# Функция для создания заказа
def create_order(user_id, product_id, address):
    conn = sqlite3.connect('C:/Users/IMOE001/Documents/GitHub/florist/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders_order (user_id, product_id, quantity, status, address) VALUES (?, ?, ?, ?, ?)",
                   (user_id, product_id, 1, 'В обработке', address))
    conn.commit()
    conn.close()
