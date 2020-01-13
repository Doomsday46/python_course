import math as m

def quest1():
    print("Quest 1")
    print(firstExpression(1, 1))
    print(secondExpression(1, 0))
    print(thirdExpression(1, 1))

def quest2(x, y, z):
    print("Quest 2")
    print("Old value: ", x, y, z)
    t = x
    x = y
    y = z
    z = t
    print("Value: ", x, y, z)
def firstExpression(x, y):
    numerator = m.sqrt(x - 1)  - m.sqrt(y)
    denominator = 1 + (x ** 2) / 2.0  + (y ** 2) / 4.0
    return numerator / denominator

def secondExpression(x, z):
    return x * (m.tan(z) + m.exp(-(x + 3)))

def thirdExpression(x, y):
    numerator = 3 + m.exp(y - 1)
    denominator = 1 + x ** 2 - 10
    return numerator / denominator



def performLaboratory():
    print("Laboratory 2")
    quest1()
    quest2(0, 1, 2)

