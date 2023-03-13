from tkinter import *

root = Tk()
label = Label(root, width=30, text="0")
string1 = ''
def addButton(text):
    global string1
    if(text in '+/-*'):
        if(len(string1) == 0):
            return
        elif(text in string1):
            return
        elif('*' in string1 or '+' in string1 or '-' in string1 or '/' in string1):
            return
    if(text == '='):
        if('*' in string1 or '+' in string1 or '-' in string1 or '/' in string1):
            string1 = str(eval(string1))
            label = Label(root, width=30, text=string1)
            label.grid(row=0, columnspan=4)
            return
        else:
            return

    string1 += text
    label = Label(root, width=30, text=string1)
    label.grid(row=0, columnspan=4)

def removeSymbol():
    global string1
    string1 = string1[:-1]
    label = Label(root, width=30, text=string1 if len(string1) > 0 else '0')
    label.grid(row=0, columnspan=4)

def removeAllSymbols():
    global string1
    string1 = ''
    label = Label(root, width=30, text='0')
    label.grid(row=0, columnspan=4)


btn1 = Button(root, width=5, text='1', command=lambda: addButton('1'))
btn2 = Button(root, width=5, text='2', command=lambda: addButton('2'))
btn3 = Button(root, width=5, text='3', command=lambda: addButton('3'))

btn4 = Button(root, width=5, text='4', command=lambda: addButton('4'))
btn5 = Button(root, width=5, text='5', command=lambda: addButton('5'))
btn6 = Button(root, width=5, text='6', command=lambda: addButton('6'))

btn7 = Button(root, width=5, text='7', command=lambda: addButton('7'))
btn8 = Button(root, width=5, text='8', command=lambda: addButton('8'))
btn9 = Button(root, width=5, text='9', command=lambda: addButton('9'))

btn0 = Button(root, width=5, text='0', command=lambda: addButton('0'))

btnPlus = Button(root, width=5, text='+', command=lambda: addButton('+'))
btnSubstraction = Button(root, width=5, text='-', command=lambda: addButton('-'))
btnDivision = Button(root, width=5, text='/', command=lambda: addButton('/'))
btnMultiply = Button(root, width=5, text='*', command=lambda: addButton('*'))
btnEquals = Button(root, width=5, text='=', command=lambda: addButton('='))
btnRemoveLastSymbol = Button(root, width=5, text='⌫', command=lambda: removeSymbol())
btnRemoveAll = Button(root, width=5, text='AC', command=lambda: removeAllSymbols())
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btnMultiply.grid(row=2, column=3)

btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btnSubstraction.grid(row=3, column=3)

btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
btnPlus.grid(row=4, column=3)
btnDivision.grid(row=5, column=2)
btnEquals.grid(row=5, column=3)
btnRemoveLastSymbol.grid(row=5, column=1)
btnRemoveAll.grid(row=5, column=0)
label.grid(row=0, columnspan=4)

root.mainloop()