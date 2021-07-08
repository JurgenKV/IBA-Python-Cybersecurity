import math

# 1

print(pow(2, 179))

# 2

print(math.sqrt(pow(179, 2) + pow(971, 2)))

# 3

a3 = float(input("a: "))
b3 = float(input("b: "))
c3 = math.sqrt(pow(a3, 2) + pow(b3, 2))
print(c3)

# 4

a4 = int(input("a: "))
b4 = int(input("b: "))
c4 = int(input("c: "))
if ((a4 + b4) > c4) & ((b4 + c4) > a4) & ((a4 + c4) > b4):
    print("YESSSSSSSS")
else:
    print("No =(")

# 5

num5 = pow(179,10)
str5 = str(num5) + str(num5) + str(num5) + str(num5)
print(str5)
ans5 = int(str5)
print(pow(ans5,.10))

# 6

i = 0
sum = 0
count6 = int(input("Count: " ))
while i <= count6:
    sum+=pow(i,2)
    i+=1
print(sum)

# 7

n7 = int(input("N:" ))
k7 = int(input("K:" ))
if (n7-k7) >= 0:
    C7 = (math.factorial(n7))/(math.factorial(k7)*math.factorial(n7-k7))
    print(C7)
else:
    print("factorial() not defined for negative values")

# 8

penguine8 = "    _~_    \n   (o o)   \n  /  V  \\ \n /(  _  )\\ \n   ^^ ^^   \n"

n8 = int(input("Num of Linux "))
if n8 >= 1 & n8 <= 9:
    i = 0
    while i != n8:
        print(penguine8)
        i+=1
else:
    print("Error")

#9

n9 = str(input("n: " ))
ans9 = int(n9) + int((n9 + n9)) + int((n9 + n9 + n9))
print(ans9)

#10

sec10 = int(input('sec: '))
min10 = sec10//60
h10 = min10//60
days10 = h10//24
print("Д/Ч/М/С")
print(str(days10)+':'+str(h10)+':'+str(min10)+':'+str(sec10))

#11

print(math.factorial(20))

#12

a12 = float(input('A: '))
b12 = float(input('B: '))

if a12 > b12:
    print(a12)
elif a12 == b12:
    print("Числа равны")
else:
    print(b12)

#13

a13 = float(input('A: '))
b13 = float(input('B: '))

if a13 > b13:
    print('1')
elif a13 == b13:
    print("0")
else:
    print('2')

#14

num14 = "179"
i = 0
string14 = ""
while i < 50:
    string14+=num14
    i+=1
print(pow(int(string14), 2))

#15

year15 = int(input())
if (year15 % 4 == 0) and (year15 % 100 != 0) or (year15 % 400 == 0):
    print('YESSSSSSSSSSSS')
else:
    print('NO')

#16

first16 = str(input('1 Клетка : '))
sec16 = str(input('2 Клетка: '))

if (first16[0] == sec16[0]) | (first16[1] == sec16[1]):
    print("Может")
else:
    print("Нельзя =/")


#17

f17 = str(input('1 Клетка : '))
s17 = str(input('2 Клетка: '))

xFirst17 = int(ord(f17[0])) - int(ord('0'))
xFirst17 = chr(xFirst17)
yFirst17 = f17[1]

xSec17 = int(ord(s17[0])) - int(ord('0'))
xSec17 = chr(xSec17)
ySec17 = s17[1]

dx17 = abs(int(xFirst17) - int(xSec17))
dy17 = abs(int(yFirst17) - int(ySec17))

if dx17 == 1 and dy17 == 2 or dx17 == 2 and dy17 == 1:
    print('Может')
else:
    print('Нет')

# 18

str18 = ""
i18 = 0
while i18 < 100:
    str18+='A'
    i18+=1
print(str18)
























