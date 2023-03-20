import telebot

bot = telebot.TeleBot("YOUR_API_TOKEN_HERE")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
