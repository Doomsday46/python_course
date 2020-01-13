import math as m

def quest1(N):
    result = 0
    for i in range(N):
        result += 1.0 / (i + 1)
    return  result

def quest2(N, p, q):
    listNumber = list(range(0, N))
    for i in range(len(listNumber)):
        if m.fabs(listNumber[i] % p) == q:
            listNumber[i] = 0
    return listNumber

def quest3(N):
    sum = 0
    for divider in range(1, N):
        if N % divider == 0:
            sum += divider
    if sum == N:
        print("Совершенное число: ", N)
    else:
        print("Несовершенное число: ", N)


def performLaboratory():
    print("Laboratory 4")
    print("Quest 1")
    print(quest1(4))

    print("Quest 2")
    print(quest2(10, 2, 1))

    print("Quest 3")
    quest3(6)
    quest3(8)
