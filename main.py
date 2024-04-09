import telebot

bot = telebot.TeleBot('7032417900:AAFnXx--IFE8Nb71hiefFj4HCimo5QwuSVo')

@bot.message_handler(commands=['start',])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.infinity_polling()