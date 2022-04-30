from random import random
import time
import multiprocessing as mp
import sympy as sym
from functools import partial


def randomfloat(a, b):
    return random() * (b - a) + a


def integral(a, b, n, p):
    s = 0
    for _ in range(n):
        s += partial(p, randomfloat(a, b))
    return ((b - a) / n) * s



if __name__ == '__main__':
    x = sym.Symbol('x')
    p = 0
    cnt = 0
    print('Введите коэффициенты полинома')
    while True:
        try:
            t = float(input())
        except ValueError:
            t = 0
            break
        p += t*x**cnt
        cnt += 1



    a = float(input('Введите начало отрезка:'))
    b = float(input('Введите конец отрезка:'))
    with mp.Pool(processes=mp.cpu_count()) as pool:
        print('Ищем определённый интеграл полинома на данном отрезке')
        N = 100000
        M = 1000
        print('подсчёт с помощью multiprocessing')
        def mf(_):
            return integral(a, b, N * M, p)
        t0 = time.time()
        mp_integral_val = sum(pool.map(mf, [N] * M)) / M
        print(f'{mp_integral_val}-посчитано за {time.time() - t0}  секунд')
        print('подсчёт без помощи multiprocessing')
        t0 = time.time()
        integral_val = integral(a, b, N * M, p)
        print(f'{integral_val} - посчитано за {time.time() - t0} секунд')
        print('подсчёт с помощью библиотеки SymPy')
        t0 = time.time()
        integral_sym = sym.integrate(p, x)
        print(f'{integral_sym}-посчитано за {time.time() - t0}  секунд')