from aiogram import Bot
from aiogram import Dispatcher
from dotenv import load_dotenv

load_dotenv()
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()