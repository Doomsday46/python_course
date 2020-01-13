from random import seed
from random import randint
import math as m
def task1(N):
    return [[abs(i - j) for j in range(N)] for i in range(N)]

def task2(n, m):
    return [['{:>4}'.format(i + 1 + m * j) for i in range(m)][::pow(-1, j)] for j in range(n)]

def task3(N, x):
    count = 0
    for row in N:
        if float(sum(row))/len(row) > x:
            count += 1
    return count

def task4(M, S, P):
    maxElement = 0
    for i, row in enumerate(M):
        for j in range(len(M[i])):
            if S <= i <= j <= P:
                if row[j] > maxElement:
                    maxElement = m.fabs(row[j])
    return maxElement

def task5(M, N):
    return rotation(M, N)

def rotation(M, N):
    return [[M[N - 1 - row][N - 1 - column] for column in range(N)] for row in range(N)]

def performLaboratory():
    print("Laboratory 9")
    print("task1")
    for row in task1(5):
        print(' '.join([str(i) for i in row]))

    print("task2")
    for row in task2(4, 4):
        print(' '.join([str(i) for i in row]))

    print("task3")
    seed(1)
    N = 5
    M = [[randint(0, 10) for i in range(N)] for j in range(N)]
    for row in M:
        print(' '.join([str(i) for i in row]))
    print(task3(M, 4))

    print("task4")
    M = [[randint(1, 10) for i in range(N)] for j in range(N)]
    for row in M:
        print(' '.join([str(i) for i in row]))
    print("Value: ", task4(M, 2, 3))

    print("task5")
    M = [[randint(1, 10) for i in range(N)] for j in range(N)]
    for row in M:
        print(' '.join([str(i) for i in row]))

    print("task5 result")
    result = task5(M, N)
    for row in result:
        print(' '.join([str(i) for i in row]))