# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
#Также нельзя использовать циклы.



def Sum(a,b):
    if b ==0:
        return a
    if b != 0:
        a+=1
        b-=1
        return Sum(a,b)




print(Sum(int(input('Введите 1 число: ')), int(input('Введите 2 число: '))))