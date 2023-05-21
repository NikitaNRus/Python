#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет 
#с номером. Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.

print ('Введите шестизначное число')
ticket = int(input())
ticketOne = ticket//1000
ticketTwo = ticket%1000

ticketOneSum = ticketOne//100 + (ticketOne//10 - ticketOne//100*10) + ticketOne%10
ticketTwoSum = ticketTwo//100 + (ticketTwo//10 - ticketTwo//100*10) + ticketTwo%10

if ticketOneSum== ticketTwoSum:
    print('YES')
else:
    print('NO')