# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

def ToList(N):
    list = []
    for i in range(N):
        list.append(int(input(f'Введите число {i+1}: ')))
    return list

def Pares (list):
    counter = 0
    for i in range(len(list)):
        for j in range (len(list)-i-1):
            if list[i]==list[j+i+1]:
                counter+=1
                break
    return counter

def ParesTrue(list,counter):
    j=0
    while j < len(list)-1:
        if list[0]==list[j+1]:
            list.pop(0)
            list.pop(j+1)
            counter.append(1)
            ParesTrue(list,counter)
        j+=1
    return len(counter)

counter = []
list = ToList(5)
print (list)
print(Pares(list))
print(f'Кол-во пар: {ParesTrue(list,counter)}')