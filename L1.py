list_1 = []
list_1 = list()
print(list_1)
list_1=[1,2,3,4,8]
print(list_1)

for i in list_1:
    print (i)

print(len(list_1))
print(list_1[3])

list_1.append(19)
print(list_1)

for i in range(5):
    list_1.append(i)
    print(list_1)

print(list_1.pop()) #pop удаляет последний элемент и показывает его
print(list_1)

print(list_1.pop(1)) #pop удаляет конкретный элемент с индексом i и показывает его
print(list_1)

print(list_1.insert(2,11)) #insert(i,j) вставляет элемент j в i индекс
print(list_1)

print(list_1[3:7])

#кортежи - неизменяемый список
t = ()
print(type(t))
t =(1, ) #в конце обязательно запятую
print(type(t))

v = [1,8,9]
print(type(v))

v = tuple(v)
print(v)
print(type(v))

#a,b = 1,2 # равно a=1, b=2
a,b,c = v #распаковска кортежа
print(a,b,c)

t = (1,2,3,5)
print(t[1])

#t[0]=2 невозможно реализовать, так как элементы кортежа не перезаписываются

#словари

d ={}
d = dict()
d['q'] = 'qwerty'
print(d)

d['w']='qwerty'
print(d['q'])

dictionary = {}
dictionary = {'up':'|','left':'<-','down':'|','right':'->'}
print(dictionary)
print(dictionary['left'])
dictionary[895]=434332
print(dictionary)

del dictionary[895] #удаляет ключ

for item in dictionary:
    print(item)
    print('{}:{}'.format(item,dictionary[item]))

for (k,v) in dictionary.items():
    print(k,v)

print(dictionary.items())

#Множества - набор уникальных элементов, не обязательно упорядоченные

colors = {'red', 'green', 'blue'}
print(colors)
colors.add('red') # не добавится, так как уже есть во множестве
print(colors)
colors.add('grey')
print(colors)

colors.discard('red')
print(colors)
colors.clear()
print(colors)

q = set()

#операции со множествами в python
a = {1,2,3,4,8}
b ={2,4,5,12}
c = a.copy()
u = a.union(b) #Объединение множеств
i = a.intersection(b)
d1 = a.difference(b)
dr = b.difference(a)
q = a.union(b).difference(a.intersection(b))

a = {1,8,6}
b = frozenset(a)
print(b)

list_1 = [i for i in range (1,5)]
print(list_1)
list_1 = [i for i in range(1,5) if i%2==0]
print(list_1)

list_1 = [(i,i) for i in range (1,10) if i%2==0]
print(list_1)

list_1=[i*2 for i in range(1,5) if i%2==0]
print(list_1)