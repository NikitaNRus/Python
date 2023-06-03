# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

M = int(input('Введите кол-во элементов подмножества М: '))
N = int(input('Введите кол-во элементов подмножества N: '))
m = []
n = []
for i in range(M):
    m.append(int(input(f'Введите число {i} в список M: ')))

for j in range(N):
    n.append(int(input(f'Введите число {j} в список N: ')))

print(f'Множество М: {m} \n Множество N: {n}')

m = set(m)
n = set(n)
j = m.union(n)
print(f'Ваше множество: {j}')