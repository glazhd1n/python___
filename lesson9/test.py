import requests
from tkinter import *

def getMoney(currency):
    b = requests.get(f'https://api.freecurrencyapi.com/v1/latest?apikey=2YdhWYt4Jge9Xo712ykDOdFabVcZ5jV3925lG4YL&currencies=EUR%2CUSD%2CRUB&base_currency={currency}').json()['data']
    eur = b['EUR']
    usd = b['USD']
    rub = b['RUB']
    lbl = Label(root, text=f'EUR {eur}\nUSD {usd}\n RUB {rub}')
    lbl.grid(row=6, columnspan=5)

a = requests.get('https://api.freecurrencyapi.com/v1/latest?apikey=2YdhWYt4Jge9Xo712ykDOdFabVcZ5jV3925lG4YL')
a = a.json()['data']
c = []
for i, j in a.items():
    c.append(i)

root = Tk()
options = StringVar(root)
options.set("Choise")
btn = Button(root, text='convert', command=lambda: getMoney(options.get()))
om1 = OptionMenu(root, options, *c)
btn.grid(row=5,column=3)
om1.grid(row=5,column=2) 
root.mainloop()