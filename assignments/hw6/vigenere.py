"""
Name: Joanna Godawa
file: vigenere.py

Takes user input for message and key to be encoded, outputs an encoded message

Certificate of Authenticity:
I certify that this assignment is my own work."""

from graphics import *


def main():
    width = 600
    height = 450
    win = GraphWin("Vigenere", width, height)

    message_text_pt = Point(width/2 - 180, height/2 - 150)
    keyword_text_pt = Point(width / 2 - 175, height / 2 - 100)
    message_text = Text(message_text_pt, "Message to code")
    keyword_text = Text(keyword_text_pt, "Enter keyword")
    message_input = Entry(Point(message_text_pt.getX() + 245, message_text_pt.getY()), 35)
    keyword_input = Entry(Point(keyword_text_pt.getX() + 158, keyword_text_pt.getY()), 17)
    button = Rectangle(Point(width / 2 - 45, height / 2 - 25), Point(width / 2 + 45, height / 2 + 25))
    button_txt = Text(Point(width/2, height/2), "Encode")

    button.draw(win)
    button_txt.draw(win)
    message_text.draw(win)
    keyword_text.draw(win)
    message_input.draw(win)
    keyword_input.draw(win)

    win.getMouse()

    raw_message = message_input.getText()
    raw_keyword = keyword_input.getText()
    encoded_msg = code(raw_message, raw_keyword)

    button.undraw()
    button_txt.undraw()

    results_header = Text(Point(width/2, height/2 + 20), "Resulting Message:")
    results_body = Text(Point(width/2, height/2 + 40), encoded_msg)
    click_to_close = Text(Point(width/2, height - 20), "Click again to close")

    results_header.draw(win)
    results_body.draw(win)
    click_to_close.draw(win)

    win.getMouse()


def code(message, keyword):
    message = message.replace(" ", "").upper()
    keyword = keyword.replace(" ", "").upper()
    acc = ''

    for i in range(len(message)):
        temp = ord(message[i]) - 65
        key = ord(keyword[i % len(keyword)]) - 65
        temp += key
        newChr = chr((temp % 26) + 65)
        acc += newChr

    return acc


if __name__ == "__main__":
    main()
