string_sample1 = 'Hello World'
string_sample2 = 'first leTteR is lOwERCaSe'
string_sample3 = '     extra witespaces         '
german_sample = 'der fLUß'

# [START:END:STEP]

# print(string_sample1[-1])  # 0123456789..-5-4-3-2-1..
# print(len(string_sample1)) # 'Hello World' has 11 characters
# print(string_sample1[5:])
# print(string_sample1[:5])
# print(string_sample1[0:11:2]) #HloWrd SAME
# print(string_sample1[::2]) #HloWrd SAME
# print(string_sample1[::-1]) #dlroW olleH
# print(string_sample1[-10:-1]) #ello Worl
# print(string_sample1.upper()) #HELLO WORLD
# print(string_sample1.lower()) #hello world
#
# print(german_sample.lower()) #der fluß
# print(german_sample.casefold()) #der fluss
# print('hello' == 'HELLO') #False
# print('001' > '0000') #True

# print(string_sample2.capitalize()) #First letter is lowercase
# print(string_sample2.title()) #First Letter Is Uppercase
# print(string_sample3.strip()) #Remove extra whitespaces (left and right)
# print(string_sample1.replace('World', 'Universe', 1))

# print(string_sample1.count('World', 8, 12))
# print(str.count("hello", 'l'))

# print(string_sample1.find('World'))
# print(string_sample1[6:])

# print('hello' .center(20, '*'))

# salary = 1000
# string = 'Johns salary is {1}, {0}, {1}, {0}.' Johns salary is USD., 1000, USD., 1000.
# print(string.format(salary, 'USD.'))

# string = 'This {product} costs {price:.2f}$.'
# print(string.format(product='computer', price=1000))

# name= "Jack"
# surname = "Smith"
# salary = 1500

# print(f'This is {name.title()} {surname.title()}. His salary is {salary:.2f}$.')

# byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'

# print(len("Thats\"s"))
# print("My favorite book is \"Python\"")
# print('\tHello\nWorld')