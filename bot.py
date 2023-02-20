import telebot
import datetime

# Задаем токен бота, который вы получили от BotFather
TOKEN = '6021283271:AAHf99148Uh0qXQ2eweCNFb43ceLw3T6_Ts'

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Создаем обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я могу вычислить разницу между двумя датами и проверить, является ли она больше двух третьих. Просто отправь мне две даты в формате ДД.ММ.ГГГГ через пробел.")

# Создаем обработчик сообщений с двумя датами
@bot.message_handler(func=lambda message: len(message.text.split()) == 2)
def calculate_diff(message):
    # Разбиваем сообщение на две даты
    date_strings = message.text.split()
    try:
        date1 = datetime.datetime.strptime(date_strings[0], '%d.%m.%Y')
        date2 = datetime.datetime.strptime(date_strings[1], '%d.%m.%Y')
    except ValueError:
        bot.reply_to(message, "Неправильный формат даты. Используйте формат ДД.ММ.ГГГГ.")
        return

    # Вычисляем разницу между датами
    date_diff = abs(date2 - date1).days

    # Вычисляем две третьих от разницы дат
    two_thirds_diff = date_diff * (2 / 3)

    # Проверяем, является ли разница больше двух третьих
    if date_diff > two_thirds_diff:
        bot.reply_to(message, f"Разница между датами равна {date_diff} дням, что больше чем две третьих от разницы. Принимай!")
    else:
        bot.reply_to(message, f"Разница между датами равна {date_diff} дням, что меньше чем две третьих от разницы. Не принимай.")

# Запускаем бота
bot.polling()
