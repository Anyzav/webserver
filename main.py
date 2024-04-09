import telebot
from telebot import types

bot = telebot.TeleBot('7032417900:AAFnXx--IFE8Nb71hiefFj4HCimo5QwuSVo')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = (types.KeyboardButton('/start'))
    btn2 = (types.KeyboardButton('/help'))
    btn3 = (types.KeyboardButton('привет'))
    btn4 = (types.KeyboardButton('id'))
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Рады тебя тут видеть. Чат-бот будет предоставлять'
                                      f' пользователям возможность создавать планы на день, устанавливать'
                                      f' напоминания. Надеемся тебе понравиться наш сервис! Чтобы продолжть работу'
                                      f' выберите один из предложенных вариантов команд в нижней панели', reply_markup=markup)

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


bot.polling(none_stop=True)