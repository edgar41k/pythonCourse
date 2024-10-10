import uuid  # Импорт библиотеки для генерации уникальных идентификаторов
# Разрешенные расширения для загружаемых файлов
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Функция для проверки, разрешен ли файл для загрузки
def allowed_file(filename):
    # Проверка, содержит ли имя файла точку и возвращает True, если расширение разрешено
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Функция для генерации уникального имени файла
def unique_filename(filename):
    # Получение расширения файла
    ext = filename.rsplit('.', 1)[1].lower()  # Извлечение расширения из имени файла
    # Генерация уникального имени с использованием UUID
    unique_name = f'{uuid.uuid4()}.{ext}'  # Создание уникального имени
    return unique_name  # Возврат уникального имени файла
