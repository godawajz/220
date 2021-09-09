"""
Name: Joanna Godawa
lab2.py
"""

import math


def sum_of_threes():
    sumOfThrees = 0
    upperBound = eval(input("Upper bound: "))

    for i in range(3, upperBound + 1, 3):
        sumOfThrees += i

    print("\nSum of threes =", sumOfThrees)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="  ")
        print("\n")


def triangle_area():
    sideA = eval(input("Side A: "))
    sideB = eval(input("Side B: "))
    sideC = eval(input("Side C: "))

    s = (sideA + sideB + sideC) / 2
    triangleArea = math.sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))

    print("\nArea:", round(triangleArea, 3))


def sumSquares():
    squareSum = 0
    lowerBound = eval(input("Lower bound: "))
    upperBound = eval(input("Upper bound: "))

    for i in range(lowerBound, upperBound + 1):
        squareSum += i ** 2
    print("Sum =", squareSum)


def power():
    base = eval(input("Base value: "))
    exponent = eval(input("exponent value: "))
    powerVal = 1

    for i in range(exponent):
        powerVal *= base

    print()
    print(base, "^", exponent, "=", powerVal)


sum_of_threes()
multiplication_table()
triangle_area()
sumSquares()
power()
