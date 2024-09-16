import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
hall, ball, wall, tall
'''

# sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'[1-9-z]+')

# pattern = re.compile(r'\w')

# pattern = re.compile(r'\b\d{3}[-.]\d{3}[-.]\d{3,4}\b')

# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

