# dick_size = -2
#
# if dick_size > 0:
#     if dick_size <= 10:
#         print("Dick is too small")
#     elif dick_size < 12:
#         print("Nah br!")
#     else:
#         print(f"Wtf {dick_size} sm... hADH!")
# else:
#     print("Check your DS, maybe you are lady.")
#
#
# user_name = input("Enter your username!: ")
# if user_name:
#     print(f'Hello {user_name}')
# else:
#     print('Hello stranger')
# idcode = input('Please enter your national id: ')
# if idcode.isdecimal():
#     if len(idcode) != 11:
#         if len(idcode) < 11:
#             print('id you entered is too short')
#         else:
#             print('ID you entered is too long')
#     else:
#         print('ID is correct')
# else:
#     print('Failed')
# username = 'Terminator'
# username and print(f'Hello {username}')

# age = 11
#
# if age <= 10 and age > 0:
#     print("He is a child")
# if age < 18 and age > 10:
#     print("He is a teenager")
# if age >= 18:
#     print('He is adult')
#
# numbers = range(0, 101)
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# odds = []
# evens = []
# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
#     else:
#         odds.append(num)
#
# print(odds)
# print(evens)
#
# names = ['Jack', 'Samantha', 'Bob', 'Simon']
# for n in names:
#     print(f'Hello {n}')
#
people = [
    ['Jack', 34, 'm'],
    ['Samantha', 28, 'f'],
    ['Sarah', 27, 'f'],
    ['Bob', 16, 'm'],
    ['Simon', 42, 'm'],
]
# for person in people:
#     if person[2] == 'm':
#         print(f'This is {person[0]}. He is {person[1]} years old')
#     elif person [2] == 'f':
#         print(f'This is {person[0]}. She is {person[1]} years old')
#
# for name, age, gender in people:
#     if gender == 'm':
#         print(f'This is {name}. He is {age} years old')
#     elif gender == 'f':
#         print(f'This is {name}. She is {age} years old')
#
# range(10) => [0, 2, 3, 4, 5, 6, 7, 8, 9]
# for num1 in range(10): #10
#     for num2 in range(10): #100
#         for num3 in range(10): #1000
#             for num4 in range(10): #10000
#                 for num5 in range(10): #100000
#                     print(num1, num2, num3, num4, num5)
# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1
#
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

