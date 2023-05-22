# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input())
power = 0
a=0
while a<=N:
        a = pow(2,power)
        if a>N:
                break
        else:
            print(a)
            power+=1
