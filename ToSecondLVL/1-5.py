#1 Вводится два числа. В выходной файл записать их сумму.

a = float(input("Первое число: "))
b = float(input("Второе число: "))
sum = str(a+b)
f = open('sum.txt', 'w')
f.write(sum)


#2 Является ли число степенью двойки?
#Вводится число, не большее 2**20. Напечатать YES, если оно является степенью двойки, NO - иначе

import math
n = int(input("Степень ? "))
if math.log(n, 2).is_integer():
    print("YES")
else:
    print("NO")

#3 Посчитать сумму цифр числа
#Вводится число. Вывести сумму его цифр

n = int(input("Число: "))
sum = 0
while (n != 0):
    sum = sum + n % 10
    n = n // 10
print("Сумма: ", sum)

#4 Даны N отрезков прямой. Найти длину общей части всех этих отрезков.
#Входные данные. Вводится сначала число N (1\leq N \leq 100)(1≤N≤100). Далее вводится NN пар чисел, задающих координаты левого и правого концов каждого отрезка. Все координаты - числа из диапазона от 0 до 30000. Левый конец отрезка всегда имеет координату строго меньшую, чем правый.
#Выходные данные. Выведите длину общей части этих отрезов. Если у всех этих отрезков общей части нет, выведите 0.

N = int(input("N: "))
x = int(input("x1: "))
y = int(input("x2: "))
for i in range(N - 1):
    a = int(input("x1: "))
    if a > x: x = a
    b = int(input("x2: "))
    if b < y: y = b

if x >= y:
    print(str(0))
else:
    print(str(y - x))

#5 Во входном файле записана последовательность чисел в странном формате: у каждого числа сначала записано количество цифр в этом числе, а потом через пробел - сами цифры. Последовательность заканчивается числом 0.
#В выходной файл нужно вывести сначала количество чисел в последовательности, а потом - сами числа.
#Количество чисел в последовательности не превышает 1000. В числах - не более 4-х знаков.

f = open('ex4.txt', 'r')
a = f.read()
res = str("")
i = 0
j = 0
count = 0
a = a.replace(" ", "")
while a[i] != '0':
    j = int(a[i])
    while j != 0:
        res += a[i+1]
        i += 1
        j -= 1
    res += ' '
    count += 1
    i +=1
f2 = open('res.txt', 'w')
count = str(count)
f2.write(count + ' ' + res)


