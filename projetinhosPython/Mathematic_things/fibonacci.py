import time
from threading import *



start = time.perf_counter()


def fibonacci(u):
    f = [0, 1]
    for i in range(u):
        f.append(plus(f[i], f[i+1]))
    return f


def plus(n1, n2):
    return n1 + n2


n = 16

print(fibonacci(n)[n-1])

finish = time.perf_counter()


print(f'process time: {finish-start}')
