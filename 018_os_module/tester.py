import os
import time

#CURRENT WORKING DIRECTORY
# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())  # Печатает текущую рабочую директорию
# print(os.listdir())  # Печатает все файлы и папки в текущей директории
# os.mkdir('new_folder/one/two') #создает последовательно вложенные папки и все папки до последней уже существуют
# os.makedirs(r'new_folder/one/two/three') #создает папки, если они не существуют
# time.sleep(6)
# os.rmdir(r'new_folder/one/two') #удаляет всегда последнюю директорию пути
# os.remove(r'new_folder/one/two/three')
# os.removedirs(r'new_folder/one/two/three/muysic.mp3') #удаляет все директории пути
# os.rename('texter.txt', 'sample.txt') #так же используют для перебрасывания файлов
# print(os.stat('001_simpleDataTypes').st_size)

# info = os.walk(os.getcwd())

# for dirpath, dirnames, filenames in info:
#     print('*' * 20)
#     print('Current path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)

# print(os.environ.get('database_password')) ##change to your passqord

# print(os.environ.get('HOMEPATH') + r'\text.py')
# print(os.path.join(os.environ.get('HOMEPATH'), 'text.py'))
# print(os.path.join('C:/home', "text.py"))

print(os.path.basename('/somedir/dir2/text')) #получает последний элемент пути
print(os.path.dirname('/somedir/dir2/text')) #получает предпоследний элемент пути
print(os.path.split('/somedir/dir2/text')) #оба пути отправленные в кортеж ()
print(os.path.splitext('/somedir/dir2/text.png')) #разбивает путь на имя и расширение

print(os.path.exists('/somedir/dir2/text.png')) #проверяет существует ли путь (возвращает булевое значение) проверяет и дирикторию и файл
print(os.path.isfile('/somedir/dir2/text.png')) #проверяет является ли путь файлом 
print(os.path.isdir('/somedir/dir2/text.png')) #проверяет является ли путь директорией

