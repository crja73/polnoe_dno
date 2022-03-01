import os
import aiogram

from aiogram import types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup

# Объект бота
bot = Bot(token="5210840543:AAGB3p2gHpYnOQiSvmlGsTECcPcK08uT47w")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения



@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    os.remove("/home/pi/Desktop/out.avi")
    os.system('ffmpeg -f alsa -f video4linux2 -s 1024x600 -i /dev/video0 -t 15 -b:v 500000 out.avi')

        


if __name__ == "__main__":
    
    executor.start_polling(dp, skip_updates=True)


os.remove("/home/pi/Desktop/out.avi")
os.system('ffmpeg -f alsa -f video4linux2 -s 1024x600 -i /dev/video0 -t 15 -b:v 500000 out.avi')
