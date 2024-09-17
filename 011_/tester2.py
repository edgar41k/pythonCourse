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

class Developer(Employee):

    def __init__(self, name, surname, salary, prog_lang):
        super().__init__(name, surname, salary)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, name, surname, salary, employees=None):
        super().__init__(name, surname, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


emp1 = Employee('John', 'Smith', 2000)  
dev1 = Developer('Luke', 'Palk', 3000, 'Python')
man1 = Manager('Anti', 'Samanti', 4000, [emp1, dev1])


# print(issubclass(Developer, Employee))
# print(isinstance(man1, Developer))
# man1.add_employee(dev1)
# print(man1.employees)


