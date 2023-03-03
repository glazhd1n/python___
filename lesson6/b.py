class Employee():
    def __init__(self, full_name, salary, department):
        self.full_name = full_name
        self.salary = salary
        self.department = department
    
    def getName(self):
        return self.full_name

    def getDepartment(self):
        return self.department

    def getSalary(self):
        return str(self.salary)
    
    def getFullInfo(self):
        return self.getName() + '\n' + self.getDepartment() + '\n' + self.getSalary()

def Manager(Employee):
    def __init__(self, full_name, salary, department, budget, count_of_employees):
        super().__init__(full_name, salary, department)
        self.budget = budget
        self.count_of_employees = count_of_employees
    
    def getBudget(self):
        return str(self.budget)

    def getCountOfEmployees(self):
        return str(self.count_of_employees)

    def getFullInfo(self):
        return super().getFullInfo() + '\n' + self.getBudget() + '\n' + self.getCountOfEmployees()

    

emp = Employee('Robert Johnson', 1000000, 'IT')
man = Manager('Sabir Glazhdin', 1000000000, 'Head of IT department', 200000000000, 2)

print(emp.getFullInfo())
print(man.getFullInfo())