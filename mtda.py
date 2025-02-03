from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7216405294:AAG1i86SbGAvtFvr-PJvnxjxsjalUpWd6EI')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types. Message) :
    markup = types. ReplyKeyboardMarkup ()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=https://google.com) )
    await massage.answer('Добро пожаловать на этот сайт!', reply_markup=marcup)


executor.start_polling(dp)
