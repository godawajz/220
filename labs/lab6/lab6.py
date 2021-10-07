"""
Name: Joanna Godawa
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    rawInput = input("Enter a first and last name: ")
    dividedName = rawInput.split(" ")
    output = dividedName[1] + ', ' + dividedName[0]
    print(output)


def company_name():
    rawInput = input("Enter a three-part internet domain name: ")
    dividedInput = rawInput.split(".")
    print(dividedInput[1])


def initials():
    students = eval(input("How many names will be input? "))

    for i in range(1, students + 1):
        prompt = 'Enter the first name of student ' + str(i) + ': '
        firstName = input(prompt)
        prompt = 'Enter ' + firstName + '\'s last name: '
        lastName = input(prompt)
        outputInitials = firstName[:1] + lastName[:1]
        output = firstName + '\'s initials are ' + outputInitials
        print(output + "\n")


def names():
    rawInput = input("Enter a list of names, separated by commas: ")
    nameList = rawInput.split(", ")
    initialsList = []

    for i in range(len(nameList)):
        firstAndLast = nameList[i].split(" ")
        initials = firstAndLast[0][:1] + firstAndLast[1][:1]
        initialsList.append(initials)

    print("The initials are", end=" ")
    for i in range(len(initialsList)):
        if i < len(initialsList) - 1:
            print(initialsList[i], end=", ")
        else:
            print(initialsList[i], end=".")


def thirds():
    sentences = eval(input("How many sentences will you input? "))

    for _ in range(sentences):
        sentence = input("Enter a sentence: ")
        print(sentence[2: len(sentence): 3])


def word_average():
    sentence = input("Enter a sentence: ")
    wordList = sentence.split(" ")
    wordSum = 0
    for i in range(len(wordList)):
        wordSum += len(wordList[i])
    average = wordSum / len(wordList)
    print("Average:", average)


def pig_latin():
    rawSentence = input("Enter a sentence: ").lower()
    wordList = rawSentence.split(" ")
    pigLatinOutput = ''
    for i in range(len(wordList)):
        temp = wordList[i][1:] + wordList[i][0:1] + 'ay '
        pigLatinOutput += temp
    print(pigLatinOutput)


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
    # add other function calls here


main()
