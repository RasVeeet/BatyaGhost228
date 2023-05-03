from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = '6231595283:AAFg23Zeg8gHZbRRjNt1zgmJBI7RLZDXs0U'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')



@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Хочу кушать')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

@dp.message()

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"

@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)