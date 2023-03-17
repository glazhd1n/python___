import telebot
import requests

bot = telebot.TeleBot('6167273283:AAG4GKgK0TR5oC8b9yGLxEBccJ0VszjHDGo')

@bot.message_handler()
def send_message(message):
    try:
        url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid=e903c049b4d03dc6fa46a716693acb3f').json()
        weather = url['main']['temp']
        bot.send_message(message.chat.id, f'На данный момент в городе {message.text} - {round(weather - 273.15, 3)} градусов Цельсия')
    except:
        bot.send_message(message.chat.id, 'Такого города в нашей базе к сожалению нет\nВыберите город из этого списка:\n')
        cities_list = open('cities_file.txt', 'r').read().split(',')
        list_1 = []
        for i in cities_list:
            list_1.append(i)
            if(len(list_1) == 20):
                cities = ''
                for j in list_1:
                    cities += j + '\n'
                bot.send_message(message.chat.id, cities)
                list_1.clear()
        else:
            cities = ''
            for j in list_1:
                cities += j + '\n'
            bot.send_message(message.chat.id, cities)
            list_1.clear()


bot.infinity_polling()