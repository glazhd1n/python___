from tkinter import *
from PIL import Image, ImageTk
import json

def logIn(root, login, password):
    with open('fake_db.json', 'r') as db:
        read_db = json.load(db)
        has_account = read_db['students'].get(login)
    if has_account == None:
        lb = Label(root, text='No user like this in our database', fg='Red').pack()
        return
    if password != read_db['students'].get(login).get('password'):
        lb = Label(root, text='Incorrect login or password', fg='Red').pack()
        return
    root.destroy()
    new_root = Tk()
    new_root.geometry('800x600')
    img = ImageTk.PhotoImage(Image.open("success.jpg"))
    Label(new_root, image=img).pack()
    new_root.mainloop()


def submit(new_root, email, password, confirm_password):
    with open('fake_db.json', 'r') as db:
        read_db = json.load(db)
        if read_db['students'].get(email.get()) != None:
            lb = Label(new_root, text='This email already taken', fg='Red').pack()
        elif password.get() != confirm_password.get():
            lb = Label(new_root, text='Passwords are not same', fg='Red').pack()
        else:
            read_db['students'].update({email.get() : {'password': password.get()}})
            with open('fake_db.json', 'w') as to_write:
                json.dump(read_db, to_write, indent=4)

def register(root):
    root.destroy()
    new_root = Tk()
    new_root.geometry('800x600')
    email = Entry(new_root)
    password = Entry(new_root, show='*')
    confirm_password = Entry(new_root, show='*')
    submit_button = Button(new_root, text='Submit', command=lambda: submit(new_root, email, password, confirm_password))
    Label(new_root, text='email').grid(row=0, column=0)
    Label(new_root, text='password').grid(row=1, column=0)
    Label(new_root, text='confirm password').grid(row=2, column=0)
    email.grid(row=0, column=1)
    password.grid(row=1, column=1)
    confirm_password.grid(row=2, column=1)
    submit_button.grid(row=3, columnspan=2)


    new_root.mainloop()

def main():
    root = Tk()
    root.geometry('800x600')
    email = Entry(root)
    password = Entry(root, show='*')
    em = Label(root, text='email').grid(row=0, column=0)
    ps = Label(root, text='password').grid(row=1, column=0)
    loggin_button = Button(root, text='Log In', command=lambda: logIn(root, email.get(), password.get()))
    register_button = Button(root, text='Register', command=lambda: register(root, ))

    email.grid(row=0, column=1)    
    password.grid(row=1, column=1)
    loggin_button.grid(row=2, columnspan=2)
    register_button.grid(row=3, columnspan=2)

    root.mainloop()

if __name__ == '__main__':
    main()