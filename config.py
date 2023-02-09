CATEGORIES = {
    'Теливизори': 'https://www.mediapark.uz/products/category/8',
    'Ноутбуки': 'https://www.mediapark.uz/products/category/22',
    'Телефоны': 'https://www.mediapark.uz/products/category/17',
    'Планшеты': 'https://www.mediapark.uz/products/category/21'
}





def get_value(key):
    for k, v in CATEGORIES.items():
        if k == key:
            return v