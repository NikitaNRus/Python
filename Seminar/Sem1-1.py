#Ввод-вывод данных
#var = input('Введите свое имя ')
#print ("Привет, ", var) #f-строка или динамическая строка, которую можно подставлять в output
#print(1,2,3, sep = '-', end = ',')
#\n и \t
#print ('the end')


#var = input()
#if var.isalpha():
#    while var.isalpha():   #isalpha - является буквами
#        var = input ('введите только число')
#print(var)


# Задание IF
#a = int (input('Введите число: '))
#if a%2==0:
#    print('Четное')
#lif a%3==0:
#    print('Число делится на 3')
#else:
#    print('Нечетное')

#Задание 1 
#За день машина проехжает n километров, сколько нужно дней, чтобы проехать m километров
#n = int(input("Сколько км проезжает машина в день: "))
#m = int(input("Сколько км надо проехать: "))
#days = m//n+(((m/n)%1)>0)

#print('Дней необходимо потратить: ',days)


# Задание 2
# В некоторой школе решили набрать три новых
#математических класса и оборудовать кабинеты для
#них новыми партами. За каждой партой может сидеть
#два учащихся. Известно количество учащихся в
#каждом из трех классов. Выведите наименьшее
#число парт, которое нужно приобрести для них.

#var1 = float(input('Введите кол-во учеников в 1 классе: '))
#var2 = float(input('Введите кол-во учеников во 2 классе: '))
#var3 = float(input('Введите кол-во учеников в 3 классе: '))

#if var1 % 2==0:
#    sum1 = var1/2
#else: sum1 = var1//2+1
#if var2 % 2==0:
#    sum2 = var2/2
#else: sum2 = var2//2+1
#if var3 % 2==0:
#    sum3 = var3/2
#else: sum3 = var3//2+1
#
#sum = sum1+sum2+sum3
#print('Кол-во необходимых парт:', sum)

#Задача 2
# Дано натуральное число. Требуется определить,
#является ли год с данным номером високосным. Если
#год является високосным, то выведите YES, иначе
#выведите NO. Напомним, что в соответствии с
#григорианским календарем, год является
#високосным, если его номер кратен 4, но не кратен
#100, а также если он кратен 400.

var = int(input())
if var%4==0 and var%100!=0:
    print('YES')
elif var%400==0:
    print('YES')
else:
    print('NO')






