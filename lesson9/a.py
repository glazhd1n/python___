from tkinter import *

def changeText():
    lbl = Label(root, width=20, text="Button Tapped", foreground='red', background='blue', padx=10, pady=10, borderwidth=5)
    lbl.grid(row=2)    
root = Tk()
root.title("First app")
btn1 = Button(root, width=5, text="1")
btn2 = Button(root, width=5, text="2")
btn3 = Button(root, width=5, text="3")
btn1.grid(row=0)
btn2.grid(row=1, column=0)
lbl = Label(root, width=30, text="Hello World")
btn = Button(root, width=5, text="My Button", command=changeText)
btn.grid(row=1, column=1)
lbl.grid(row=2)

root.mainloop()