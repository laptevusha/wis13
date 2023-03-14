import os
from flask import Flask, request
import telegram

TOKEN = ['6186334339:AAH0PNwLuzTMJlHvTEa496HGKDrwp8iMdMQ']
bot = telegram.Bot(TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # получаем сообщение от пользователя
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    # получаем id чата и текст сообщения
    chat_id = update.message.chat_id
    text = update.message.text

    # отправляем ответ пользователю
    bot.send_message(chat_id=chat_id, text=text)

    return 'ok'

if __name__ == '__main__':
    app.run()
