from aiogram import types, executor
from data.data import dp
from handlers.commands import start
from handlers.commands import help
from handlers.commands import main
from handlers.commands import language







if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



