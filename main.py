import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from credits import bot_token, bot_token_omauga, hi_my_frend_token
from aiohttp import BasicAuth
from aiogram.client.session.aiohttp import AiohttpSession

PROXY_URL="http://proxy.server:3128"
logging.basicConfig(level=logging.INFO)
bot = Bot(token = hi_my_frend_token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Иди нахуй")

@dp.message(F.text)
async def answer(message: types.Message):
    if message.text == "САМ ИДИ НАХУЙ" or message.text == "сам иди нахуй" or  message.text == "САМ ИДИ" or message.text == "сам иди":
       await message.answer("Ладно, переубедил")
    else:
        await  message.answer("Ты блять с первого раза не понял?  ИДИ НАХУЙ")

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    #asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    #main()
    asyncio.run(main())