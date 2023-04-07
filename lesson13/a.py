import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import telebot
import dataframe_image as dfi
from datetime import datetime


bot = telebot.TeleBot('6165404922:AAHg7bUiRP5Ism12SssmJ1mOOWLKB_Argys')

@bot.message_handler(commands=['start'])
def start(message):
    link = 'https://almatycity.kz/wp-content/uploads/2022/06/almaty-metro-схема.png'
    bot.send_photo(message.chat.id, link, 'Привет! Меня зовут Метротик, я знаю расписание поездов в метро Алматы. Напиши <strong>ВРЕМЯ</strong> чтобы узнать расписание.' , parse_mode='html')

@bot.message_handler()
def get_messages(message):
    if message.text.lower() == 'время':
        time = datetime.now()
        save_image(get_time())
        bot.send_photo(message.chat.id, open('mytable.png', 'rb'), f'Расписание на время - {time.strftime("%H:%M:%S")}')
        

def get_time():
    site = requests.get('http://metroalmaty.kz/?q=ru/schedule-list').text
    soup = BeautifulSoup(site, 'html.parser')
    table = soup.tbody.find_all('tr')
    head = ['Станции','Время прибытия (Райымбек батыра - Б. Момышулы)', 'Время прибытия (Б. Момышулы - Райымбек батыра)']
    with open('time.csv', 'w') as time_file:
        f = csv.writer(time_file)
        rows = []
        for i in table:
            column = i.find_all('td')
            row = []
            for j in column:
                row.append(j.text)
            rows.append(row)
        f.writerow(head)
        f.writerows(rows)
        
    df = pd.read_csv('time.csv')
    return df

def save_image(data):
    df = data
    df_styled = df.style.background_gradient()
    dfi.export(df_styled,"mytable.png")

bot.infinity_polling()