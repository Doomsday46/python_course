from random import seed
from random import randint

def quest1(N):
    return [[abs(i - j) for j in range(N)] for i in range(N)]

def quest2(n, m):
    return [['{:>4}'.format(i + 1 + m * j) for i in range(m)][::pow(-1, j)] for j in range(n)]

def quest3(N, x):
    count = 0
    for row in N:
        if float(sum(row))/len(row) > x:
            count += 1
    return count


def performLaboratory():
    print("Laboratory 9")
    print("Quest1")
    for row in quest1(5):
        print(' '.join([str(i) for i in row]))

    print("Quest2")
    for row in quest2(4, 4):
        print(' '.join([str(i) for i in row]))

    print("Quest3")
    seed(1)
    N = 5
    M = [[randint(0, 10) for i in range(N)] for j in range(N)]
    for row in M:
        print(' '.join([str(i) for i in row]))
    print(quest3(M, 4))