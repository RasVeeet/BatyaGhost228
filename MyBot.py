import random

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text, or_f
from aiogram.types import Message
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = '6231595283:AAFg23Zeg8gHZbRRjNt1zgmJBI7RLZDXs0U'
anek1 = [f'Алло, полиция?\n'
'Да, что у вас случилось?\n'
 'Из—за меня дерутся две девушки.\n'
 'И в чем, собственно проблема?\n'
  'Страшненькая побеждает!',
         'Если падает нож, то придёт мужик,\n'
         ' если вилка - то женщина,\n'
         ' а если что-то сверху – то дама с косой.',''
           '"Задумался" - это не когда яйцо переварил или остановку проехал.\n'
         'Это  когда в 9 вечера пришёл на работу с пакетом мусора',
         'Настоящие мужики-самцы, даже когда выносят мусор,\n' 
         'берут с собой презервативы…',
         'И тринадцать моё любимое число и чёрные кошки мне нравятся,'
         ' когда дорогу переходят… Но не везёт также как и всем – не больше и не меньше',
         'У Алексея на днях родилась тройня'
         'Все мамы чувствуют себя хорошо!',
         'В наше время, чтобы растёгивали приходится отстёгивать...']
# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
button_1: KeyboardButton = KeyboardButton(text='Интересный факт')
button_2: KeyboardButton = KeyboardButton(text='Анекдот')
button_3: KeyboardButton = KeyboardButton(text='Помощь')

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
button_4: KeyboardButton = KeyboardButton(text='Ещё')
button_5: KeyboardButton = KeyboardButton(text='Назад')

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
button_6: KeyboardButton = KeyboardButton(text='Ещё хочу')
button_7: KeyboardButton = KeyboardButton(text='Обратно')



# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2, button_3]],
                                    resize_keyboard=True)

keyboard2: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_4, button_5]],
                                    resize_keyboard=True)

keyboard3: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_6, button_7]],
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

@dp.message(or_f(Command(commands=['jack']),Text(text='Анекдот')))
async def process_help_command(message: Message):
    await message.answer(anek1[random.randint(0,7)], reply_markup=keyboard2)

    @dp.message(or_f(Command(commands=['back']), Text(text='Назад')))
    async def process_start_command(message: Message):
        await message.answer('Привет!\nХочешь расскажу смешной анекдот и интересный факт ?\n\n'
                             'Чтобы получить список доступных '
                             'команд - отправьте команду Помощь', reply_markup=keyboard)


@dp.message(or_f(Command(commands=['more']),Text(text='Ещё')))
async def process_positive_answer(message: Message):
        await message.answer(anek1[random.randint(0,7)],reply_markup=keyboard2)

@dp.message(or_f(Command(commands=['fact']),Text(text='Интересный факт')))
async def process_help_command(message: Message):
    await message.answer(f'У осьминога три сердца',reply_markup=keyboard3)

@dp.message(or_f(Command(commands=['more2']),Text(text='Ещё хочу')))
async def process_positive_answer(message: Message):
        await message.answer('Жаб использовали как тест на беременность',reply_markup=keyboard3)

@dp.message(or_f(Command(commands=['back2']),Text(text='Обратно')))
async def process_positive_answer(message: Message):
        await message.answer('Привет!\nХочешь расскажу смешной анекдот и интересный факт ?\n\n'
                             'Чтобы получить список доступных '
                             'команд - отправьте команду Помощь', reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)