import re


def task1():
    file = open('lab10.1.txt', 'r')
    countLines = 0
    countSymbols = 0
    for line in file.readlines():
        if line.find("EOF") == -1:
            countLines += 1
            countSymbols += len(line.replace(" ", "").replace("\n", "").replace("EOLN", "").replace("EOF", ""))
        else:
            break
    file.seek(0)
    print(countLines, countSymbols)
    file.close()
    return


def task2():
    file1 = open('lab10.2.1.txt', 'r')
    fileText = file1.read().split("\n")
    file1.close()
    file2 = open('lab10.2.2.txt', 'r')
    for index, line in enumerate(file2.readlines()):
        if index < len(fileText) - 1:
            fileText[index] = fileText[index] + " " + line

    file1 = open('lab10.2.1.txt', 'w+')
    for line in fileText:
        file1.write(line)
    file2.close()
    return


def task3(k):
    file1 = open('lab10.3.1.txt', 'r')
    words = file1.read().replace("\n", " ").split(" ")
    file1.close()
    file2 = open('lab10.3.2.txt', 'w+')
    for word in words:
        if len(word) == k:
            file2.write(word + " ")

    return


def task4():
    file1 = open('lab10.4.1.txt', 'r')
    numbers = file1.read().replace("\n", " ").split(" ")
    numbers = list(filter(isValid, numbers))
    return sum(float(number) for number in numbers)


def isValid(number):
    if re.match(r'^-?\d+(?:\.\d+)?$', number) is None or int(number.split(".")[1]) == 0:
        return False
    else:
        return True


def performLaboratory():
    print("Laboratory 10")
    print("task1")
    task1()

    print("task2")
    task2()

    print("task3")
    task3(3)

    print("task4")
    print(task4())
