from aiogram import types, executor
from data.data import dp

@dp.message_handler(commands="help")
async def start(message: types.Message):
    await message.answer(text="Hello World Help")