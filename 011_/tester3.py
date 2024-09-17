class Employee:

    raise_amount = 1.04

    def __init__(self, name, surname, salary):
        self.name = name.title()
        self.surname = surname.title()
        self.salary = salary
        self.email = f'{name.lower()}.{surname.lower()}@company.com'


    def fullname(self):
        return f'{self.name.title()} {self.surname.title()}'


    def raise_salary(self):
        self.salary *= self.raise_amount


    def __str__(self):
        return self.fullname()

    
    def __add__(self, other):
        return self.salary + other.salary
    
    
emp1 = Employee('John', 'Smith', 2000)

print(1 + 2)
print('a' + 'b')

print(int.__add__(1, 2))