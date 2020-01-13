import math as m

def quest1():
    n = 0
    while expression(n) >= 0:
        n += 1
    return n

def expression(n):
    return -4 * n + (84 / (m.sqrt(n) + 3))

def quest2(value):
    reverse = 0
    while (value > 0):
        remind = value % 10
        reverse = (reverse * 10) + remind
        value = value // 10
    return reverse

import math as m

def quest3(a, x, eps):
    i = 0
    y1 = a
    while True:
        y2 = y1
        y1 = 0.5 * (y2 + x/y2)
        i += 1
        if condition(y1, y2) < eps:
            break
    return i

def condition(y1, y2):
    return m.fabs(y1 ** 2 - y2 ** 2)

def performLaboratory():
    print("Laboratory 5")
    print("Quest1")
    print(quest1())

    print("Quest2")
    print(quest2(123456))

    print("Quest3")
    print(quest3(1, 2, 0.0014))