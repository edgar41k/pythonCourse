# while True:
#     idcode = input('Please enter your national id: ')
#     if idcode.isdecimal():
#         if len(idcode) != 11:
#             if len(idcode) < 11:
#                 print('ID you entered is too short')
#                 continue
#             else:
#                 print('ID you entered is too long')
#         else:
#             while True:
#                 name = input('Enter name:')
#                 if not name:
#                     print('Try again!')
#                     continue
#                 # exit()
#                 # quit()
#                 break
#             break
#     else:
#         print('Failed')
#
# print('Good bye!')
# защита от ошибки
# try:
#     int('123')
# except:
#     print('ERROR')
# else:
#     print('NO ERROR')
# finally:
#     print('Good bye!')
# try:
#     name = input('Enter name: ')
#     if not name:
#         raise Exception
# except ValueError:
#     print('Dont divide by 0')
# except Exception:
#     print('Name is empty')
# else:
#     print('NO ERROR')
# finally:
#     print('Good bye!')
# empty = {} пустой словарь
# empty = dict()
# print(type(empty))
#from random import sample
#
# x = 5
# sample = {
#     'name' : 'Jack',
#     'courses' : ['Art', 'English', 'Programming'],
#     1: 'int key',
#     0.2: 'float key',
#     x: 'variable key'
#     }
# # print(sample['courses'][2])
# # print(sample.get('names', []))
#
# sample['name'] = 'Sarah'
# sample['phone'] = '555-555-5555'
# print(sample)
#
# sample.update({'name': 'Mark', 'aadress': 'Tallinn' })
# print(sample)
#
# del sample['name']
# print(sample)
#
# courses = sample.pop('courses')
# print(courses)
# print(sample)

# sample2 = {'name': 'Jack', 'surname': 'Smith', 'age': 40}
# for x in sample2:
#     print(sample2[x])
#
# print(sample2.keys())
# print(sample2.values())
# print(sample2.items())
#
# for key, value in sample2.items():
#     print(key, value)
# def say_welcome(name, surname):
#     return f'Welcome {name}, {surname}!'
#
# x = say_welcome('Roman', 'Kutselepa')
# print(x)

# def short_or_long(string):
#     if len(string) > 5:
#         return 'long'
#     else:
#         return 'short'
#     print('Goodbye')
#
# print(short_or_long('long'))
#
# words = ['Sun', 'Helium', 'Parralax', 'Instrumentarium']
# for word in words:
#     print(short_or_long(word))
#
# def fizz_buzz(start, end):
#     for num in range(start, end + 1):
#         if num % 3 == 0 and num % 5 == 0:
#             print(num, 'FIZZ')
#         elif num % 3 == 0:
#             print(num, 'BUZZ')
#         elif num %  5 == 0:
#             print(num, 'BUZZ')
#
# fizz_buzz(-100, 200)

# a = 1
# b = 2
# c = 3
#
# def sample():
#     global a, b
#     a = 10
#     b = 20
#     c = 30
#     print(a, b, c)
#
# sample()
# print(a, b, c)

# a = 100
# def sample(a):
#     print(a ** 2)
#
# print(a)

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area  = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area
# print(triangle_area(3, 4, 5))


def print_result():
    print(f'The area of triangle is {triangle_area(3, 4, 5)}')


print_result()
