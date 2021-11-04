"""
Name: Joanna Godawa
file: bumper.py

Circle bumper car simulation

Certificate of Authenticity:
I certify that this assignment is my own work."""
import time
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb


def main():

    height = randint(200, 350)
    width = height + randint(0, 175)
    win = GraphWin("Bumper", width, height)
    win.setBackground(get_random_color())

    circ1 = Circle(Point(randint(30, width // 2 - 30),
                         randint(30, height - 30)), 25)
    circ1_color = get_random_color()
    circ1.setFill(circ1_color)
    circ1.draw(win)

    circ2 = Circle(Point(randint(width // 2 + 30, width - 30),
                         randint(30, height - 30)), 25)
    circ2_color = get_random_color()
    circ2.setFill(circ2_color)
    circ2.draw(win)

    circ1_x = get_random(2)
    circ1_y = get_random(2)
    circ2_x = get_random(2)
    circ2_y = get_random(2)

    while win.isOpen():
        if did_collide(circ1, circ2):
            circ1_y, circ2_y = circ2_y, circ1_y
            circ1_x, circ2_x = circ2_x, circ1_x
            circ1.move(circ1_x, circ1_y)
            circ2.move(circ2_x, circ2_y)
            time.sleep(0.002)
            circ1.move(circ1_x, circ1_y)
            circ2.move(circ2_x, circ2_y)
            time.sleep(0.002)
        if hit_horizontal(circ1, win):
            circ1_y *= -1
        if hit_vertical(circ1, win):
            circ1_x *= -1
        if hit_horizontal(circ2, win):
            circ2_y *= -1
        if hit_vertical(circ2, win):
            circ2_x *= -1
        circ1.move(circ1_x, circ1_y)
        circ2.move(circ2_x, circ2_y)
        time.sleep(0.002)


def get_random_color():
    red_val = randint(0, 255)
    green_val = randint(0, 255)
    blue_val = randint(0, 255)

    return color_rgb(red_val, green_val, blue_val)


def get_random(move_amount):
    num = randint(-move_amount, move_amount)
    return num


def did_collide(circ1, circ2):
    collision = False
    point_1 = circ1.getCenter()
    point_2 = circ2.getCenter()
    diameter = 2 * (circ1.getRadius())
    distance = ((point_2.getX() - point_1.getX()) ** 2 +
                (point_2.getY() - point_1.getY()) ** 2) ** (1/2)
    if distance - diameter <= -diameter / 8:
        collision = True
    return collision


def hit_horizontal(circ1, win):
    collision = False
    point_1 = (circ1.getCenter()).getY()
    win_height = win.getHeight()
    radius = circ1.getRadius()
    if point_1 - radius <= 0 or point_1 + radius >= win_height:
        collision = True
    return collision


def hit_vertical(circ1, win):
    collision = False
    point_1 = (circ1.getCenter()).getX()
    win_width = win.getWidth()
    radius = circ1.getRadius()
    if point_1 - radius <= 0 or point_1 + radius >= win_width:
        collision = True
    return collision


if __name__ == "__main__":
    main()
