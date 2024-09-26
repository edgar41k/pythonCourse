from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Загрузка страницы
driver.get('https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/')

# Ожидание загрузки таблицы
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#nav-tabContent > div > div.ajx-outer-container > div > div.float-thead-table-container > table'))
)

# Находим таблицу
table = driver.find_element(By.CSS_SELECTOR, '#nav-tabContent > div > div.ajx-outer-container > div > div.float-thead-table-container > table')

# Извлекаем заголовки таблицы
header_row = driver.find_element(By.CSS_SELECTOR, 'thead tr')
headers = [header.text for header in header_row.find_elements(By.TAG_NAME, 'th')]

# Извлекаем строки таблицы
rows = table.find_elements(By.CSS_SELECTOR, 'tr')

# Подготовка списка для хранения данных
data = []

# Извлечение данных из каждой строки
for row in rows[1:]:  # Пропускаем заголовок
    cells = row.find_elements(By.TAG_NAME, 'td')
    
    if len(cells) > 0:  # Проверяем, есть ли данные в строке
        # Инициализируем словарь для хранения данных
        row_data = {}
        
        # Извлекаем название станции
        row_data["Jaam"] = cells[0].text if cells[0].text.strip() != '' else 'None'
        
        # Извлекаем данные по температуре
        row_data["Õhutemperatuur keskmine (°C)"] = cells[1].text if cells[1].text.strip() != '' else 'None'
        row_data["Õhutemperatuur max (°C)"] = cells[2].text if cells[2].text.strip() != '' else 'None'
        row_data["Õhutemperatuur min (°C)"] = cells[3].text if cells[3].text.strip() != '' else 'None'
        
        # Извлекаем остальные данные
        row_data["Maapinna minimaalne temperatuur (°C)"] = cells[4].text if cells[4].text.strip() != '' else 'None'
        row_data["Minimaalne temperatuur 2cm kõrgusel maapinnast (°C)"] = cells[5].text if cells[5].text.strip() != '' else 'None'
        
        # Обработка относительной влажности
        row_data["Suhteline õhuniiskus keskmine (%)"] = cells[6].text if cells[6].text.strip() != '' else 'None'
        row_data["Suhteline õhuniiskus min (%)"] = cells[7].text if cells[7].text.strip() != '' else 'None'
        
        # Обработка скорости ветра
        row_data["Tuule kiirus keskmine (m/s)"] = cells[8].text if cells[8].text.strip() != '' else 'None'
        row_data["Tuule kiirus max (m/s)"] = cells[9].text if cells[9].text.strip() != '' else 'None'
        
        # Остальные данные
        row_data["Sademed (mm)"] = cells[10].text if cells[10].text.strip() != '' else 'None'
        row_data["Päikesepaiste kestus (h)"] = cells[11].text if cells[11].text.strip() != '' else 'None'
        
        # Добавляем данные в общий список
        data.append(row_data)

# Преобразование в JSON
json_data = json.dumps(data, indent=4, ensure_ascii=False)

# Вывод JSON данных
print(json_data)

# Сохранение JSON в файл
with open('weather_data.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

# Закрытие драйвера
driver.quit()
