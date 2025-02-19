import telegram
from gemini import Gemini

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего Telegram бота
bot_token = '7216405294:AAG1i86SbGAvtFvr-PJvnxjxsjalUpWd6EI'

# Замените 'YOUR_GEMINI_API_KEY' на ваш API ключ Gemini
gemini_api_key = 'AIzaSyCwDMWH-Hhp5DsK2Mcan4rsgWtOJ_3_5LU'

# Создаем экземпляры бота Telegram и Gemini
bot = telegram.Bot(token=bot_token)
gemini = Gemini(api_key=gemini_api_key)

# Обработчик сообщений
def handle_message(update, context):
    message = update.message.text
    response = gemini.generate_text(message)
    bot.send_message(chat_id=update.effective_chat.id, text=response)

# Запускаем обработчик сообщений
updater = telegram.ext.Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text & (~telegram.ext.Filters.command), handle_message))

# Запускаем бота
updater.start_polling()
updater.idle()
