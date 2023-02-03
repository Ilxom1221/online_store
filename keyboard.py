from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import CATEGORIES




# def button_store():
#     murkup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     buttons = []
#     for category in CATEGORIES.keys():
#         btn = KeyboardButton(text=category)
#         buttons.append(btn)
#     murkup.add(*buttons)
#     return murkup


def send_phone_button():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='Отправить свой контакт', request_contact=True)]
    ], resize_keyboard=True)


def generate_main_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='✔ Каталог')],
        [KeyboardButton(text='📙 История'), KeyboardButton(text='Корзина'), KeyboardButton(text='⚙ Настройки')]
    ], resize_keyboard=True)




def generate_category_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(
        InlineKeyboardButton(text='Всё меню', url='')
    )