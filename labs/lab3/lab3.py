"""
Name: Joanna Godawa
lab3.py

"""


def average():
    totalGrades = 0
    rounds = eval(input("Enter the number of grades: "))

    for i in range(1, rounds+1):
        print("Enter grade for homework", i, end="")
        totalGrades += eval(input(":"))

    print("\nAverage score:", round(totalGrades/rounds, 2), end="")
    print("%")


def tip_jar():
    totalTips = 0

    print("=========== Tip Jar ==========")
    for i in range(5):
        totalTips += eval(input("How much will you be tipping? "))

    print("\nTotal amount:", round(totalTips, 2), "dollars")


def newton():
    x = eval(input("Enter x value: "))
    approxRounds = eval(input("How many times should this answer be improved? "))
    approx = x/2
    for i in range(approxRounds):
        approx = (approx+(x/approx))/2

    print("\nFor number", x, end="")
    print(", approximation =", approx)


def sequence():
    terms = eval(input("Enter the number of terms in this sequence: "))
    for i in range(1, terms + 1):
        output = 1 + (i // 2) * 2
        print(output, end=", ")


def pi():
    n = eval(input("Enter value n: "))
    approx = 1

    for i in range(n):
        numerator = 2 + (i // 2) * 2
        denominator = 1 + ((i + 1) // 2) * 2
        # print(" numerator:", numerator, "denominator:", denominator)
        approx *= numerator / denominator

    print("\nApproximation of pi:", approx * 2)


average()
tip_jar()
newton()
sequence()
pi()
