import telebot
from telebot import types

bot = telebot.TeleBot('7032417900:AAFnXx--IFE8Nb71hiefFj4HCimo5QwuSVo')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = (types.KeyboardButton('Добавить задачу'))
    btn2 = (types.KeyboardButton('Удалить задачу'))
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.', reply_markup=markup)

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Чат-бот будет предоставлять пользователям возможность создавать планы на день,'
                                      'устанавливать напоминания')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

# @bot.callback_query_handlers(func=lambda callback: True)
# def callback_message(callback):
    # if callback.data == 'add':


bot.polling(none_stop=True)