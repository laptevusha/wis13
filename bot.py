import telebot

bot = telebot.TeleBot("6186334339:AAH0PNwLuzTMJlHvTEa496HGKDrwp8iMdMQ")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
