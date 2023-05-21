# Задача 2: Найдите сумму цифр трехзначного числа.
print('Введите трехзначное число: ')
var = input()

if var.isalpha():
    while var.isalpha():   #isalpha - является буквами
        var = input ('введите ТОЛЬКО трехзначное число')
elif (int(var) // 1000) >= 1:
    var = input ("Введите ТРЕХЗНАЧНОЕ число!")
else:
    var = int(var)
    sum = var//100 + var//10 - var//100*10 + var%10
    print(sum)