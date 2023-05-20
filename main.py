#a = 5
#b = 5.89
#c = 'hello'
#print("{}-{}-{}".format(a,b,c))

#print("Введите первое число: ")
#a=int(input())

#b = int(input('Введите второе число: '))

#print(a,"+",b, "=", a+b)


#c = 5.89
#print(c)
#n = int (c)
#print(n)
#print(type(n))


#a = 5.89323
#b = 6.24343
#print(round(a*b,3))

#iter =2 
#iter +=3
#iter *=2


#a = 1!=2
#print(a)

#a = 'qwe'
#b = 'qwe'
#print(a==b)

#username = input ("Введите имя: ")
#if username == 'Маша':
#    print('Ура, это же Маша')
#elif username == 'Марина':
#    print ("Я так ждала Вас, Марина!")
#elif username == "Ильнар":
#    print("Ильнар - топ")
#else:
#    print('Привет, ',username)

#i = 0
#while i <5:
#    if i ==6:
 #       break
  #  i = i+1
#else:
#    print ('пожалуй, хватит')
#print(i)


#n = int(input())
#flag = True
#i = 2
#while flag == True:
#    if n%i ==0:
#        flag = False
#        print (i)
#    elif i > n //2:
#        print(n)
#        flag = False
#    i += 1

#a = 'qwerty'
#for i in a:
#    print(i)


#line = ""
#for i in range(5):
#    line = ""
#    for j in range(5):
#        line +="+"
#    print(line)



text = 'СЪЕШЬ ещё этих мяГких французских булок'
print(len(text))
print ('ещё' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё', 'больше'))

print(text[1])
print(text[-1])
print(text[:])
print(text[2:12])
print(text[0:len(text):2])

text = text[2:9] + text [-5] + text[:3]
print(text)