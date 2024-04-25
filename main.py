import telebot
import datetime
from telebot import types
from datetime import date
import sqlite3

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
    bot.send_message(m.chat.id, 'Введите логин')
    bot.register_next_step_handler(m, user_pass)


def user_pass(m):
    password = m.text.strip()
    insert_varible_into_table(password)
    bot.send_message(m.chat.id, 'Готово!')

def user_pass1(m):
    password = m.text.strip()
    insert_varible_into_table_1(password)
    bot.send_message(m.chat.id, 'Готово!')

def user_pass2(m):
    password = m.text.strip()
    insert_varible_into_table_2(password)
    bot.send_message(m.chat.id, 'Готово!')

def user_purpose(m):
    purpose = m.text.strip()
    insert_varible_into_table2(purpose)
    bot.send_message(m.chat.id, 'Готово!')

def user_purpose1(m):
    purpose = m.text.strip()
    insert_varible_into_table3(purpose)
    bot.send_message(m.chat.id, 'Готово!')

def user_purpose2(m):
    purpose = m.text.strip()
    insert_varible_into_table4(purpose)
    bot.send_message(m.chat.id, 'Готово!')

def insert_varible_into_table(name):
    try:
        sqlite_connection = sqlite3.connect('web.sql')
        cursor = sqlite_connection.cursor()
        cursor.execute("""INSERT INTO plans
                                             (data, text)
                                             VALUES (?, ?)""", (current_date, name))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def insert_varible_into_table_1(name):
    try:
        sqlite_connection = sqlite3.connect('web.sql')
        cursor = sqlite_connection.cursor()
        cursor.execute("""INSERT INTO plans
                                             (data, text)
                                             VALUES (?, ?)""", (current_date + datetime.timedelta(days=2), name))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def insert_varible_into_table_2(name):
    try:
        sqlite_connection = sqlite3.connect('web.sql')
        cursor = sqlite_connection.cursor()
        cursor.execute("""INSERT INTO plans
                                             (data, text)
                                             VALUES (?, ?)""", (current_date + datetime.timedelta(days=1), name))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def insert_varible_into_table2(name):
    try:
        sqlite_connection = sqlite3.connect('web.sql')
        cursor = sqlite_connection.cursor()
        cursor.execute("""INSERT INTO web1
                                             (year)
                                             VALUES (?)""", (name,))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def insert_varible_into_table3(name):
    try:
        sqlite_connection = sqlite3.connect('web.sql')
        cursor = sqlite_connection.cursor()
        cursor.execute("""INSERT INTO web1
                                             (six_months)
                                             VALUES (?)""", (name,))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def insert_varible_into_table4(name):
    try:
        sqlite_connection = sqlite3.connect('web.sql')
        cursor = sqlite_connection.cursor()
        cursor.execute("""INSERT INTO web1
                                             (month)
                                             VALUES (?)""", (name,))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

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
        key_year = types.InlineKeyboardButton(text='Год', callback_data='year')
        keyboard.add(key_year)
        key_sixmonths = types.InlineKeyboardButton(text='Полгода', callback_data='six_months')
        keyboard.add(key_sixmonths)
        key_month = types.InlineKeyboardButton(text='Месяц', callback_data='month')
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


@bot.callback_query_handler(func=lambda call: call.data in ['otvet1', 'otvet2', 'otvet3'])
def date_clicked(call):
    if call.data == 'otvet1':
        data = current_date1
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите планы:')
        bot.register_next_step_handler(call.message, user_pass)
    elif call.data == 'otvet2':
        data = current_date2
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите планы:')
        bot.register_next_step_handler(call.message, user_pass1)
    elif call.data == 'otvet3':
        data = current_date3
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите планы:')
        bot.register_next_step_handler(call.message, user_pass2)

@bot.callback_query_handler(func=lambda call: call.data in ['year', 'six_months', 'month'])
def date_clicked(call):
    if call.data == 'year':
        data = current_date1
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id,'Введите цель:')
        bot.register_next_step_handler(call.message, user_purpose)
    elif call.data == 'six_months':
        data = current_date2
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите цель:')
        bot.register_next_step_handler(call.message, user_purpose1)
    elif call.data == 'month':
        data = current_date3
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите цель:')
        bot.register_next_step_handler(call.message, user_purpose2)

bot.polling()