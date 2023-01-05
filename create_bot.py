from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv, find_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv(find_dotenv())

storage = MemoryStorage()
bot = Bot(os.getenv('TOKEN_API'))
dp = Dispatcher(bot, storage=storage)


support_ids = [
    1064938479
]