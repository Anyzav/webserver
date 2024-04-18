import telebot
from telebot import types

bot = telebot.TeleBot('7032417900:AAFnXx--IFE8Nb71hiefFj4HCimo5QwuSVo')
a = ['год', 'Год', 'месяц', 'Месяц', 'Полгода', 'полгода']


@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = (types.KeyboardButton('/start'))
    btn2 = (types.KeyboardButton('/help'))
    btn3 = (types.KeyboardButton('привет'))
    btn4 = (types.KeyboardButton('id'))
    btn5 = (types.KeyboardButton('Написать планы на день'))
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
        bot.send_message(message.from_user.id, 'На какой срок вы ставите цели?год, полгода, месяц')
    if message.text in a:
        target_date = message.text
        bot.send_message(message.from_user.id, 'Напишите цели')
    elif message.text == 'Написать планы на день':
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='otvet')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='otvet')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, 'Нужны ли вам напоминания для выполнения планов?', reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)