import pandas as pd

# Загрузка данных
data = pd.read_csv('017_pandas/csv_files/survey_results_public.csv')

# Функции для обработки каждого запроса
def hobbyist_info():
    hobbyist_counts = data['Hobbyist'].value_counts()
    print(f"Профессиональные программисты: {hobbyist_counts.get('No', 0)}")
    print(f"Хобби-программисты: {hobbyist_counts.get('Yes', 0)}")

def age_info():
    print(f"Средний возраст: {data['Age'].mean():.2f}")
    print(f"Максимальный возраст: {data['Age'].max()}")
    print(f"Минимальный возраст: {data['Age'].min()}")

def country_info():
    print(data['Country'].value_counts())

def currency_info():
    print(data['CurrencyDesc'].value_counts().sort_index())

# Меню для выбора действия
def menu():
    actions = {
        '1': hobbyist_info,
        '2': age_info,
        '3': country_info,
        '4': currency_info
    }

    choice = input("Выберите действие (1: Профессионалы/хобби, 2: Возраст, 3: Страны, 4: Валюты): ")
    action = actions.get(choice)

    if action:
        action()
    else:
        print("Неверный выбор, попробуйте снова.")

# Вызов меню
menu()
