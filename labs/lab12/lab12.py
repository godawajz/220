"""
Name: Joanna Godawa
lab12.py
"""
from random import randint


def find_and_remove(lst, val):
    try:
        lst[lst.index(val)] = "Joanna"
    except:
        pass


def read_data(f_name):
    f_in = open(f_name, "r")
    out_list = []
    in_list = f_in.readlines()
    i = 0
    while i < len(in_list):
        temp = in_list[i].strip("\n")
        out_list.append(int(temp))
        i += 1
    return out_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        i += 1
    return False


def good_input():
    valid_guess = False
    while not valid_guess:
        guess = eval(input("Enter a number from 1-10: "))
        if 1 <= guess <= 10:
            return guess
        if guess < 1:
            print("Error: this guess is too low!")
        if guess > 10:
            print("Error: this guess is too high!")


def num_digits():
    num = 1
    while num != 0:
        num = eval(input("Enter a positive integer (0 to exit): "))
        temp = num
        digits = 0
        while temp != 0:
            temp = temp // 10
            digits += 1
        print("The number ", num, " has ", digits, " digits.")


def hi_lo_game():
    correct_number = 50
    guesses = 0
    is_running = True
    guess = eval(input("Enter a guess (1-100): "))
    if guess == correct_number:
        print("You win! it took 1 guess.")
    while guesses <= 7 and is_running:
        guesses += 1
        if guess > correct_number:
            print("This guess is too high!")
        elif guess < correct_number:
            print("This guess is too low!")
        else:
            is_running = False
        if is_running:
            guess = eval(input("Enter a guess (1-100): "))
        if not is_running and guesses != 1:
            print("You win! It took " + str(guesses) + " guesses.")


def main():
    hi_lo_game()
    num_digits()
    x = read_data("dataSorted.txt")
    print(is_in_linear(10, x))
    find_and_remove(x, 7)
    print(x)
    x = good_input()
    print(x)
    pass


main()
