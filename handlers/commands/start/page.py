from aiogram import types, executor
from data.data import dp
from aiogram.types.web_app_info import WebAppInfo
@dp.message_handler(commands="start")
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(types.InlineKeyboardButton("open web venv", web_app=WebAppInfo(url="https://slidesigma.com/themes/html/floristica/")))
    await message.answer("hello gay", reply_markup=markup)

    # await message.answer(text="Hello World Start")