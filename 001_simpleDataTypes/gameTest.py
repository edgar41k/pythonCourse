import random


def guess_the_number():
    # Приветственное сообщение
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадаю число от 1 до 100, а ты попробуй его угадать.")

    # Генерация случайного числа
    secret_number = random.randint(1, 100)

    # Начальное количество попыток
    attempts = 0

    while True:
        # Ввод числа от пользователя
        guess = input("Введи число: ")

        # Проверка, что ввод корректный
        if not guess.isdigit():
            print("Пожалуйста, введи целое число.")
            continue

        # Преобразование ввода в целое число
        guess = int(guess)
        attempts += 1

        # Проверка, угадал ли игрок число
        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
            break


# Запуск игры
guess_the_number()
