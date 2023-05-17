import random

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text, or_f
from aiogram.types import Message
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = '6231595283:AAFg23Zeg8gHZbRRjNt1zgmJBI7RLZDXs0U'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
button_1: KeyboardButton = KeyboardButton(text='Привет')
button_2: KeyboardButton = KeyboardButton(text='Интересный факт')
button_3: KeyboardButton = KeyboardButton(text='Анекдот')
button_4: KeyboardButton = KeyboardButton(text='Помощь')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2, button_3, button_4]],
                                    resize_keyboard=True)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(or_f(Command(commands=['start']),Text(text='Привет')))
async def process_start_command(message: Message):
    await message.answer('Привет!\nХочешь расскажу смешной анекдот и интересный факт ?\n\n'
                         'Чтобы получить список доступных '
                         'команд - отправьте команду Помощь',reply_markup=keyboard)

@dp.message(or_f(Command(commands=['help']),Text(text='Помощь')))
async def process_help_command(message: Message):
    await message.answer(f'Анекдот-рассказывает анекдот\n'
                             f'Факт-рассказывает интересный факт.\n')

    @dp.message(Command(commands=['Анекдот']))
    async def process_help_command(message: Message):
        await message.answer(f'Алло, полиция?'
                            'Да, что у вас случилось?\n'
                            'Из—за меня дерутся две девушки.\n'
                            'И в чем, собственно проблема?\n'
                            'Страшненькая побеждает!')

if __name__ == '__main__':
    dp.run_polling(bot)