import lab5

def max(a, b):
    return a >= b if a else b

def quest1(a, b, c):
    return (max(a, a + b) + max(a, b + c))/(1 + max(a + b * c, 1.15))

def quest2():
    return lab5.quest3(1, 2, 0.0014)

def performLaboratory():
    print("Laboratory 6")
    print("Quest1")
    print(quest1(1,2,3))

    print("Quest2")
    print(quest2())