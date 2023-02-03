import sqlite3



def create_users_table():
    database = sqlite3.connect('store_bot.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT
    );
    ''')
    database.commit()
    database.close()


def create_carts_table():
    database = sqlite3.connect('store_bot.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
        cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id),
        total_price DECIMAL(12, 2) DEFAULT 0,
        total_name INTEGER DEFAULT 0
    );
    ''')
    database.commit()
    database.close()


def create_cart_product_table():
    database = sqlite3.connect('store_bot.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart_product(
      cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
      cart_id INTEGER REFERENCES carts(cart_id),
      product_name VARCHAR(100) NOT NULL,
      final_price DECIMAL(12, 2) NOT NULL,
      UNIQUE(cart_id, product_name)
    );
    ''')
    database.commit()
    database.close()



#create_users_table()
#create_carts_table()
#create_cart_product_table()



# ____________________________________________________________



def create_categories_table():
    database = sqlite3.connect('store_bot.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name VARCHAR(60) NOT NULL UNIQUE
    );
    ''')
    database.commit()
    database.close()




#create_categories_table()



def first_select_user(chat_id):
    database = sqlite3.connect('store_bot.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE telegram_id = ?
    ''', (chat_id,))
    user = cursor.fetchone()
    database.close()
    return user


def first_register_user(chat_id, full_name):
    database = sqlite3.connect('store_bot.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO users(telegram_id, full_name) VALUES(?, ?)
    ''', (chat_id, full_name))
    database.commit()
    database.close()


def update_user_to_finish_register(chat_id, phone):
    database = sqlite3.connect('store_bot.db')
    cursor = database.cursor()
    cursor.execute('''
    UPDATE users
    SET phone = ? 
    WHERE telegram_id =?
    ''', (phone, chat_id))
    database.commit()
    database.close()



def insert_to_cart(chat_id):
    database = sqlite3.connect('store_bot.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO carts(user_id) VALUES
    (
        (SELECT user_id FROM users WHERE telegram_id = ?)
    )
    ''', (chat_id,))
    database.commit()
    database.close()