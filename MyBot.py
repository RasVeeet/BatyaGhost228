import random

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = '6231595283:AAFg23Zeg8gHZbRRjNt1zgmJBI7RLZDXs0U'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

button_1: KeyboardButton = KeyboardButton(text='Анекдот')
button_2: KeyboardButton = KeyboardButton(text='Интересный факт')
button_3: KeyboardButton = KeyboardButton(text='Помощь')


# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2, button_3,]],
                                    resize_keyboard=True)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['Сыграем?']))
async def process_start_command(message: Message):
    await message.answer(text='Привет!\nХочешь расскажу смешной анекдот или интересный факт "?\n\n'
                         'Чтобы получить список доступных '
                         'команд - отправьте команду Помощь',reply_markup=keyboard)

    @dp.message(Command(commands=['Помощь']))
    async def process_help_command(message: Message):
        await message.answer(f'Анекдот-рассказывает анекдот'
                             f'Факт-рассказывает интересный факт.\n')



