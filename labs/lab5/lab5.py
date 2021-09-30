"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *
from math import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    inst_pt = Point(win_width / 2, win_height - 20)
    win = GraphWin("Draw a Triangle", win_width, win_height)

    instructions = Text(inst_pt, "Click 3 points to draw a triangle.")
    instructions.draw(win)

    click1 = win.getMouse()
    click2 = win.getMouse()
    click3 = win.getMouse()

    triangle1 = Polygon(click1, click2, click3)
    triangle1.setFill("red")
    triangle1.setOutline("red")
    triangle1.draw(win)

    sideA = sqrt((click2.getX() - click1.getX())**2 + (click2.getY() - click1.getY())**2)
    sideB = sqrt((click3.getX() - click2.getX()) ** 2 + (click3.getY() - click2.getY())**2)
    sideC = sqrt((click1.getX() - click3.getX()) ** 2 + (click1.getY() - click3.getY())**2)

    tri_perimeter = round(sideA + sideB + sideC, 3)
    tri_s = tri_perimeter / 2
    tri_area = round(sqrt(tri_s * (tri_s - sideA) * (tri_s - sideB) * (tri_s - sideC)), 3)


    instructions.undraw()
    instructions = Text(inst_pt, 'Area is equal to ' + str(tri_area) +
                        '\nPerimeter is equal to ' + str(tri_perimeter))
    instructions.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    green_box = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    blue_box = Entry(Point(win_width / 2, win_height / 2 + 100), 5)

    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for _ in range(5):
        win.getMouse()

        red_value = int(red_box.getText())
        green_value = int(green_box.getText())
        blue_value = int(blue_box.getText())

        shape.undraw()
        shape.setFill(color_rgb(red_value, green_value, blue_value))
        shape.draw(win)

    inst.undraw()
    msg = "Click again to close program."
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    stringVal = input("Enter a string: ")
    print("First character:", stringVal[0])
    print("Last character:", stringVal[-1])
    print("Positions 2-5:", stringVal[1:6])
    print("First and last characters:", stringVal[0] + stringVal[-1])
    print("First three characters 10 times:", stringVal[:3] * 10)
    print("Each character one line per time:")
    for i in range(len(stringVal)):
        print(stringVal[i])
    print("number of characters in the string:", len(stringVal))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)

    x = values[0] + values[2]
    print(x)

    x = values[1] * 5
    print(x)

    x = [values[2], values[3], pt]
    print(x)

    x = [values[2], values[3], int(pt.getX())]
    print(x)

    x = [values[2], int(pt.getX()), float(values[5])]
    print(x)

    x = values[2] + int(pt.getX()) + float(values[5])
    print(x)

    x = len(values)
    print(x)


def another_series():
    seriesSum = 0
    value = eval(input("Enter the number of terms in the series: "))
    for i in range(value):
        term = ((i % 3) + 1) * 2
        print(term, end=" ")
        seriesSum += term
    print("sum =", seriesSum)


def main():
    # target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
