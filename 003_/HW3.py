# Print to console what is different in each set compared to another
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# print(set_a.difference(set_b)) #{1, 2}
# print(set_b.difference(set_a)) #{5, 6}
#
# # Create a string from a list and save it to variable
# # Make each name on a new line.
# names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']
# names = '\n'.join(names)
# print(names)
#
# print sum of all numbers in a list
# print sum of all unique numbers in a list
# numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]
# print(sum(numbers)) # 362
# print(set(numbers)) # {2, 12, 32, 53, 65, 87}
# print(sum(set(numbers))) # 251
#
# create a new list from studentsA and studentsB
# make sure there is no duplicates in a new lists
# studentsA = ['Jack', 'Bob', 'Mary']
# studentsB = ['Bob', 'Sarah', 'Simon']
# print(list(set(studentsA).union(set(studentsB))))
#
# What elements are common for both tuples?
# numbersA = (23, 52, 12, 75, 42)
# numbersB = (75, 22, 42, 94, 70)
# print(set(numbersA).intersection(set(numbersB))) # {75, 42}
#
# # add 5 to the tuple on a right position
# a = (1, 2, 3, 4, 6, 7, 8)
# a = list(a)

#VARIANT 1
# a.insert(4, 5)
# a = tuple(a)
# print(a) # (1, 2, 3, 4, 5, 6, 7, 8)

#VARIANT 2
# a.append(5)
# a.sort()
# print(a)




