#        1

#N=int(input())
#for i in range(1,11):
#    print(i, "x", N,"=", i*N)

#         2

#x=0
#while x <=10:
#    if x !=5:
#        print(x,":", (x-3)/(x-5))
#    x +=0.5

#         3

#Z = int(input())
#s=0
#for i in range(Z-1):
#    s+= int(input())
#print(Z*(Z+1)//2-s)

#         4

#print('Введите диапазон A и B:')
#A=int(input())
#B=int(input())

#while True:
#    print('Введите число')
#    C= int(input())
#    if A<=C<=B:
#        print('Число корректное')
#        break

#         5

#import random

#A=int(input())
#B=int(input())
#s=random.randint(A,B)

#while True:
#    n=int(input())
#    if n>s:
#        print("Перелёт")
#    elif n<s:
#        print("Недолёт")
#    else:
#        print("Число угадано")
#        break

#         6

#N=int(input())
#temperat=100
#c=0

#for i in range(N):
#    t=int(input())
#    if t<temperat:
#        temperat=t
#        c=1
#    elif t==temperat:
#        c+=1
#print(c)

#         7

#A = int(input())
#B = int(input())

#while A != B:
#    if A > B:
#        A = A - B
#    else:
#        B = B - A
#print(A)

#         8

#N = int(input())

#f = 1
#for i in range(1, N + 1):
#    f = f * i
#print(f)
#f = 1
#i = 1
#while i <= N:
#    f = f * i
#    i = i + 1
#print(f)
#def fact(n):
#    if n <= 1:
#        return 1
#    return n * fact(n - 1)
#print(fact(N))

#         9

#x = float(input())
#eps = float(input())

#y = 1
#while True:
#    y2 = 0.5 * (y + x / y)
#    if abs(y2 - y) < eps:
#        break
#    y = y2
#print(y2)

#         10

N = int(input())

for i in [64, 32, 16, 8, 4, 2, 1]:
    if N >= i:
        print(i, "—", N // i)
        N = N % i
