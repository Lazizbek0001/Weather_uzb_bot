import logging
from aiogram import Bot, Dispatcher, executor, types
from config import *
from api import *
from buttons import *


bot =Bot(token=API_TOKEN)
dp=Dispatcher(bot)



logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Welcome choose your region of Uzbekistan", reply_markup = await gen_start())


@dp.message_handler(text = start)
async def send(message: types.Message):
    data = place(message.text)
    await message.answer(data)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)