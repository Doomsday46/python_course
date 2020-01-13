import math as m

def firstExpression(x, b):
    return 5 * b * m.cos(x) ** 2


def secondExpression(a, x):
    return (1.0 / 8) * (a * x)


def thirdExpression(x):
    return (x - 1) ** 2 + 6


def fourthExpression(x):
    return 3 * m.tan(x)


def task1(a, b, x):
    if x < 1:
        print(firstExpression(x, b))
    elif x == 1:
        print(secondExpression(a, x))
    elif 1 < x < 2:
        print(thirdExpression(x))
    elif x > 2:
        print(fourthExpression(x))


def task2(a, b, c, x, y):
    print("Value: ", a, b, c, x, y)
    t = ((a <= x) and (b <= y)) or ((a <= x) and (c <= y)) or ((b <= x) and (c <= y)) or ((a <= y) and (b <= x)) or (
                (a <= y) and (c <= x)) or ((b <= y) and (c <= x))
    if t:
        print('Пройдет!')
    else:
        print('Не пройдет!')


def performLaboratory():
    print("Laboratory 3")
    print("task 1")
    task1(1, 1, 0)
    task1(1, 1, 1)
    task1(1, 1, 1.5)
    task1(1, 1, 3)

    print("task 2")
    task2(1, 1, 2, 2, 2)
    task2(3, 3, 2, 2, 2)
