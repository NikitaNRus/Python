a = [1,2,3,9,2]
#b = [1,'abcd', True, [1,2,3],(1,2,3)]
#c = list(map(str,input().split()))
#d = [int(a) for a in input().split()]
l = list('abcdef')
print(l)
poped = a.pop()       #Удаляет элемент по заданному индексу
print(poped)
print(a)

print(a.index(2)) #выводит номер индекса заданного объекта в листе

a.sort(reverse = True) #сортирует список
print(a)

a.remove(9) #Убрать определенное значение
a.append(4) #добавить значение к концу списка

#Бывают изменяемые (list, tuple, множество, словарь...) и неизменяемые (строка, int, float, bool...) переменные
#Можем только создать новую переменную из куска старой
a = 'sdadsads'
b = a[3:]

a= [1,2,3]
b = a
a.append(5)
#b тоже изменится, так как оба ссылаются на один и тот же лист, чтобы избежать изменения, используй copy
a= [1,2,3]
b = a.copy
a.append(5)
print(a==b)

a.insert(0,0) #Вствляем 0 на позицию 0, все остальное сдвигается
print(a)

#Задание множества
setty=set([1,1,1,1,1,2,2,2,3,3,4])
set2={1,1,2,2,3,3,4}
print(set2==setty)