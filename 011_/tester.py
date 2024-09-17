import datetime
class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, name, surname, salary):
        self.name = name.title()
        self.surname = surname.title()
        self.salary = salary
        self.email = f'{name.lower()}.{surname.lower()}@company.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return f'{self.name.title()} {self.surname.title()}'
    

    def raise_salary(self):
        self.salary *= self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


    @classmethod
    def amp_from_string(cls, string):
        name, surname, salary = string.split('-')
        return cls(name.title(), surname.title(), float(salary))

    @staticmethod
    def is_workday(day):
        if day.workday() in [5, 6]:
            return False
        return True
    

emp1 = Employee( 'John', 'Smith', 2000)
emp2 = Employee.amp_from_string('john-smith-3000')
print(emp2.salary)

now = datetime.datetime.today()
print(Employee.is_workday(now))


# print(Employee.__dict__)
# print(emp1.__dict__)
# print(Employee.fullname(emp1))
# print(emp1.fullname())
# print(emp1.email)
# print(emp1.num_of_employees)
# print(Employee.num_of_employees)
# print(emp1.__dict__)
# print(Employee.__dict__)
# emp1.raise_amount = 1.10
# print(emp1.__dict__)
# print(Employee.__dict__)
# emp1.raise_salary()
