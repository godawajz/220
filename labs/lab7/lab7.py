"""
Name: Joanna Godawa
lab7.py
"""

import math

def cash_conversion():
    rawInput = eval(input("Enter an integer value: "))
    print("Output: $", end="")
    print('{0:.2f}'.format(rawInput))


def encode():
    s = input("Enter a message to be encoded: ")
    key = eval(input("Enter a key value: "))
    acc = ""

    for i in range(len(s)):
        temp = ord(s[i]) + key
        newChar = chr(temp)
        acc += newChar
    print(acc)


def sphere_area(radius):
    return (radius ** 2) * 4 * math.pi


def sphere_volume(radius):
    return (radius ** 3) * (4 / 3) * math.pi


def sum_n(n):
    total = 0
    for i in range(n):
        total += i
    return total


def sum_n_cubes(n):
    total = 0
    for i in range(n):
        total += (n ** 3)
    return total


def encode_better():
    s = input("Enter a string to be encoded: ")
    key = input("Enter a key: ")
    acc = ""

    for i in range(len(s)):
        temp = ord(s[i])
        k = ord(key[i % len(key)]) - 97
        temp += k
        newChr = chr(temp)
        acc += newChr
    print(acc)

def main():
    cash_conversion()
    encode()

    area = sphere_area(5)
    print("\nSphere area of r = 5:", area)
    volume = sphere_volume(5)
    print("Sphere volume of r = 5:", volume, "\n")

    sum10 = sum_n(10)
    print("Sum of first 10 natural numbers:", sum10)
    sumCubes5 = sum_n_cubes(5)
    print("Sum of the cubes of the first 5 natural numbers:", sumCubes5, "\n")

    encode_better()
    pass


main()
