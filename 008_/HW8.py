# Напишите функцию которая принимает список из строк
# Возвращает список строк, которые являются палиндромом
# Читаются слева направо и наоборот - одинаково
# Пример 'rotator'

# strings = [
#     "racecar",
#     "hello",
#     "madam",
#     "world",
#     "level",
#     "open",
#     "rotor",
#     "javascript"
# ]

# def is_palindrome(s): # функция проверки палиндрома
#     return s.lower() == s.lower()[::-1] # lower() - переводит все буквы в нижний регистр
#
# strings = [
#     "racecar",
#     "hello",
#     "madam",
#     "world",
#     "level",
#     "open",
#     "rotor",
#     "javascript"
# ]
#
# for s in strings: # перебираем все строки
#     if is_palindrome(s): # если строка палиндром
#         print(f'"{s}" is a palindrome.') # печатаем палиндром
#     else: # если строка не палиндром
#         print(f'"{s}" is not a palindrome.') # печатаем не палиндром
#
#
# # Напишите программу которая добавит в новый массив только совершеннолетних
# people = [
#     {
#         "name": "Jack",
#         "age": 15
#     },
#     {
#         "name": "Sarah",
#         "age": 21
#     },
#     {
#         "name": "Bob",
#         "age": 54
#     },
#     {
#         "name": "Mary",
#         "age": 12
#     },
#     {
#         "name": "Simon",
#         "age": 18
#     },
#     {
#         "name": "Jonhatan",
#         "age": 17
#     }
# ]
# for person in people: # перебираем массив
#     if person['age'] >= 18: # если возраст больше или равен 18
#         print(f'This is {person["name"]}. He is {person["age"]} years old', person) # печатаем совершеннолетней


# Напишите программу которая выберет из данного массива книги изданые в 2023
# В новый массив добавит объекты в которых ключом будет имя автора, а значением название книги

# books = [
#     {
#         "author": "Jeremy Brook",
#         "title": "My childhood",
#         "release": 2023
#     },
#     {
#         "author": "Samantha Jhones",
#         "title": "Living with ten cats",
#         "release": 2020
#     },
#     {
#         "author": "Bob Summers",
#         "title": "Exploring far space",
#         "release": 2021
#     },
#     {
#         "author": "Bill Brown",
#         "title": "Insects in our garden",
#         "release": 2023
#     },
#     {
#         "author": "Jessica Love",
#         "title": "Programming for beginners",
#         "release": 2023
#     }
# ]
# for books in books: # перебираем массив
#     if books["release"] == 2023: # если год издания равен 2023
#         print(books) # печатаем книги


# ЗАДАНИЯ НИЖУ
cars = [
    {
        "make": "Toyota",
        "model": "Camry",
        "year": 2020,
        "price": 24000,
        "specifications": {
            "engine": "2.5L I4",
            "horsepower": 203,
            "fuelType": "Gasoline",
            "transmission": "Automatic",
        },
        "owner": {
            "name": "John Doe",
            "address": {
                "street": "123 Maple St",
                "city": "Springfield",
                "state": "IL",
                "zip": "62704",
            },
        },
    },
    {
        "make": "Honda",
        "model": "Accord",
        "year": 2018,
        "price": 22000,
        "specifications": {
            "engine": "1.5L I4",
            "horsepower": 192,
            "fuelType": "Gasoline",
            "transmission": "Automatic",
        },
        "owner": {
            "name": "Jane Smith",
            "address": {
                "street": "456 Oak Ave",
                "city": "Madison",
                "state": "WI",
                "zip": "53703",
            },
        },
    },
    {
        "make": "Ford",
        "model": "Mustang",
        "year": 2019,
        "price": 26000,
        "specifications": {
            "engine": "2.3L I4",
            "horsepower": 310,
            "fuelType": "Gasoline",
            "transmission": "Manual",
        },
        "owner": {
            "name": "Bob Johnson",
            "address": {
                "street": "789 Pine Rd",
                "city": "Austin",
                "state": "TX",
                "zip": "73301",
            },
        },
    },
    {
        "make": "Chevrolet",
        "model": "Malibu",
        "year": 2021,
        "price": 27000,
        "specifications": {
            "engine": "1.5L I4",
            "horsepower": 160,
            "fuelType": "Gasoline",
            "transmission": "Automatic",
        },
        "owner": {
            "name": "Alice Brown",
            "address": {
                "street": "101 Elm St",
                "city": "Denver",
                "state": "CO",
                "zip": "80201",
            },
        },
    },
    {
        "make": "Tesla",
        "model": "Model 3",
        "year": 2022,
        "price": 35000,
        "specifications": {
            "engine": "Electric",
            "horsepower": 283,
            "fuelType": "Electric",
            "transmission": "Automatic",
        },
        "owner": {
            "name": "Charlie Davis",
            "address": {
                "street": "202 Cedar Dr",
                "city": "San Francisco",
                "state": "CA",
                "zip": "94102",
            },
        },
    },
    {
        "make": "BMW",
        "model": "X5",
        "year": 2021,
        "price": 50000,
        "specifications": {
            "engine": "3.0L I6",
            "horsepower": 335,
            "fuelType": "Gasoline",
            "transmission": "Automatic",
        },
        "owner": {
            "name": "Emily Wilson",
            "address": {
                "street": "303 Birch Ln",
                "city": "Seattle",
                "state": "WA",
                "zip": "98101",
            },
        },
    },
    {
        "make": "Audi",
        "model": "A4",
        "year": 2017,
        "price": 28000,
        "specifications": {
            "engine": "2.0L I4",
            "horsepower": 252,
            "fuelType": "Gasoline",
            "transmission": "Automatic",
        },
        "owner": {
            "name": "David Miller",
            "address": {
                "street": "404 Walnut St",
                "city": "Portland",
                "state": "OR",
                "zip": "97201",
            },
        },
    },
    {
        "make": "Mercedes-Benz",
        "model": "C-Class",
        "year": 2019,
        "price": 42000,
        "specifications": {
            "engine": "2.0L I4",
            "horsepower": 255,
            "fuelType": "Gasoline",
            "transmission": "Automatic",
        },
        "owner": {
            "name": "Sarah Green",
            "address": {
                "street": "505 Spruce St",
                "city": "Boston",
                "state": "MA",
                "zip": "02108",
            },
        },
    },
]

# Попробуйте оформить каждое задание в виде функции
# 1. Отфильтруйте бензиновые машины и добавьте в новый список марку и модель
# пример: ['BMW 520i', 'Audi A5', 'VW Golf']

# def gasoline_cars(cars):
#     for cars in cars:
#         if cars["specifications"]["fuelType"] == "Gasoline":
#             print(cars["make"] + " " + cars["model"])
# # gasoline_cars(cars)
# print(list(map(lambda cars: cars["make"] + " " + cars["model"], cars))) # с помощью map


# 2. Отфильтруйте машины которые стоят больше 30000 и добавьте в новй список словари
# пример словарей: {make: 'BMW', model: '528i', owner_name: 'Jack Smith'}

# for car in filter(lambda car: car["price"] > 30000, cars):
#     print(car)


# 3. Используйте метод map() чтобы создать новый массив из владельцев
# Пример:
# [{"John Doe": {
#     "street": "123 Maple St",
#     "city": "Springfield",
#     "state": "IL",
#     "zip": "62704",

# map(lambda car: car["owner"]["name"], cars)
# print(list(map(lambda car: car["owner"]["name"], cars)))

