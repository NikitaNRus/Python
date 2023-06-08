#Анонимные и lambda функции

def f(x):
    return x*x
print(f(5))

a = f #a хранит ссылку на фукнцию
print(a(5))


def calc1(a,b):
    return a+b

def calc2(a,b):
    return a*b

def math(op,x,y):
    print(op(x,y))

math(calc1,5,5) #Передали функцию в функцию
math(calc2,5,5)


#lambda function

calc3 = lambda a,b: a+b
math(calc3,45,5)

math (lambda a,b:a*b,5,6)

list1 = [1,2,3,5,8,15,23,38]
res = list()

for i in list1:
    if i%2==0:
        res.append((i,i*i))
print (res)

def select(f,col):
    return [f(x) for x in col]

def where(f,col):
    return[x for x in col if f(x)]
res = select(int,list1)
print(res)

res = where(lambda x: x%2==0, res)
print(res)
res = list(select(lambda x: (x,x**2),res))
print(res)


#функция MAP #позволяет применить функцию к каждому элементу списка

list2 = [x for x in range(1,20)]
print(list2)

list2 = list(map(lambda x: x+10, list2))
print(list2)

list3 = '15 156 96 3 5 8'
print(list3)

list3 = list3.split()
print(list3)

list3 = '15 156 96 3 5 8'
list3 = list(map(int, list3.split())) #превратили строку в список
print(list3)

# функция filter фильтрует значения по указаному правилу

data = [15,65,1,9,8,54,2]
res = list(filter(lambda x: x%10 == 5, data))
print(res)

# функция zip 

users = ['user1','user2','user3','user4']
ids = [4,5,9,13]
salary = [123,456,123,654,43342]
data = list(zip(users,ids,salary))
print(data)

#функция enumerate применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных

users = ['user1','user2','user3','user4']
data = list(enumerate(users))
print(data)

#файлы
# a - открытие для добавления данных, r - открытие для чтения, w - открытие для записи данных
# w+ открыть файл для записи и читать из него, если файла не существует, он будет создан
# r+ позволяет открывать файл для чтения и дописывать в него, если файла не существует, то программа выдаст ошибку

colors = ['red', 'green' , 'blue'] 
data = open('file.txt','a', encoding ='utf-8') #добавляет к существующему
data.writelines(colors)
data.close()

with open('file.txt','w') as data: #перезаписал все, что было в файле
    data.write('line1 \n')
    data.write('line2 \n')
print(56)

path = 'file.txt'
data = open(path,'r')
for line in data:
    print(line)
data.close()

#модуль os
import os
#os.chdir(path) #- смена текущей директории 
os.getcwd() #-текущая рабочая директория
os.path.basename(path) #базовое имя пути
os.path.abspath(path) #возвращает нормализованный абсолютный путь

#модуль shutil
import shutil
shutil.copyfile(scr,dst) #копирует содержимое файла scr в файл dst
shutil.copy(scr,dst) #копирует содержимое файла scr в файл или папку dst
#shutil.rmtree(path) #удаляет текущую директорию и все поддиректории



