from bs4 import BeautifulSoup
import requests

page = requests.get('https://ru.wikipedia.org/wiki/Всемирный_день_борьбы_против_туберкулёза').text
soup = BeautifulSoup(page, 'html.parser')
print(soup.find_all('ul')[1].text)