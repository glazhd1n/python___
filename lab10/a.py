import requests
import csv
from bs4 import BeautifulSoup

link = 'https://www.worldometers.info/coronavirus/#countries'
file = open('test.csv', 'w')
writer = csv.writer(file)
req = requests.get(link).text
soup = BeautifulSoup(req, 'html.parser')
a = soup.table.tbody.find_all('tr')
writer.writerow(['Counry Name', 'Total cases', 'Total deaths', 'Total recovered', 'Active cases', 'New cases', 'New deaths', 'Total tests', 'Population'])
for i in a:
    if i.get('class') != None:
        continue
    c = []
    for j in i:
        if j == '\n':
            continue
        c.append(j.text.strip())
    writer.writerow([c[1], c[2], c[4], c[6], c[8], c[3], c[5], c[12], c[14]])