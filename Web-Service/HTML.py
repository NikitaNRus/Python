#file = open('file.txt', 'r',encoding='utf-8')

#list_1=list()
#resultData = list()
#for line in file.readlines():  
#    resultData.append(tuple(line.split('\n')[0].split(';')))
#file.close()

#print(resultData)

#ПИТОН ФАЙЛ
#import random 
#from flask import Flask, render_template 
#app = Flask(__name__)
#@app.route('/')
#def main():
#    with open('file.txt', 'r',encoding='utf-8') as file:
#        resultData = list()
#        for line in file.readlines():
#            resultData.append(tuple(line.split('\n')[0].split(';')))
#   
#    return render_template('base.html', data = resultData)
#@app.route('/about')
#def about():
#    return render_template('about.html')
#if __name__=='__main__':
#    app.run()

#HTML ФАЙЛ
#<!DOCTYPE html>
#<html>
#{% block content %}
#<head>
#    <meta charset="UTF-8">
#    <title>Главная страница</title>
#</head>
#<style>
#    html{
#        background-color:honeydew;
#    }
#</style>
#
#<body>
#    {% if data %}
#    <table> 
#        <tr><th>Имя</th><th>Фамилия</th><th>Дата рождения</th></tr>
#        {% for row in data %}
#            <tr><td>{{row[0]}}</td> <td>{{row[1]}}</td> <td>{{row[2]}}</td> <br> </tr>
#        {% endfor %}
#    </table>
#    {% endif %}
#<h3><a href="/about">О нас</a></h3>
#{% endblock %}
#</body>
#</html>





'''
a - режим добавления 
w - режим на запись (очищает файл)
r - режим на считывание

'''
import random 
from flask import Flask, render_template 
from LoginForm import Lf
from AuthForm import AuthF

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nikita1999'

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/register', methods = ['GET', 'POST'])
def reg():
    form = Lf()
    if form.validate_on_submit():
        if form.password_again.data != form.password.data:
            return render_template('register.html', title = 'Регистрация', form = form, message = 'Пароли не совпадают')
        
        with open('file.txt', 'a', encoding='utf-8' ) as file:
            file.write(f'{form.name.data};{form.email.data};{form.password.data}\n')
        return render_template('register.html', message = 'Регистрация прошла успешно')
    
    return render_template('register.html', title = 'Регистрация', form = form)

@app.route('/log',methods = ['GET', 'POST'])
def log():
    form = AuthF()
    if form.validate_on_submit():
        with open('file.txt','r',encoding='utf-8') as file:
            data = ' '.join(file.readlines())
        if form.email.data not in data:
            return render_template('login.html', form=form, message = 'Вы не зарегестрированы')
        else:
            for i in data.split():
                if form.email.data in i:
                    if i.split(';')[-1] == form.password.data:
                        return render_template('login.html', form=form, message = 'Вы успешно авторизовались')
    return render_template('login.html', form=form)


if __name__=='__main__':
    app.run()