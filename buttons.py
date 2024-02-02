from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




start = ['Tashkent', 'Andijan', 'Bukhara', 'Fergana', 'Jizzakh', 'Namangan', 'Navoiy', 'Qashqadaryo','Samarqand','Sirdaryo', 'Surxondaryo','Xorazm']

async def gen_start():
    btn = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    for key in start:
        btn.insert(KeyboardButton(text=key))
    return btn