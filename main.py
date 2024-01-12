import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
import asyncio

BOT_TOKEN = ''
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def answer_as_echo(msg:types.Message):
    await msg.answer(text=msg.text)


@dp.message()
async def reply_as_echo(msg:types.Message):
    await msg.reply(text=msg.text)



async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


# print(f"{__name__ = }")

if __name__ == "__main__":
    asyncio.run(main())