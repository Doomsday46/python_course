import math as m

def quest1(A):
    countElementForAQuest = len(list(filter(isEvenNumberDividers, A)))
    minNumber = min(filter(isValidElement, A))
    return countElementForAQuest, minNumber

def isEvenNumberDividers(number):
    sumDividers = 0
    for i in range(1, number + 1):
        if number % i == 0:
            sumDividers += i
    return sumDividers % 2 == 0

def isValidElement(number):
    return "2" in str(number) and "0" not in str(number)

def quest2(A):
    firstPositiveNumber = firstIndexPositiveNumber(A)
    lastNegativeNumber =  (len(A) - 1) - lastIndexNegativeNumber(A)
    begin = firstPositiveNumber  if firstPositiveNumber < lastNegativeNumber else lastNegativeNumber
    end = firstPositiveNumber if  firstPositiveNumber > lastNegativeNumber else lastNegativeNumber
    subArray = A[begin + 1:end]
    subArray = sorted(subArray)
    A[begin + 1: end] = subArray
    return A

def sorted(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and array[j] > item_to_insert:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item_to_insert
    return array

def firstIndexPositiveNumber(A):
   return next(x for x, val in enumerate(A) if val >= 0)

def lastIndexNegativeNumber(A):
   return next(x for x, val in enumerate(reversed(A)) if val < 0)

def performLaboratory():
    print("Laboratory 8")
    print("Quest1")
    a, b = quest1(range(1000,2000))
    print("A: {}".format(a), "B: {}".format(b))

    print("Quest2")
    array = [0, 9, -1, 2, 4, -4, -9, 2, 5, 9]
    print(array)
    print(quest2(array))

