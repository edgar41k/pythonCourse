class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__module = model
        self.__year = year
        self.__color = color
        
    @property
    def make(self):
        return self.__make
    
@property
    def color(self):
        return self.__color

@color.setter
    def color(self, new_color):
        self.__color = new_color

@color.deleter
def color(self, new_color):
        self.__color = new_color


car1 = Car('audi', 'a4', 2016)
print(car1.__color)
print(car1.color)
print(car1.__dict__)

