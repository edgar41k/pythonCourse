import requests

# Функция для получения обменных курсов
def get_exchange_rates(api_key):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'  # Запрос курсов по отношению к USD
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']

# Функция для конвертации валюты
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency != 'USD':
        amount = amount / exchange_rates[from_currency]  # Приводим к USD
    return round(amount * exchange_rates[to_currency], 2)  # Конвертируем в целевую валюту

# Основная логика
if __name__ == '__main__':
    api_key = 'b9b9acf8296c547955bbce25'  # Замените на ваш ключ API
    exchange_rates = get_exchange_rates(api_key)

    # Ввод данных пользователем
    from_currency = input("Введите валюту, которую хотите конвертировать (например, EUR, USD): ")
    to_currency = input("Введите валюту, в которую хотите конвертировать (например, RUB, GBP): ")
    amount = float(input("Введите сумму: "))

    # Конвертация
    result = convert_currency(amount, from_currency, to_currency, exchange_rates)
    
    # Вывод результата
    print(f"{amount} {from_currency} = {result} {to_currency}")
