from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import CATEGORIES






def send_phone_button():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='Отправить свой контакт', request_contact=True)]
    ], resize_keyboard=True)


def generate_main_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='✔ Каталог')],
        [KeyboardButton(text='📙 История'), KeyboardButton(text='Корзина'), KeyboardButton(text='⚙ Настройки')]
    ], resize_keyboard=True)




def generate_category_shop():
    murkup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = []
    for category in CATEGORIES.keys():
        btn = KeyboardButton(text=category)
        buttons.append(btn)
    murkup.add(*buttons)
    return murkup


def button_link(link):
    murkup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Ссылка', url=link)
    murkup.add(btn)
    return murkup