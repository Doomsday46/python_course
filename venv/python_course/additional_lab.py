def spLab():
    while True:
        a = input()
        if a.isdigit():
            task(a)
            a = None
        if a == "exit":
            break


def task(number):
    numberSplit = list(map(int, str(number)))
    stack = []

    for number in numberSplit:
        stack.append(number)

    while len(stack) > 0:
        print(stack.pop(), end="")
