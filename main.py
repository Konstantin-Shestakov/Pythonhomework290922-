# Напишите бота, удаляющего из текста все слова, содержащие "абв". 
# (текст вводит пользователь)

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5720713668:AAGht_IV-3-jTBNWrdhywBj3PbfkQJJQY1E')
updater = Updater(token='5720713668:AAGht_IV-3-jTBNWrdhywBj3PbfkQJJQY1E')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет!\nЯ удаляю слова из сообщения с сочетанием "абв".')

def find_abv(update, context):
    text = update.message.text
    try:
        find_txt = "абв"
        lst = [i for i in text.split() if find_txt not in i]
        result = " ".join(lst)
        context.bot.send_message(update.effective_chat.id, f'Твое сообщение: {result}')
    except:
        context.bot.send_message(update.effective_chat.id, '')



start_handler = CommandHandler('start', start)
find_abv_handler = MessageHandler(Filters.text, find_abv )


dispatcher.add_handler(start_handler)
dispatcher.add_handler(find_abv_handler)

updater.start_polling()
updater.idle()