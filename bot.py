import aiogram
import pandas
import config

bot = aiogram.Bot(token = config.TOKEN)

dp = aiogram.dispatcher.Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start(msg):
    await msg.reply('Поиск по полю '+config.FIELD_NAME)

@dp.message_handler()
async def search(msg):
    excel_data_df = pandas.read_excel(config.FILE_NAME, sheet_name=config.SHEET)
    key = msg.text
    data = excel_data_df.to_dict('records')
    for i in data:
        if str(i[config.FIELD_NAME]) == key:
            await bot.send_message(msg.from_user.id, make_readeble(i), parse_mode='html')
            return
    await bot.send_message(msg.from_user.id, 'Ничего не найдено')

def make_readeble(d):
    lines = []
    for key, value in zip(d.keys(), d.values()):
        lines.append('<b>'+str(key)+'</b>'+' : '+str(value))
    return '\n'.join(lines)
    
    

aiogram.utils.executor.start_polling(dp)