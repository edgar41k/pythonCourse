from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import timedelta, datetime
import hashlib
from .utils.helpers import allowed_file, unique_filename # Импорт утилит для работы с файлами
import os



# Инициализация Flask приложения
app = Flask(__name__)
app.secret_key = 'hello'  # Секретный ключ для управления сессиями
app.permanent_session_lifetime = timedelta(minutes=10)  # Установка времени жизни сессии на 10 минут

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/flask_python15'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключение отслеживания изменений

# Конфигурация загрузки файлов
app.config['UPLOAD_FOLDER'] = 'static/upload'  # Папка для сохранения загруженных файлов
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Максимальный размер загружаемого файла (16 МБ)

# Инициализация SQLAlchemy
db = SQLAlchemy(app)

# Модель пользователя для базы данных
class User(db.Model):
    _id = db.Column('user_id', db.Integer, primary_key=True)  # Первичный ключ
    login = db.Column('login', db.String(20), unique=True)  # Уникальное поле для логина
    password = db.Column('password', db.String(32))  # Поле для пароля
    email = db.Column('email', db.String(100))  # Поле для электронной почты
    avatar = db.Column('avatar', db.String(100))  # Поле для аватара пользователя

    def __init__(self, login, password, email='', avatar=''):
        self.login = login
        self.password = password
        self.email = email
        self.avatar = avatar

# Модель поста для базы данных
class Post(db.Model):
    _id = db.Column('post_id', db.Integer, primary_key=True)  # Первичный ключ
    title = db.Column('title', db.String(100))  # Заголовок поста
    content = db.Column('content', db.String(1000))  # Содержимое поста
    date_added = db.Column('date_added', db.DateTime())  # Дата добавления поста
    owner = db.Column('owner', db.String(20))  # Владелец поста

    def __init__(self, title, content, owner):
        self.title = title
        self.content = content
        self.owner = owner
        self.date_added = datetime.now()  # Установка даты добавления на текущее время

# Главный маршрут для отображения всех постов
@app.route('/')
def home():
    posts = Post.query.order_by(desc('date_added')).all()  # Получение постов, отсортированных по дате
    return render_template('index.html', posts=posts)  # Отображение шаблона index с постами

# Маршрут для входа пользователя (аутентификация и регистрация)
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Если запрос POST
        session.permanent = True  # Установить сессию как постоянную
        user_name = request.form['user-name']  # Получение имени пользователя из формы
        user_pass = hashlib.md5(request.form['user-pass'].encode()).hexdigest()  # Хеширование пароля
        user_in_db = User.query.filter_by(login=user_name).first()  # Поиск пользователя в БД по логину

        if user_in_db:  # Если пользователь найден
            if user_pass == user_in_db.password:  # Проверка пароля
                session['login'] = user_name  # Сохранение логина в сессию
                session['email'] = user_in_db.email  # Сохранение электронной почты в сессию
                flash('Logged in successfully.', 'success')  # Успешное сообщение
                return redirect(url_for('user_profile'))  # Перенаправление на профиль пользователя
            else:
                flash('Wrong password.', 'danger')  # Ошибка неверного пароля
                return redirect(url_for('login'))  # Перенаправление на страницу входа
        else:  # Если пользователь не найден
            new_user = User(user_name, user_pass, '')  # Создание нового пользователя
            db.session.add(new_user)  # Добавление нового пользователя в сессию
            db.session.commit()  # Сохранение изменений в БД
            session['login'] = user_name  # Сохранение логина в сессию
            session['email'] = ''  # Очищение электронной почты в сессии
            flash('User account is created.', 'success')  # Успешное сообщение о создании учетной записи
            return redirect(url_for('user_profile'))  # Перенаправление на профиль пользователя
    else:  # Если запрос GET
        if 'login' in session:  # Если пользователь уже в сессии
            flash('You are already logged in.', 'info')  # Сообщение о том, что пользователь уже вошел
            return redirect(url_for('user_profile'))  # Перенаправление на профиль пользователя
        return render_template('login.html')  # Отображение страницы входа

# Маршрут для профиля пользователя
@app.route('/user_profile/', methods=['GET', 'POST'])
def user_profile():
    if 'login' in session:  # Проверка, что пользователь в сессии
        the_user = User.query.filter_by(login=session['login']).first()  # Получение данных пользователя из БД
        if request.method == 'POST':  # Если запрос POST
            user_email = request.form['user-email']  # Получение электронной почты из формы
            user_in_db = User.query.filter_by(login=session['login']).first()  # Поиск пользователя в БД
            user_in_db.email = user_email  # Обновление электронной почты
            db.session.commit()  # Сохранение изменений в БД
            session['email'] = user_email  # Обновление электронной почты в сессии
            flash('Email was saved.', 'success')  # Успешное сообщение
        return render_template('user.html', login=session['login'], email=session['email'], avatar=the_user.avatar)  # Отображение шаблона профиля пользователя
    else:
        flash('Please log in.', 'info')  # Сообщение о необходимости входа
        return redirect(url_for('login'))  # Перенаправление на страницу входа

# Маршрут для создания нового поста
@app.route('/post/', methods=['GET', 'POST'])
def post():
    if 'login' in session:  # Проверка, что пользователь в сессии
        if request.method == 'POST':  # Если запрос POST
            title = request.form['post-title']  # Получение заголовка поста из формы
            content = request.form['post-content']  # Получение содержимого поста из формы
            new_post = Post(title, content, session['login'])  # Создание нового поста
            db.session.add(new_post)  # Добавление нового поста в сессию
            db.session.commit()  # Сохранение изменений в БД
            flash('Post saved', 'success')  # Успешное сообщение
            return redirect(url_for('home'))  # Перенаправление на главную страницу
        else:
            return render_template('post.html')  # Отображение страницы создания поста
    else:
        return redirect(url_for('login'))  # Перенаправление на страницу входа

# Маршрут для загрузки аватара пользователя
@app.route('/upload_avatar/', methods=['GET', 'POST'])
def upload_avatar():
    if 'login' in session:  # Проверка, что пользователь в сессии
        if request.method == 'POST':  # Если запрос POST
            if 'avatar' not in request.files:  # Проверка наличия файла в запросе
                flash('No file selected', 'danger')  # Ошибка отсутствия файла
                return redirect(request.url)  # Перенаправление на текущую страницу

            file = request.files['avatar']  # Получение файла аватара

            if not file.filename:  # Проверка, выбрал ли пользователь файл
                flash('No file selected', 'danger')  # Ошибка отсутствия файла
                return redirect(request.url)  # Перенаправление на текущую страницу

            if file and allowed_file(file.filename):  # Проверка, что файл разрешен для загрузки
                filename = unique_filename(file.filename)  # Генерация уникального имени файла
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Сохранение файла
                the_user = User.query.filter_by(login=session['login']).first()  # Получение пользователя из БД
                the_user.avatar = filename  # Обновление аватара пользователя
                db.session.commit()  # Сохранение изменений в БД
                flash('Avatar uploaded successfully', 'success')  # Успешное сообщение
                return redirect(url_for('user_profile'))  # Перенаправление на профиль пользователя
        return render_template('upload_avatar.html')  # Отображение страницы загрузки аватара
    else:
        return redirect(url_for('login'))  # Перенаправление на страницу входа

# Маршрут для администрирования (редирект на главную страницу)
@app.route('/admin/')
def admin():
    return redirect(url_for('home'))  # Перенаправление на главную страницу

# Маршрут для выхода из системы
@app.route('/logout/')
def logout():
    session.pop('login', None)  # Удаление логина из сессии
    session.pop('email', None)  # Удаление электронной почты из сессии
    flash('Logged out.', 'info')  # Успешное сообщение о выходе
    return redirect(url_for('login'))  # Перенаправление на страницу входа

# Маршрут для удаления пользователя
@app.route('/delete_user/')
def delete_user():
    User.query.filter_by(login=session['login']).delete()  # Удаление пользователя из БД по логину
    db.session.commit()  # Сохранение изменений в БД
    session.pop('login', None)  # Удаление логина из сессии
    session.pop('email', None)  # Удаление электронной почты из сессии
    flash('User was deleted', 'success')  # Успешное сообщение об удалении пользователя
    return redirect(url_for('home'))  # Перенаправление на главную страницу

# Маршрут для удаления поста
@app.route('/delete_post/<post_id>')
def delete_post(post_id):
    post = Post.query.filter_by(_id=post_id).first()  # Получение поста из БД по ID
    if 'login' in session and post.owner == session['login']:  # Проверка, что пользователь в сессии и он владелец поста
        Post.query.filter_by(_id=post_id).delete()  # Удаление поста из БД
        db.session.commit()  # Сохранение изменений в БД
        flash('Post was deleted', 'success')  # Успешное сообщение об удалении поста
    return redirect(url_for('home'))  # Перенаправление на главную страницу

# Запуск приложения
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание всех таблиц в базе данных
    app.run(debug=True)  # Запуск приложения в режиме отладки
