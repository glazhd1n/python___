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
            return
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



pb = PhoneBook()

pb.edit_user(name='hjsfgjh', new_country='Sweden')
pb.edit_user('Sabir', new_country='USA')
pb.edit_user('Adelya', new_country='German')
pb.printUsers()