import tkinter as tk
my_w = tk.Tk()
my_w.geometry("300x200")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

options = tk.StringVar(my_w)
options.set("One") # default value

l3 = tk.Label(my_w,  text='Select One', width=15 )  
l3.grid(row=5,column=1) 

om1 =tk.OptionMenu(my_w, options, "HTML","PHP", "MySQL", "Python")
om1.grid(row=5,column=2) 
my_w.mainloop()