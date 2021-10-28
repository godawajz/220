"""
Name: Joanna Godawa
lab9.py
"""
from graphics import *
import math


def addTen(nums):
    for i in range(len(nums)):
        nums[i] += 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    inName = input("Enter name of input file: ")
    inFile = open(inName, "r")
    outFile = open("sumOfSquares.txt", "w+")

    for line in inFile:
        line = line.strip("\n")
        nums = line.split(" ")
        toNumbers(nums)
        squareEach(nums)
        total = sumList(nums)
        outFile.write("Sum =" + str(total) + "\n")

    inFile.close()
    outFile.close()


def starter():
    weight = eval(input("Enter player's weight: "))
    wins = eval(input("Enter number of player's wins: "))

    if 150 <= weight < 160 and wins >= 5:
        print("Player is eligible.")
    elif weight > 199 or wins > 20:
        print("Player is eligible.")
    else:
        print("Player is not eligible.")


def leapYear(year):
    isLeapYear = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        isLeapYear = True
    return isLeapYear


def circleOverlap():
    win = GraphWin("Circle", 400, 400)

    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    shape = Circle(p1, radius1)
    shape.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    shape = Circle(p3, radius2)
    shape.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p3.getY()) ** 2)
    outMsg = ""

    if distance <= (radius1 + radius2):
        outMsg = "Circles overlap"
    else:
        outMsg = "Circles do not overlap"

    overlapTxt = Text(Point(200, 350), outMsg)
    overlapTxt.draw(win)

    win.getMouse()



def main():
    x = [5, 2, -3]
    addTen(x)
    print(x)

    circleOverlap()
    starter()

    writeSumOfSquares()

    isLeapYear = leapYear(2000)
    print("2000 is ", end="")
    if isLeapYear:
        print("a leap year")
    else:
        print("not a leap year.")

    isLeapYear = leapYear(2100)
    print("2100 is ", end="")
    if isLeapYear:
        print("a leap year")
    else:
        print("not a leap year.")
    pass

main()
