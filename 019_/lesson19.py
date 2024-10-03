import pandas as pd

df = pd.read_csv('019_/2019.csv')
# df = pd.read_csv('019_/2019.csv', nrows=5) #Читает первые 5 строк
# df = pd.read_csv('019_/test.csv', header=None, names=['Name', 'Date of birth', 'City']) #Меняет названия столбцов
# pd.set_option('display.max_columns', 9) #Максимальное количество столбцов
# pd.set_option('display.max_rows', 9) #Максимальное количество строк

# print(df.head(10)) #Показывает первые 10 строк
# print(df.tail(10)) #Показывает последние 10 строк
# df2 = df.head(10) #Сохраняет первые 10 строк в новую переменную

# df.to_csv('019_/new.csv', index=False, header=None) #Перезаписывает файл
# df.to_csv('019_/new.csv', index_label='ID') #Перезаписывает файл с новым названием
# df.to_csv('019_/new.csv', columns=['Name', 'Date of birth']) #Перезаписывает файл с новыми столбцами (в данном случае только Name и Date of birth)

# print(df.columns)
# print(type(df.columns))

#конвертация данных в DataFrame
# df = pd.DataFrame(people)
# print(df)

#выбор и вывод данных
# print(df['Country or region']) 
# print(type(df['Country or region']))

#цикл по столбцам
# for country in df['Country or region']:
    # print(country)

# print(df['Country or region'][45:55]) #выводит страны по индексам с 45 по 55
# print(df[['Country or region', 'Score']]) #выводит страны и счет 
# print(df[1:50]) #выводит страны с 1 по 50 где последний индекс не включается

# print(df.iloc[54]) #выводит страну с индексом 54
# print(df.iloc[45:55]) #выводит страны с индексом 45 по 55
# print(df.iloc[[45, 46, 47, 48]]) #выводит страны с индексом 45, 46, 47, 48
# print(df.iloc[54, 1]) #выводит страну с индексом 54 и столбец с индексом 1
# print(df.iloc[50:55, 1]) #выводит страны с индексом 50 по 55 и столбец с индексом 1
# print(df.iloc[54:55, 1:2]) #выводит страну с индексом 54 по 55 и столбец с индексом 1 по 2

# print(df.loc[54, 'Country or region']) #выводит страну с индексом 54 и столбец с индексом Country or region
# print(df.loc[50:55, ['Country or region', 'Social support']]) #выводит страны с индексом 50 по 55 и столбец с индексом Country or region и Social support 

# print(df.shape) #выводит количество строк и столбцов в DataFrame
# print(df['Country or region'].value_counts()) #считает количество стран, выводит их в порядке убывания


# import mysql.connector

# conn = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     port=3306,
#     password='##########',
#     database='sakila'
# )


# df = pd.read_sql_query('SELECT * FROM actor', conn)
# print(df)


# for index, row in df.iterrows(): #перебор по строкам
    # print(index, type(row)) #выводит индекс и тип каждой строки

# print(df.loc[df['Country or region'] == 'Estonia']) #выводит страну с названием Estonia
# print(df.loc[df['Score'] > 9]) #выводит страны с счетом больше 9

# print(df.describe()) #выводит статистику
#count - количество строк
#mean - среднее
#std - стандартное отклонение
#min - минимальное значение
#25% - 25-й перцентиль
#50% - 50-й перцентиль
#75% - 75-й перцентиль
#max - максимальное значение

# print(df.dtypes)
#выводит типы данных где строка - object, 
#целое число - int64, 
#дробное число - float64
#булевое значение - bool

# print(df.memory_usage(deep=True)) #выводит общую память DataFrame в байтах

# print(df.sort_values('Country or region')) #сортировка по странам в алфавитном порядке
# print(df.sort_values('Country or region', ascending=False)) #сортировка по странам в обратном алфавитном порядке
# print(df.sort_values(['Country or region', 'Perceptions of corruption'], ascending=[False, True]))

# df['Total'] = df['Perceptions of corruption'] * 2 + df['Score'] #добавляет столбец Total
# df.insert(loc=3, column='New', value=(df['Score'] ** 2)) #добавляет столбец New со значением Score в квадрате
# df = df.drop(columns=['New']) #удаляет столбец New
# print(df)

# print(df.groupby('Country or region').count().sort_values('Score', ascending=True)) #группировка по странам, считает количество стран и сортировка по счету.
# print(df.groupby('Country or region').min()['Social support']) #группировка по странам, выводит минимальное значение Social support
# print(df.loc[df['Country or region'].str.contains('on')]) #выводит страны, содержащие в названии слово "on"
# print(df.loc[df['Country or region'].str.endswith('land')]) #выводит страны, оканчивающиеся на "land"
# print(df.loc[df['Country or region'].str.startswith('E')]) #выводит страны, начинающиеся на букву "E"

# print(df.nlargest(10, 'GDP per capita')) #выводит 10 стран с наибольшим значением GDP per capita
# print(df.nsmallest(10, 'GDP per capita')) #выводит 10 стран с наименьшим значением GDP per capita

# print(df.isna().sum()) #считает количество пропущенных значений в каждом столбце

# print(pd.concat([df.nlargest(10, 'GDP per capita'), df.nsmallest(10, 'GDP per capita').reset_index(drop=True)]))

# df.to_excel('output.xlsx', index=False) #сохраняет DataFrame в Excel


