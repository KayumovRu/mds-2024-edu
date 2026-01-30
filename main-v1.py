import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

bot = Bot(token="8286955245:AAF4-p57MkJjg1vDlCvCEh5CNBGmQnHq_f4")
dp = Dispatcher()

@dp.message(F.text == "hello")
async def hello_handler(message):
    await message.answer("HI!!!!!!!")

@dp.message()
async def echo_handler(message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())