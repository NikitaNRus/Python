# найти N-ое число Фибоначчи

def Fibo (n):
    if n in [1,2]:
        return 1
    return Fibo(n-1) + Fibo(n-2)

list_1 = []
for i in range(1,11):
    list_1.append(Fibo(i))
print(list_1)

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные 
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.

def CreateList(n):
    list =[]
    for i in range (n):
        list.append(int(input(f"Введите {i} элемент: ")))
    return list
list = CreateList(int(input('Введите кол-во оценок:')))
print(list)

def Reverse (list):
    values = {5:1,4:2}
    for i in range (len(list)):
        if list[i] in values.keys():
            list[i]=values.get(list[i])
    return list

print (Reverse(list))