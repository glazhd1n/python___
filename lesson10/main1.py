from numpy import delete
import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6167273283:AAG4GKgK0TR5oC8b9yGLxEBccJ0VszjHDGo')

current_point = 0
end_point = 10


@bot.message_handler(commands=["cities"])
def show_cities(message):
    global current_point, end_point
    markup_inline = types.InlineKeyboardMarkup()
    cities_list = open('cities_file.txt', 'r').read().split(',')
    for i in range(current_point, end_point):
        button = types.InlineKeyboardButton(cities_list[i], callback_data=cities_list[i])
        markup_inline.add(button)
    right = types.InlineKeyboardButton('=>', callback_data='right_button')
    left = types.InlineKeyboardButton('<=', callback_data='left_button')
    markup_inline.add(left, right)
    bot.send_message(message.chat.id, 'Выберите город', reply_markup=markup_inline)

@bot.callback_query_handler(func = lambda call: True)
def manage_call(call):
    if call.data == 'right_button':
        bot.delete_message(call.message.chat.id, call.message.id)
        go_forward(call.message)
    elif call.data == 'left_button':
        bot.delete_message(call.message.chat.id, call.message.id)
        go_back(call.message)
    url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={call.data}&appid=e903c049b4d03dc6fa46a716693acb3f').json()
    weather = url['main']['temp']
    bot.send_message(call.message.chat.id, f'На данный момент в городе {call.data} - {round(weather - 273.15, 3)} градусов Цельсия')

@bot.message_handler()
def send_message(message):
    try:
        url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid=e903c049b4d03dc6fa46a716693acb3f').json()
        weather = url['main']['temp']
        bot.send_message(message.chat.id, f'На данный момент в городе {message.text} - {round(weather - 273.15, 3)} градусов Цельсия')
    except:
        bot.send_message(message.chat.id, 'Такого города в нашей базе к сожалению нет\nВыберите город из этого списка:\n')
        cities_list = open('cities_file.txt', 'r').read().split(',')


bot.infinity_polling()