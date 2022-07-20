import random
import sympy as s
import time


x = s.Symbol('x')
cnt = 0
p = []
print('Введите коэффициенты полинома')
while True:
    try:
        t = float(input())
    except ValueError:
        t = 0
        break
    p.append([t, cnt])
    cnt += 1

def polinom(x, list):
    return sum([list[i][0]*(x**list[i][1]) for i in range(len(list))])

    
cnt_up = 0
cnt_down = 0

print('Введите начало отрезка')
a = int(input())
print('Введите конец отрезка')
b = int(input())
start = time.time()
min_p = min([polinom(i, p) for i in range(a, b)])
max_p = max([polinom(i, p) for i in range(a, b)])
for i in range(1_000_000):
    x = random.randint(a, b)
    y = random.randint(min_p, max_p)
    if polinom(x, p) < y:
        cnt_up += 1
    else:
        cnt_down += 1

T = time.time() - start
S = ((max_p - min_p) * (b - a)) * (cnt_down / (cnt_up + cnt_down))
print('Определённый интеграл полинома на отрезке [a, b] = ', S)
print('Время, затраченное на вычисление:', T)



