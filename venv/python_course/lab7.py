import collections

def quest1(text):
    countLetters = collections.Counter(text.split())
    result = countLetters.most_common(1)
    for letter, count in countLetters.items():
        resultLetter, countResultLetter = result[0]
        if countResultLetter <= count:
            result = [(letter, count)]
    return result[0]

def quest2(text, symbol):
    count = 0
    wordResult = ""
    textSplitted = text.split(" ")
    for index, word in enumerate(textSplitted):
        if word[0] == symbol:
            textSplitted[index] = word[len(word)::-1]
            count += 1
    return count, textSplitted

def performLaboratory():
    print("Laboratory 7")
    print("Quest1")
    letter, count = quest1("aaa bb xxxxx")
    print('Letter: {}'.format(letter), 'Counter: {}'.format(count))

    print("Quest2")
    count, text = quest2("arb ccc vvv bbb","a")
    print(count, text)