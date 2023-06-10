# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

def ToList(N, list):
    for i in range(N):
        list.append(int(input()))
    return list

def Compare(list1,list2):
    container=[]
    for i in range (len(list1)):
        if list1[i] not in list2:
            container.append(list1[i])
                
    return container

N = int(input("Задайте кол-во элементов в первом массиве"))
list1 = []
list1 = ToList(N,list1)

print(list1) 

M = int(input("Задайте кол-во элементов во втором массиве"))
list2 = []
list2 = ToList(M,list2)
print(list2)

print(Compare(list1,list2))