import requests
# from requests.exceptions import HTTPError
# 200 - success
# 300 - redirect
# 400 - client error
# 500 - server error

# r = requests.get('https://xkcd.com/353/', timeout=20)
# r = requests.get('https://imgs.xkcd.com/comics/python.png', timeout=20)

# print(r.text)
# print(r.content)
# print(r.ok)
# print(r.status_code)
# print(r.headers)

# try:    
#     response = requests.get('http://api.github.com/invalid', timeout=20)
#     response.raise_for_status()
# except HTTPError as err:
#     print(f'HTTP error: {err}')
# else:
#     print(f'Success')


from bs4 import BeautifulSoup as BS

url = 'http://gammatest.net/ru/kurs_python_105_php'
response = requests.get(url, timeout=20)

soup = BS(response.content, 'html.parser')
# match = soup.find('div', class_='navbar', role='navigation')
# print(match.find())

# match = soup.find_all('a')
# print(match)
# for m in match:
    # print(m['href'])
    # print(m.get_attribute_list('href'))

# match = soup.find('td', string='16. Регулярные выражения')
# row = match.find_previous_sibling()
# print(row)

response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response.content)
result = response.json()
for post in result:
    print(post['body'])
    print(post['title'])
    print('*' * 20)