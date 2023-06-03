#Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
#Количество повторов добавляется к символам с помощью постфикса формата _n.


#str = 'a b c a a a b b c a c'.split()
#list = {}
#r =""
#for i in range (len(str)):
#    if str[i] not in list.keys():
#        list[str[i]]=1
#        r+=f'{str[i]} '
#    else:
#        r += f'{str[i]}_{list[str[i]]} '
#        list[str[i]] +=1
#print(r)

#for i, letter in enumerate((str)):
#    if str[:i].count(letter)<1:
#        r+=letter+" "
#    else:
#        r+=f'{letter}_{str[:i].count(letter)}'


#Пользователь вводит текст(строка). 
#Словом считается последовательность непробельных символов идущих подряд, 
#слова разделены одним или большим числом пробелов. 
#Определите, сколько различных слов содержится в этом тексте.

#str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".split()
#mn = set()
#for i in range(len(str)):
#    mn.add(str[i].strip('.,!?\n').lower())
#print(mn)
#print(len(mn))

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
#“Задана последовательность неотрицательных целых чисел. 
#Требуется определить значение наибольшего элемента последовательности, 
#которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
#Однако 2  друга оказались не такими смышлеными. 
#Никто из ребят не смог до конца сделать это задание. 
#Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
#За помощью товарищи обратились к Вам, студентам.

n = int(input())
max_number = n
while n!= 0:
    if n>max_number and n !=0:
        max_number=n
    n = int(input())
print(max_number)
