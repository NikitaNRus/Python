# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

start = int(input("Начало: "))
end = int (input('Конец: '))
list = [1,2,3,67,34,23,54,87,4,23,14,2,34,1,8,90,19,16,21]

def IndexInRange(start,end,list):
    index = []
    for i in range (len(list)):
        if list[i]<=end and list[i]>=start:
            index.append(i)
    return index

print(IndexInRange(start,end,list))