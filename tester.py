import re

text_to_search = """
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
"""

urls = """
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
"""

pattern = re.compile(r'(https?://)?(www\.)?([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+)')

matches = pattern.finditer(urls)
for match in matches:
    print(match.group())
# https://www.google.com
# http://www.wordpress.org
# https://www.nasa.gov
# https://example.net
# www.example.net
# example.net