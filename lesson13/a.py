import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import telebot
from telebot import types
import dataframe_image as dfi
from datetime import datetime

bot = telebot.TeleBot('6165404922:AAHg7bUiRP5Ism12SssmJ1mOOWLKB_Argys')
coordinates = {
    'Бауыржан Момышулы': '43.216438,76.837982',
    'Сарыарка': '43.223665,76.858230',
    'Москва': '43.230834,76.867593',
    'Сайран': '43.236646,76.876991',
    'Алатау': '43.238726,76.897613',
    'Мухтара Ауэзова': '43.240085,76.917960',
    'Байконыр': '43.240208,76.927250',
    'Абая': '43.242804,76.949849',
    'Алмалы': '43.251635,76.946115',
    'Жибек-Жолы': '43.260379,76.945800',
    'Райымбек-Батыра': '43.271375,76.944659'
}

def get_time():
    site = requests.get('http://metroalmaty.kz/?q=ru/schedule-list').text
    soup = BeautifulSoup(site, 'html.parser')
    table = soup.tbody.find_all('tr')
    head = ['Станции','Время прибытия (Райымбек батыра - Б. Момышулы)', 'Время прибытия (Б. Момышулы - Райымбек батыра)']
    rows = []
    with open('time.csv', 'w') as time_file:
        f = csv.writer(time_file)
        for i in table:
            column = i.find_all('td')
            row = []
            for j in column:
                row.append(j.text)
            rows.append(row)
        f.writerow(head)
        f.writerows(rows)
        
    return rows

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    if name == None:
        name = last_name
    if name == None:
        name = username
    if name == None:
        name = 'Anonim'
    to_rep = bot.send_message(message.chat.id, f"""Привет, <strong>{name}</strong>🖐🏻\n\nМеня зовут Метротик, я знаю расписание поездов в метро Алматы. Напиши <strong>/help</strong> для более подробной информации.""" , parse_mode='html')
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    ff=types.KeyboardButton('Ближайшая станция', request_location=True)
    new_button = types.KeyboardButton('Определенная станция')
    keyboard.add(ff, new_button)

    bot.reply_to(to_rep, "Выберите действие", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Если вы хотите узнать расписание поезда определнной станции нажмите\n\n\n<strong>Определенная станция -> Выберите станцию</strong>\n\n\nМожете посмотреть ближайшую к вам станцию нажав на кнопку <strong>Ближайшая станция</strong>', parse_mode='html')

@bot.message_handler(content_types=['location'])
def handle_location(message):
    api_key = 'B1CmKcutpNFpQlVisGnaSACUCblDfs8p'
    latitude = message.location.latitude
    longitude = message.location.longitude
    start_location = f'{latitude},{longitude}'
    station = ''
    min_len = 999999999999999999
    for i, j in coordinates.items():
        end_location = j
        url = f'https://api.tomtom.com/routing/1/calculateRoute/{start_location}:{end_location}/json?key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            # Success! The response content is in JSON format.
            json_response = response.json()
            lengthInMeters = json_response['routes'][0]['summary']['lengthInMeters']
            if (lengthInMeters < min_len):
                min_len = lengthInMeters
                station = i

    bot.send_message(message.chat.id, f'Ближайшая станция - {station}')



@bot.message_handler()
def get_messages(message):
    for i in get_time():
        if message.text == i[0]:
            time = datetime.now()
            time1 = i[1]
            time2 = i[2]
            if len(time1) == 0:
                time1 = "Конечная"
            if len(time2) == 0:
                time2 = 'Конечная'
            bot.send_message(message.chat.id, f'Расписание на время - {time.strftime("%H:%M:%S")}\n\n\nСтанция - {i[0]}\nОт {i[0]} До Бауыржан Момышулы:\n{time1}\n\nОт {i[0]} До Райымбек Батыра:\n{time2}')
            
        
    if message.text == 'Определенная станция':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add('<- Назад')
        for i in get_time():
            keyboard.add(i[0])
        bot.reply_to(message, 'Выберите станцию',reply_markup=keyboard)
    
    if message.text == '<- Назад':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        ff=types.KeyboardButton('Ближайшая станция', request_location=True)
        new_button = types.KeyboardButton('Определенная станция')
        keyboard.add(ff, new_button)

        bot.reply_to(message, "Выберите действие", reply_markup=keyboard)    



def save_image():
    df = pd.read_csv('time.csv')
    df_styled = df.style.background_gradient()
    dfi.export(df_styled,"mytable.png")

bot.infinity_polling()