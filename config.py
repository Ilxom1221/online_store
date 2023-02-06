CATEGORIES = {
    'Теливизори': 'products/category/8',
    'Ноутбуки': 'products/category/22',
    'Телефоны': 'products/category/17',
    'Планшеты': 'products/category/21'
}





def get_value(key):
    for k, v in CATEGORIES.items():
        if k == key:
            return v