import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Token from @BotFather
TOKEN = "8123157608:AAFzVZcA6BFvW8kN7xGoh-9SMwJtKOHrRHc"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я чат бот канала TourNew. Я могу ответить на ваши вопросы")

@dp.message()
async def scripted_response(message: types.Message):
    text = message.text.lower()  # Convert text to lowercase for convenience

    if text == "привет":
        await message.reply("Привет! Как я могу вам помочь?")
    elif text == "как дела?":
        await message.reply("Отлично! Спасибо, что спросил \U0001F60A")
    elif text == "что ты умеешь?":
        await message.reply("Я могу отвечать на вопросы по по теме канала!")
    else:
        await message.reply("Я не знаю, что ответить... Попробуй спросить что-то другое.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
