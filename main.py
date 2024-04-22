import telebot
import datetime
from telebot import types
from datetime import date

current_date = date.today()
current_date1 = str(current_date)
current_date3 = str(current_date + datetime.timedelta(days=2))
current_date2 = str(current_date + datetime.timedelta(days=1))


bot = telebot.TeleBot('7032417900:AAFnXx--IFE8Nb71hiefFj4HCimo5QwuSVo')


@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = (types.KeyboardButton('/start'))
    btn2 = (types.KeyboardButton('/help'))
    btn3 = (types.KeyboardButton('привет'))
    btn4 = (types.KeyboardButton('id'))
    btn5 = (types.KeyboardButton('Планы'))
    btn6 = (types.KeyboardButton('Написать цели'))
    btn7 = (types.KeyboardButton('Поставить напоминание'))
    btn8 = (types.KeyboardButton('Изменить цели'))
    markup.add(btn1, btn5)
    markup.add(btn6, btn7, btn8)
    markup.add(btn3, btn2, btn4)
    bot.send_message(m.chat.id, f'Привет, {m.from_user.first_name}. Рады тебя тут видеть. Чат-бот будет предоставлять'
                                      f' пользователям возможность создавать планы на день, устанавливать'
                                      f' напоминания. Надеемся тебе понравиться наш сервис! Чтобы продолжть работу'
                                      f' выберите один из предложенных вариантов команд в нижней панели', reply_markup=markup)

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Чат-бот будет предоставлять пользователям возможность создавать планы на день,'
                                      'устанавливать напоминания')

@bot.message_handler(content_types=['text'])
def info(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.')
    elif message.text == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text == 'Написать цели':
        keyboard = types.InlineKeyboardMarkup()
        key_year = types.InlineKeyboardButton(text='Год', callback_data='otvet')
        keyboard.add(key_year)
        key_sixmonths = types.InlineKeyboardButton(text='Полгода', callback_data='otvet')
        keyboard.add(key_sixmonths)
        key_month = types.InlineKeyboardButton(text='Месяц', callback_data='otvet')
        keyboard.add(key_month)
        bot.send_message(message.from_user.id, 'На какой срок вы ставите цели?', reply_markup=keyboard)
    elif message.text == 'Планы':
        keyboard = types.InlineKeyboardMarkup()
        key_d1 = types.InlineKeyboardButton(text=current_date1, callback_data='otvet1')
        keyboard.add(key_d1)
        key_d2 = types.InlineKeyboardButton(text=current_date2, callback_data='otvet2')
        keyboard.add(key_d2)
        key_d3 = types.InlineKeyboardButton(text=current_date3, callback_data='otvet3')
        keyboard.add(key_d3)
        bot.send_message(message.from_user.id, 'Выберите нужный день', reply_markup=keyboard)


bot.polling()