from telebot import TeleBot
import settings
from googletrans import Translator

# html
# <b></b>
# <i></i>
bot = TeleBot(token=settings.BOT_TOKEN, parse_mode='HTML')
translator = Translator()
