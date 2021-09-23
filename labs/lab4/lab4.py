"""
Name: Joanna Godawa
lab4.py
"""

from graphics import *
import math

width = 400
height = 400
inst_pt = Point(width / 2, height - 10)


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    instructions = Text(inst_pt, "Click to draw another square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("lab 4: rectangles", width, height)
    instructions = Text(inst_pt, "Click 2 points to draw a rectangle.")
    instructions.draw(win)

    corner1 = win.getMouse()
    corner2 = win.getMouse()

    rect = Rectangle(corner1, corner2)

    rect.setOutline("red")
    rect.setFill("red")
    rect.draw(win)

    rect_length = abs(corner2.getY() - corner1.getY())
    rect_width = abs(corner2.getX() - corner1.getX())
    rect_area = rect_length * rect_width
    rect_perimeter = (2 * rect_length) + (2 * rect_width)

    instructions.undraw()

    results = Text(Point(200, 50), "Area is equal to " + str(rect_area) + " px.")
    results.draw(win)
    results = Text(Point(200, 75), "Perimeter is equal to " + str(rect_perimeter) + " px.")
    results.draw(win)
    instructions.undraw()
    instructions = Text(inst_pt, "click again to exit.")
    instructions.draw(win)

    win.getMouse()
    win.close()

    pass


def circle():
    win = GraphWin("lab 4: rectangles", width, height)
    instructions = Text(inst_pt, "Click 2 points to draw a circle.")
    instructions.draw(win)

    centerCirc = win.getMouse()
    radiusCirc = win.getMouse()
    c1 = centerCirc.getX()
    c2 = centerCirc.getY()
    r1 = radiusCirc.getX()
    r2 = radiusCirc.getY()

    distance = math.sqrt(((r1-c1)**2) + ((r2 - c2) ** 2))

    circ = Circle(centerCirc, distance)
    circ.setFill("red")
    circ.setOutline("red")
    circ.draw(win)

    distance = round(distance, 3)
    results = Text(Point(200, 50), "Radius is equal to " + str(distance) + " px.")
    results.draw(win)
    instructions.undraw()
    instructions = Text(inst_pt, "click again to exit.")
    instructions.draw(win)

    win.getMouse()
    win.close()


def pi2():
    n = eval(input("Enter value for n: "))
    acc = 0
    for i in range(n):
        numerator = 4 * math.pow(-1, i)
        denominator = 1 + (2 * i)

        acc += (numerator / denominator)
    print("approximation =", round(acc, 5))
    print("pi - approximation  = ", round(math.pi - acc, 5))


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
