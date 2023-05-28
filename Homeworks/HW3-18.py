# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

list=[]

N = int(input('Введите положительное целое число: '))
for i in range (N):
    list.append(int(input(f'Введите число под номером {i+1}: ')))
X = int(input('Введите число, ближайшее по величине число которого будем искать: '))

diff = abs(X-list[0])
num = list[0]
for i in range (len(list)):
    if abs(X-list[i])==diff:
        num=[num]
        num.append(list[i])
    if abs(X-list[i])<diff:
        diff = abs(X-list[i])
        num=list[i]

if type(num) is list:
    print(print(f'Ближайшие числа от {X} равны {num}'))
else:
    print(f'Ближайшее число от {X} равно {num}')