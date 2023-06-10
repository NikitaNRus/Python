# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 

def ToList(N):
    list = []
    for i in range(N):
        list.append(int(input(f'Введите число {i+1}: ')))
    return list

def Bigger (list):
    counter = 0
    i = 1
    while i < len(list)-1:
        if list[i]>list[i-1] and list[i]>list[i+1]:
            counter+=1
        i+=1
    return counter

print('Hello')
list = ToList(5)
print(list)
print(list[-1])
print(Bigger(list))
