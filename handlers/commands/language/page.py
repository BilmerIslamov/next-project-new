from aiogram import types, executor
from data.data import dp

@dp.message_handler(commands="language")
async def start(message: types.Message):
    await message.answer(text="Hello World Language")