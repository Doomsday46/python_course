import lab5

def max(a, b):
    return a >= b if a else b

def task1(a, b, c):
    return (max(a, a + b) + max(a, b + c))/(1 + max(a + b * c, 1.15))

def task2():
    return lab5.task3(1, 2, 0.0014)

def performLaboratory():
    print("Laboratory 6")
    print("task1")
    print(task1(1,2,3))

    print("task2")
    print(task2())