import telebot

bot = telebot.TeleBot(
    token='6534512588:AAGFatTlsX_lAVNVAkNG-CsOapk3ObSzW4U')

@bot.message_handler(commands=['start'])
def main(massage):
    bot.send_message(massage.chat.id, 'ПИСЬКА')

bot.polling(none_stop=True)