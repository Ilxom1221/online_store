from aiogram import executor, Bot, Dispatcher
from aiogram.types import Message
import os
from dotenv import load_dotenv
from keyboard import *
from database import *



load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message:Message):
    await message.answer(f'Здраствуйте {message.from_user.full_name}\n Добро пожаловать в наш магазин бот')
    await register_user(message)



async def register_user(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    user = first_select_user(chat_id)
    if user:
        await message.answer('Авторизация прошла успешно')
        await show_main_menu(message)
    else:
        first_register_user(chat_id, full_name)
        await message.answer('Для регистрации отправьте контакт', reply_markup=send_phone_button())


@dp.message_handler(content_types=['contact'])
async def finish_register(message:Message):
    chat_id = message.chat.id
    phone = message.contact.phone_number
    update_user_to_finish_register(chat_id, phone)
    await creat_cart_for_user(message)
    await message.answer('Регистратция прошло успешно')
    await show_main_menu(message)


async def creat_cart_for_user(message:Message):
    chat_id = message.chat.id
    try:
        insert_to_cart(chat_id)
    except:
        pass



async def show_main_menu(message:Message):
    await message.answer('Выберите ', reply_markup=generate_main_menu())


@dp.message_handler(lambda message: '✔ Каталог' in message.text)
async def make_order(message: Message):
    await message.answer('Выберите Католог', reply_markup=generate_category_menu())



executor.start_polling(dp)
