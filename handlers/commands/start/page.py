from aiogram import types, executor
from data.data import dp

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(text="Hello World Start")