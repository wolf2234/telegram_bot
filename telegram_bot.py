import telebot
from telebot import types

bot = telebot.TeleBot('5563168020:AAGmUtuQTu7h5gGiP4yxskseQll5TegBOuU')


@bot.message_handler(commands=['start'])
def start(message):
    mass = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mass, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'Hello, nice to meet you!', parse_mode='html')
#     elif message.text == 'ID':
#         bot.send_message(message.chat.id, f'Your id is {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('pyshot_logo.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "I don't understand you", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Ahh, it is beautifuly!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit website!", url="https://itproger.com"))
    bot.send_message(message.chat.id, 'Go to the website.', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    website = types.KeyboardButton('Website')
    start = types.KeyboardButton('Start')

    markup.add(website, start)
    bot.send_message(message.chat.id, 'Go to the website.', reply_markup=markup)


bot.polling(none_stop=True)
