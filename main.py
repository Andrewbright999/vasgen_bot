import asyncio, logging, sys
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from config import TG_TOKEN
from fasgen_parser import generate_image

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

@dp.message(Command("start")) 
async def cmd_start(message: Message):
    await message.answer("Привет, я Васген и быстро нарисую, все что ты захочешь🎨")
    

@dp.message(F.text)
async def message_with_text(message: Message):
    mess = await message.answer(f"Рисую...")
    try:
        path = generate_image(prompt=message.text)
        print(path)
        # if path:
            # Отправка изображения
        photo = FSInputFile(f"{path}", "rb")
        await message.answer_photo(photo=photo)
            # Удаляем изображение после отправки
        # else:
            # await message.answer('Ошибка при создании изображения.')
    except Exception as e:
        print(e)
        await message.answer(f'Произошла ошибка: {e}')
    await mess.delete()

        



async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# try:
#     session = AiohttpSession(proxy='http://proxy.server:3128')
#     bot = Bot(token=TG_TOKEN, session=session)
# except:
#     bot = Bot(token=TG_TOKEN)
