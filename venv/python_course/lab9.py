from random import seed
from random import randint
import math as m
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

def quest4(M, S, P):
    maxElement = 0
    for i, row in enumerate(M):
        for j in range(len(M[i])):
            if S <= i and P >= j and i <= j:
                if row[j] > maxElement:
                    maxElement = m.fabs(row[j])
    return maxElement

def quest5(M, N):
    matrix = rotation(M, N)
    return rotation(matrix, N)

def rotation(M, N):
    return [[row[j] for row in M] for j in range(N - 1, -1, -1)]

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

    print("Quest4")
    M = [[randint(1, 10) for i in range(N)] for j in range(N)]
    for row in M:
        print(' '.join([str(i) for i in row]))
    print("Value: ", quest4(M, 2, 3))

    print("Quest5")
    M = [[randint(1, 10) for i in range(N)] for j in range(N)]
    for row in M:
        print(' '.join([str(i) for i in row]))

    print("Quest5 result")
    result = quest5(M, N)
    for row in result:
        print(' '.join([str(i) for i in row]))