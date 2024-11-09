from data import bot
from data.loader import translator
from keyboards.reply import lang_kb
from telebot.types import ReplyKeyboardRemove
from handlers.commands import start

@bot.message_handler(func=lambda msg: msg.text == 'Перевод')
def start_translation(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Выберите язык, с которого хотите сделать перевод',
                     reply_markup=lang_kb())
    bot.register_next_step_handler(message, get_lang_from)


def get_lang_from(message):
    print(message.text)
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Выберите язык, на который хотите сделать перевод',
                     reply_markup=lang_kb())
    bot.register_next_step_handler(message, get_lang_to, message.text)

def get_lang_to(message, lang_from):
    print('lang_from', lang_from)
    print('lang_to', message.text)
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Напишите слово или текст для перевода',
                     reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, translate, lang_from, message.text)


def translate(message, lang_from, lang_to):
    from googletrans import LANGCODES

    chat_id = message.chat.id

    code_from = LANGCODES.get(lang_from) # код языка en, ru, uz ...
    code_to = LANGCODES.get(lang_to)

    translated_text = translator.translate(message.text, dest=code_to, src=code_from).text

    bot.send_message(chat_id, f"""
Оригинал: <b>{message.text}</b>
Перевод: <b>{translated_text}</b>
""")
    bot.send_message(chat_id, f'Перевод успешно выполнен')
    start(message)
