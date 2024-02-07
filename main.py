import telebot
import webbrowser

bot = telebot.TeleBot(
    token='6534512588:AAGFatTlsX_lAVNVAkNG-CsOapk3ObSzW4U')


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://t.me/lkv414_bot/lkv414')


@bot.message_handler(commands=['start','main','hello'])
def main(massage):
    bot.send_message(massage.chat.id,f'ПИСЬКА, {massage.from_user.first_name}')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,f'ты лох, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID, {message.from_user.id}')


bot.infinity_polling()

#сделать открывающеися приложение в самом телеграмме что бы там был сам этот функционал