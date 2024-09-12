# empty = []
# print(empty) #[]

# empty = list()
# print(type(empty)) #list()
# print(bool(empty)) #empty list give false value

# x = 10
# filled = [123, 0.123, 'hello',x , [1, 2, 3, [1, 2, 3],4, 5], True]
# print(len(filled))
# # print(filled[5])

# print(len(filled[4]))

# courses = ['History', 'Math', 'Literature', 'Physics', 'programming', '1231414']

# courses.sort(reverse=True)
# print(courses)

# [Start:End:Step]
# print(course[1])
# print(course[1:4])
# print(course[::-2])
# print(course[0:5:2])

# courses[0] = 'Art'
# print(courses) #['Art', 'Math', 'Literature', 'Physics', 'Programming']

# courses.append('Art') #append element to the end of list
# print(courses[3])
# courses.insert(9999, 'English') #insert element to list
# print(courses)
# courses.extend(['Art', 'Economics']) #extend list
# print(courses)

# courses.remove('Literature')
# print(courses)

# courses.pop(0) #remove last element, or by index
# print(courses)

# courses.reverse() #reverse list
# print(courses)

# ['History', 'Math', 'Literature', 'Physics', 'Programming']
# courses.sort()
# print(courses) #['History', 'Literature', 'Math', 'Physics', 'Programming']

# numbers = [11, 21, 33, 44, 55, 66, 77, 88, 99, 104, 5, 6, 7, 8, 9, 10]
# numbers.sort(reverse=True)
# print(numbers)

# print(min(courses))
# print(max(courses))
# print(min('Hello world')) #space
# print(max('Hello world'))

# print('Math' in courses)
# print('world' in 'Hello world')

# print('hello people of planet earth'.split()) #['hello', 'people', 'of', 'planet', 'earth']

# user_input = input('Enter your name: ') #always return string
# print(user_input.split(', '))
# print('***'.join(courses))

# a = 'one'
# b = a
# a += 'two'
# print(a, b)

# a = [1, 2, 3]
# print(id(a))
# b = a.copy()
# print(id(b))
# a.append(555)
# b.append(666)
# print(a)
# print(b)

# empty = ()
# print(type(empty)) #tuple

# x = (1, )
# print(type(x))

# courses = ('History', 'Math', 'Literature', 'Physics', 'programming', '1231414')
# print(courses[0])
# # courses[0] = 'Art'
# print(courses.count('Math'))
# print(courses.index('Math'))
# courses = list(courses)
# courses.append('Art')
# courses = tuple(courses)
# print(courses)

# print([1, 2, 3] + [3, 2, 1]) #list
# print((1, 2, 3) + (3, 2, 1)) #tuple

# x = {1, 2, 3} #set () delete duplicates, no index
# print(type(x))

# courses = {'History', 'Math', 'Math', 'Literature', 'Physics', 'Programming', '1231414'}
# courses2 = {'Math', 'Economics', 'History', 'Spanish'}
# print(courses.difference(courses2))
# print(courses2.difference(courses))

# print(courses.intersection(courses2))

