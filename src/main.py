import asyncio
from handlers.handlers import dp
from settings.bot_init import bot




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())