# Для диапозона чисел от 1 до 100 включитель
# Если число делится на 3 без остатка, вывести число и FIZZ
# Если число делится на 5 без остатка, вывести число и BUZZ
# Если число делится на 3 и на 5 без остатка, вывести число и FIZZBUZZ
# Каждое число выводится не больше одного раза

numbers = range(1, 101)
for num in numbers:
    div3 = num % 3
    div5 = num % 5
    if div3 == 0 and div5 == 0:
        print(f'{num}FIZZBUZZ')
    elif div5 == 0:
        print(f'{num}FIZZ')
    elif div3 == 0:
        print(f'{num}BUZZ')
# 3FIZZ
# 5BUZZ
# 6FIZZ
# 9FIZZ
# 10BUZZ
# 12FIZZ
# 15FIZZBUZZ
# 18FIZZ
# 20BUZZ
# 21FIZZ
# 24FIZZ
# 25BUZZ
# 27FIZZ
# 30FIZZBUZZ
# 33FIZZ
# 35BUZZ
# 36FIZZ
# 39FIZZ
# 40BUZZ
# 42FIZZ
# 45FIZZBUZZ
# 48FIZZ
# 50BUZZ
# 51FIZZ
# 54FIZZ
# 55BUZZ
# 57FIZZ
# 60FIZZBUZZ
# 63FIZZ
# 65BUZZ
# 66FIZZ
# 69FIZZ
# 70BUZZ
# 72FIZZ
# 75FIZZBUZZ
# 78FIZZ
# 80BUZZ
# 81FIZZ
# 84FIZZ
# 85BUZZ
# 87FIZZ
# 90FIZZBUZZ
# 93FIZZ
# 95BUZZ
# 96FIZZ
# 99FIZZ
# 100BUZZ