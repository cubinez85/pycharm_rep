from flask import Flask # импортируем главный класс Flask из модуля flask

app = Flask(__name__) #создаём объект приложения app как экземпляр класса Flask с именем текущего скрипта __name__

admin_login = 'cubinez85'
admin_password = 'admin123'
users_list = []
auth_status = False

@app.route('/greeting') # добавляем декоратор, который выводит приветствие при переходе по определённому адресу на сайте ('/greeting'), то есть передаём этот маршрут декоратору route() как аргумент
def greeting(): # создаём метод greeting, который будет возвращать строку с приветствием (этот метод мы рассматривали ранее, он уже готов)
	return "<h1> Привет, " + admin_login + "! </h1>"

app.run(debug = True) # добавляем строку запуска приложения с помощью метода run