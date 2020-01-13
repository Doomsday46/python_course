import math as m


def task1():
    n = 0
    while expression(n) >= 0:
        n += 1
    return n


def expression(n):
    return -4 * n + (84 / (m.sqrt(n) + 3))


def task2(value):
    reverse = 0
    while value > 0:
        remind = value % 10
        reverse = (reverse * 10) + remind
        value = value // 10
    return reverse


import math as m


def task3(a, x, eps):
    i = 0
    y1 = a
    while True:
        y2 = y1
        y1 = 0.5 * (y2 + x / y2)
        i += 1
        if condition(y1, y2) < eps:
            break
    return i


def condition(y1, y2):
    return m.fabs(y1 ** 2 - y2 ** 2)


def performLaboratory():
    print("Laboratory 5")
    print("task1")
    print(task1())

    print("task2")
    print(task2(123456))

    print("task3")
    print(task3(1, 2, 0.0014))
