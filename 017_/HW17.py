from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_google_exchange(from_currency, to_currency, amount):
    # Инициализируем драйвер и открываем страницу Google Exchange
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = f"https://www.google.com/search?q={amount}+{from_currency}+to+{to_currency}"
    driver.get(url)

    # Принять файлы cookie (если необходимо)
    try:
        # Ожидание загрузки кнопки принятия файлов cookie и клик по ней
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='L2AGLb']"))
        )
        cookie_button.click()
    except Exception as e:
        print("Кнопка принятия файлов cookie не найдена или уже была нажата.")

    return driver

def get_conversion_result(driver):
    # Ожидание результата
    result_selector = "#knowledge-currency__updatable-data-column > div.ePzRBb > div > div.MWvIVe.egcvbb > input"
    try:
        result_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, result_selector))
        )
        return result_element.get_attribute('value')  # Получаем значение из input
    except Exception as e:
        print(f"Ошибка при получении результата конвертации: {e}")
        return None

if __name__ == '__main__':
    # Запрашиваем данные у пользователя
    from_currency = input("Введите валюту, которую хотите конвертировать (например, EUR): ").strip().upper()
    to_currency = input("Введите валюту, в которую хотите конвертировать (например, USD): ").strip().upper()
    amount = float(input("Введите сумму: "))

    driver = open_google_exchange(from_currency, to_currency, amount)

    try:
        # Получаем результат конвертации
        converted_amount = get_conversion_result(driver)
        
        if converted_amount is not None:
            print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
        else:
            print("Не удалось получить результат конвертации.")
    finally:
        # Закрываем драйвер
        driver.quit()
