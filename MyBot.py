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
         ' а если что-то сверху – то дама с косой.',
           '"Задумался" - это не когда яйцо переварил или остановку проехал.\n'
         'Это  когда в 9 вечера пришёл на работу с пакетом мусора',
         'Настоящие мужики-самцы, даже когда выносят мусор,\n' 
         'берут с собой презервативы…',
         'И тринадцать моё любимое число и чёрные кошки мне нравятся,'
         ' когда дорогу переходят… \n'
         'Но не везёт также как и всем – не больше и не меньше',
         'У Алексея на днях родилась тройня\n'
         'Все мамы чувствуют себя хорошо!',
         'На уроке физкультуры: - Вовочка, за сколько ты пробежишь 300 метров?\n'
         'Ну, рублей за 300 пробегу.',
         'Сегодня мы нашли группу русских туристов пропавших в джунглях Таити, все живы и здоровы!\n'
         '- Как вам это удалось, ведь их искали больше года? - Мы нашли их по матерящимся попугаям!',
         'Бабушка, а ты пришла сама? - Сама внученька, сама!\n'
         'А папа сказал, что тебя черти принесли! ',
         'Я согрешил батюшка! - И в чем же ты грешен?\n'
         'Я обманул еврея! - Успокойся, это не грех, а чудо!']

fact1 = ['Двое из пяти человек женятся на своей первой любви.',
         'В среднем дети смеются около 400 раз в день, взрослые смеются около 15 раз в день.',
         ' В среднем самые высокие люди – голландцы.',
         '47% людей видят кошмарные сны не реже раза в месяц.',
         'В течение жизни человек проходит расстояние, равное 5 экваторам Земли.',
         ' В среднем человек засыпает в течение 7 минут.',
          'Дети в возрасте от 1 до 3 месяцев плачут без слёз.',
         'У женщин в среднем IQ выше, чем у мужчин.',
         ' Домохозяйка в среднем проходит 11 километров в день, занимаясь домашними делами.',
         ' Россия является единственной в мире страной, которая омывается 12 морями.',]

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
button_1: KeyboardButton = KeyboardButton(text='Интересный факт')
button_2: KeyboardButton = KeyboardButton(text='Анекдот')
button_3: KeyboardButton = KeyboardButton(text='Помощь')



# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2, button_3]],
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
                             f'Интересный факт-рассказывает интересный факт.\n')

@dp.message(or_f(Command(commands=['jack']),Text(text='Анекдот')))
async def process_help_command(message: Message):
    await message.answer(anek1[random.randint(0,9)], reply_markup=keyboard)

@dp.message(or_f(Command(commands=['fact']),Text(text='Интересный факт')))
async def process_help_command(message: Message):
    await message.answer(fact1[random.randint(0, 10)], reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)