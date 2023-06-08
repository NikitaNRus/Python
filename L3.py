def SumNumbers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1,n+1):
        summa +=i
    return summa

print(SumNumbers(5))

def sum_str(*args): #неограниченное кол-во переменных c помощью * или словарь **
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('h','e','y'))

from module import *

print(max1(5,9))

def Fibo (n):
    if n in [1,2]:
        return 1
    return Fibo(n-1) + Fibo(n-2)

list_1 = []
for i in range(1,11):
    list_1.append(Fibo(i))
print(list_1)


#Быстрая сортировка
def quick_sort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14,5,9,3,434,23,132,12,32,43]))

#Сортировка слиянием

def merge_sort(nums):
    if len(nums)>1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j <len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i +=1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k]=left[i]
            i+=1
            k +=1
        while j < len(right):
            nums[k]=right[j]
            j+=1
            k +=1

list1 = [1,5,43,233,34,12,23]

merge_sort(list1)
print(list1)