"""
Name: Joanna Godawa
file: greeting.py

Displays a greeting with a heart and moving arrow.

Certificate of Authenticity:
I certify that this assignment is my own work."""
import time
from graphics import GraphWin, Circle, Polygon, Point, Text, color_rgb

shapes_list = []
text_list = []


def main():
    win = GraphWin("test", 500, 400)
    create_text(win)
    for i in range(25):  # create grid
        win.create_line(0, i * 20, 500, i * 20, fill=color_rgb(255, 219, 239))
        win.create_line(i * 20, 0, i * 20, 500, fill=color_rgb(255, 219, 239))

    # Begin greeting sequence
    create_shapes()
    draw_shapes(shapes_list, win)  # places shapes on window
    fade_in(text_list[0], win, 1)  # Fade in greeting message
    time.sleep(1.0)
    move_arrow(shapes_list[3], shapes_list[4], shapes_list[5])  # move arrow
    fade_in(text_list[1], win, 3)  # display exit prompt
    win.getMouse()


def create_shapes():
    # create heart
    shape1 = Polygon(Point(159, 120), Point(341, 120), Point(250, 260))
    shape1.setFill("deeppink")
    shape1.setOutline(color_rgb(140, 20, 86))

    shape2 = Circle(Point(205, 100), 50)
    shape2.setFill("deeppink")
    shape2.setOutline(color_rgb(140, 20, 86))

    shape3 = Polygon(Point(171, 136), Point(247, 88), Point(329, 132),
                     Point(241, 243))
    shape3.setOutline("deeppink")
    shape3.setFill("deeppink")

    shape4 = Circle(Point(295, 100), 50)
    shape4.setFill("deeppink")
    shape4.setOutline(color_rgb(140, 20, 86))

    shape5 = Polygon(Point(241, 97), Point(340, 120), Point(249, 259))
    shape5.setOutline("deeppink")
    shape5.setFill("deeppink")

    # create arrow
    arrow = Polygon(Point(-6, 251), Point(-30, 257), Point(-30, 265),
                    Point(-225, 435), Point(-219, 442), Point(-25, 272),
                    Point(-15, 273), Point(-6, 251))
    arrow_tip = Polygon(Point(-6, 251), Point(-30, 257), Point(-30, 265),
                        Point(-25, 272), Point(-15, 273), Point(-6, 251))
    arrow_tail = Polygon(Point(-208, 424), Point(-220, 419), Point(-240, 435),
                         Point(-222, 437), Point(-222, 455), Point(-205, 441),
                         Point(-205, 428))
    arrow.setFill(color_rgb(133, 23, 92))
    arrow.setOutline(color_rgb(66, 11, 46))
    arrow_tip.setFill(color_rgb(250, 80, 173))
    arrow_tip.setOutline(color_rgb(196, 47, 129))
    arrow_tail.setFill(color_rgb(235, 28, 69))
    arrow_tail.setOutline(color_rgb(133, 12, 36))

    shapes_list.append(shape1)
    shapes_list.append(shape2)
    shapes_list.append(shape3)
    shapes_list.append(arrow_tail)
    shapes_list.append(arrow)
    shapes_list.append(arrow_tip)
    shapes_list.append(shape4)
    shapes_list.append(shape5)


def create_text(window):
    display_msg = Text(Point(250, 300), "Happy Valentine's Day!")
    display_msg.setFace("courier")
    display_msg.setStyle("bold")
    display_msg.setSize(20)
    display_msg.setTextColor("whitesmoke")
    display_msg.draw(window)  # this has to be here for the fade in to function

    close_msg = Text(Point(250, 330), "(click to close.)")
    close_msg.setFace("courier")
    close_msg.setTextColor("whitesmoke")
    close_msg.draw(window) # this has to be here for the fade in to function

    text_list.append(display_msg)
    text_list.append(close_msg)


def draw_shapes(shape_list, window):
    for i in range(len(shape_list)):
        shape_list[i].draw(window)


def fade_in(text, window, speed):
    time.sleep(0.25 / speed)
    g_val = 245
    b_val = 245
    for _ in range(14):
        text.undraw()
        text.setTextColor(color_rgb(245, g_val, b_val))
        g_val -= 8
        b_val -= 5
        text.draw(window)
        time.sleep(0.1 / speed)


def move_arrow(shape1, shape2, shape3):
    for i in range(39):  # first motion
        shape1.move(9.5, -5.45)
        shape2.move(9.5, -5.45)
        shape3.move(9.5, -5.45)
        time.sleep(.001)

    for i in range(3, 1, -1):  # second motion
        shape1.move(-i, 0)
        shape2.move(-i, 0)
        shape3.move(-i, 0)
        time.sleep(.015)
        shape1.move(i, 0)
        shape2.move(i, 0)
        shape3.move(i, 0)
        time.sleep(.0125)


main()
