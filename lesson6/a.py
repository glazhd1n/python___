class Person():
    def __init__(self, full_name, id, age):
        self.full_name = full_name
        self.id = id
        self.age = age
    
    def getName(self):
        return self.full_name

    def getId(self):
        return self.id

    def getAge(self):
        return str(self.age)

    def setName(self, new_name):
        self.full_name = new_name
    
    def getFullInfo(self):
        return self.getName() + '\n' + self.getId() + '\n' + self.getAge()
a = []
a.append(Person('Sabir', '1111', 19))
a.append(Person('AqBota', '3333', 19))

for i in a:
    print(i.getFullInfo())