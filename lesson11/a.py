import csv
import pandas as pd

class User:
    def __init__(self, full_name, phone_number, birthday, country):
        self.full_name = full_name
        self.phone_number = phone_number
        self.birthday = birthday
        self.country = country

    def get_info(self):
        name = f'Name - {self.full_name}\n'
        phone_number = f'Phone Number - {self.phone_number}\n'
        birthday = f'Birthday - {self.birthday}\n'
        country = f'Country - {self.country}'
        return name + phone_number + birthday + country

    def save_user(self):
        check = open('users.csv', 'r').read()
        if(self.phone_number in check):
            return
        
        with open('users.csv', 'a') as fake_db:
            writer = csv.writer(fake_db)
            writer.writerow([self.full_name, self.phone_number, self.birthday, self.country])

    def checkUser(self, newUser):
        if self.birthday == newUser.birthday and self.full_name == newUser.full_name and self.country == newUser.country and self.phone_number == newUser.phone_number:
            return True
        return False

class PhoneBook:
    def __init__(self):
        self.Users = []
        self.get_from_csv()

    def addUser(self, User):
        for user in self.Users:
            if user.checkUser(User):
                return
        self.Users.append(User)
        User.save_user()
    
    def printUsers(self):
        df = pd.read_csv('users.csv')
        print(df)

    def save_all_users(self):
        for User in self.Users:
            User.save_user()
    
    def deleteUser(self, phone_number):
        file = open('users.csv', 'r').read()
        if not phone_number in file:
            return False
        file = file.split('\n')
        file.pop()
        for i in range(len(file)):
            if(phone_number in file[i]):
                file.pop(i)
                break
        with open('users.csv', 'w') as fake_db:
            writer = csv.writer(fake_db)
            for i in file:
                writer.writerow(i.split(','))
        return True

    def edit_user(self, name, new_name='', new_phone_number='', new_birthday='', new_country=''):
        for user in self.Users:
            if name == user.full_name:
                if(len(new_name) > 0):
                    user.full_name = new_name
                if(len(new_phone_number) > 0):
                    user.phone_number = new_phone_number
                if(len(new_birthday) > 0):
                    user.birthday = new_birthday
                if(len(new_country) > 0):
                    user.country = new_country
                break
        self.rewrite_all_users()

    def rewrite_all_users(self):
        with open('users.csv', 'w') as fake_db:
            writer = csv.writer(fake_db)
            for user in self.Users:
                writer.writerow([user.full_name, user.phone_number, user.birthday, user.country])

    def get_from_csv(self):
        file = open('users.csv', 'r').read().split('\n')
        
        file.pop()

        for i in file:
            user = User(*i.split(','))
            self.addUser(user)

    def isNameInUsers(self, name):
        for i in self.Users:
            if (name == i.full_name):
                return True
        return False


pb = PhoneBook()

while 1:
    try:
        pb.printUsers()
        print('\n\n')
    except:
        pass
    command = input('Введите 1 для того чтобы добавить контакт\nВведите 2 для того чтобы удалить контакт\nВведите 3 для того чтобы отредактировать контакт\nВведите 4 для того чтобы завершить программу\n - ')
    if(command == '1'):
        name = input('Введите Имя - ')
        phone_number = input('Введите номер телефона - ')
        birthday = input('Введите день рождения - ')
        country = input('Введите страну проживания - ')
        new_user = User(name, phone_number, birthday, country)
        pb.addUser(new_user)
    elif command == '2':
        phone_number = input('Введите номер телефона человека, которого вы хотите удалить\n - ')
        if not pb.deleteUser(phone_number):
            print('Вы ввели не корректный номер')
            continue
        print('Контакт удален')
    elif command == '3':
        print('Введите имя человека')
        name = input()
        if not pb.isNameInUsers(name):
            print('Человека с таким именем к сожалению нет')
            continue
        cmnd = input('Введите 1 чтобы обновить имя\nВведите 2 чтобы обновить номер телефона\nВведите 3 чтобы обновить день рождения\nВведите 4 чтобы обновить страну\n - ')
        if cmnd == '1':
            new_name = input('Введите новое имя\n- ')
            pb.edit_user(name, new_name=new_name)
        elif cmnd == '2':
            phone_number = input('Введите новый номер телефона\n- ')
            pb.edit_user(name, new_phone_number=phone_number)
        elif cmnd == '3':
            birthday = input('Введите новый день рождения')
            pb.edit_user(name, new_birthday=birthday)
        elif cmnd == '4':
            country = input()
            pb.edit_user(name, new_country=country)
        else:
            print('Выберите правильную комманду')
            continue
        print('Контакт изменен')

    elif command == '4':
        print('Всего доброго!')
        exit()
    else:
        print('Введите корректную комманду')
    print('\n\n\n')
