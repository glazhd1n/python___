import psycopg2
from config import data

conn = psycopg2.connect(**data)
cursor = conn.cursor()

query = '''
select * from library;
'''

def add_people(name='', surname=''):
    query = f'''
        insert into chitatel (name, surname)
        values (\'{name}\', \'{surname}\')
    '''
    cursor.execute(query)
    conn.commit()

name = input()
surname = input()

add_people(name, surname)

cursor.execute(query)
response = cursor.fetchall()

for i in response:
    print(i)

cursor.close()
conn.close()