from data import bot

def main():
    from handlers import commands, texts

    print("Bot starting")
    bot.infinity_polling()


main()