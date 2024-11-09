from data import bot
from keyboards.reply import start_kb


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Добро пожаловать в бот переводчик. Выберите дейтсвие ниже',
                     reply_markup=start_kb())