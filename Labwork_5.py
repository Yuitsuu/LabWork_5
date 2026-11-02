#        1

def table():
    N = int(input())
    for i in range(1, 11):
        print(i, "x", N, "=", i * N)
table()

#         2

def table():
    x=0
    while x <= 10:
        if x != 5:
            y = (x-3)/(x-5)
            print(x,"|", y)
        x=x+0.5
table()

#         3

def f():
    Z=int(input())
    s=0
    for i in range(Z-1):
        s=s+int(input())
    print(Z*(Z+1)//2-s)
f()

#         4

def f():
    A=int(input())
    B=int(input())
    if A>B:
        A,B=B,A
    while True:
        print('Введите число')
        n=int(input())
        if A<=n<=B:
            print('Число коректно')
            break
f()

#         5

import random
def f():
    A = int(input())
    B = int(input())
    s = random.randint(A, B)
    n = 0
    while n != s:
        n = int(input())
        if n > s:
            print("Перелёт")
        elif n < s:
            print("Недолёт")
    print("Число угадано")
f()

#         6

def f():
    D = int(input())
    min_temp = 100
    c = 0
    for i in range(D):
        t = int(input())
        if t < min_temp:
            min_temp = t
            c = 1
        elif t == min_temp:
            c+= 1
    print(c)
f()

#         7

def C(A, B):
    while A!=B:
        if A>B:
            A=A-B
        else:
            B=B-A
    return A

def R(A, B):
    if A == B:
        return A
    if A>B:
        return R(A - B, B)
    return R(A, B - A)

def f():
    A = int(input())
    B = int(input())
    print("Цикл:", C(A, B))
    print("Рекурсия:", R(A, B))
f()

#         8

def fac_F(n):
    c = 1
    for i in range(1, n + 1):
        c =c* i
    return c

def fac_W(n):
    c = 1
    i = 1
    while i <= n:
        c=c* i
        i =i+1
    return c

def fac_R(n):
    if n <= 1:
        return 1
    return n * fac_R(n - 1)

def fac():
    N = int(input())
    print(fac_F(N))
    print(fac_W(N))
    print(fac_R(N))

fac()

#         9

def C(x, eps):
    y1 = 1
    while True:
        y = 0.5 * (y1 + x / y1)
        if abs(y - y1) < eps:
            return y
        y1 = y

def R(x, eps, y1=1):
    y = 0.5 * (y1 + x / y1)
    if abs(y - y1) < eps:
        return y
    return R(x, eps, y)

def f():
    x = float(input())
    eps = float(input())
    print("Цикл:", C(x, eps))
    print("Рекурсия:", R(x, eps))
f()

#         10

def f():
    N = int(input())
    c = 64
    while c >= 1:
        if N >= c:
            count = N //c
            print(f"{c} — {count}")
            N = N % c
        c = c // 2
f()
