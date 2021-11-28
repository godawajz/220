"""
Name: Joanna Godawa
button.py

Random 3 door guessing game

Certificate of authenticity:
I certify that this assignment is my own work."""
from random import randint
from graphics import GraphWin, Text, Point, Rectangle, color_rgb


class Button:
    """
    Creates button object which can be clicked and modified.
    """
    def __init__(self, shape, label):
        x_coord = (shape.p1.getX() + shape.p2.getX()) / 2
        y_coord = (shape.p1.getY() + shape.p2.getY()) / 2
        self.text = Text(Point(x_coord, y_coord), label)
        self.shape = shape

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        return (self.shape.p1.getX() <= point.getX() <= self.shape.p2.getX()) \
               and (self.shape.p1.getY() <= point.getY() <= self.shape.p2.getY())

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)

    def set_font(self, face):
        self.text.setFace(face)


def game_start(win):
    # coords of the center of the screen
    height = win.getHeight() / 2
    width = win.getWidth() / 2

    header = Text(Point(width, height - 75), "I have a secret door")
    header.draw(win)
    footer = Text(Point(width, height + 150), "click to choose a door.")
    footer.setSize(10)
    footer.setFill("grey")
    footer.draw(win)

    door_1_shape = Rectangle(Point(width - 200, height), Point(width - 100, height + 65))
    door_2_shape = Rectangle(Point(width - 50, height), Point(width + 50, height + 65))
    door_3_shape = Rectangle(Point(width + 100, height), Point(width + 200, height + 65))

    doors = [Button(door_1_shape, "Door 1"), Button(door_2_shape, "Door 2"),
             Button(door_3_shape, "Door 3")]
    for button in doors:
        button.draw(win)
    correct_door_index = randint(0, 2)
    correct_door = doors[correct_door_index]
    other_doors = []
    for button in doors:
        if button != correct_door:
            other_doors.append(button)

    while win.isOpen():
        button_click = False
        click = win.getMouse()
        if correct_door.is_clicked(click):
            button_click = True
            correct_door.color_button(color_rgb(109, 214, 88))
            win_message(header, footer, win)
        elif other_doors[0].is_clicked(click):
            button_click = True
            other_doors[0].color_button(color_rgb(245, 86, 91))
            correct_door.color_button(color_rgb(109, 214, 88))
            lose_message(header, footer, correct_door_index, win)
        elif other_doors[1].is_clicked(click):
            button_click = True
            other_doors[1].color_button(color_rgb(245, 86, 91))
            correct_door.color_button(color_rgb(109, 214, 88))
            lose_message(header, footer, correct_door_index, win)
        if button_click:
            break


def win_message(header, footer, win):
    header.undraw()
    footer.undraw()
    header.setText("You win!")
    footer.setText("click to close.")
    header.draw(win)
    footer.draw(win)


def lose_message(header, footer, correct_door_index, win):
    header.undraw()
    footer.undraw()
    header.setText("You lose!")
    footer.setText("The correct door is door " + str(correct_door_index + 1)
                   + ".\nclick to close.")
    header.draw(win)
    footer.draw(win)


def main():
    win = GraphWin("Three Door Game", 500, 350)
    game_start(win)
    win.getMouse()


if __name__ == "__main__":
    main()
