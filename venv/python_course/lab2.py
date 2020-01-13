import math as m

def task1():
    print("task 1")
    print("---- Float -----")
    print(firstExpression(1.25, 1))
    print(secondExpression(4, 1))
    print(thirdExpression(5, 6))

    print("---- Integer -----")
    print(int(firstExpression(1.25, 1)))
    print(int(secondExpression(4, 1)))
    print(int(thirdExpression(5, 6)))

def task2(x, y, z):
    print("task 2")
    print("Old value: ", x, y, z)
    t = x
    x = y
    y = z
    z = t
    print("Value: ", x, y, z)


def firstExpression(x, y):
    numerator = m.sqrt(x - 1) - m.sqrt(y)
    denominator = 1 + (x ** 2) / 2.0 + (y ** 2) / 4.0
    return numerator / denominator


def secondExpression(x, z):
    return x * (m.tan(z) + m.exp(-(x + 3)))


def thirdExpression(x, y):
    numerator = 3 + m.exp(y - 1)
    denominator = 1 + x ** 2 - 10
    return numerator / denominator


def performLaboratory():
    print("Laboratory 2")
    task1()
    task2(0, 1, 2)
