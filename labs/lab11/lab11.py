"""
Name: Joanna Godawa
lab11.py
"""
from random import randint


def word_list(file_name):
    in_file = open(file_name, "r")
    words = in_file.readlines()
    for i in range(len(words)):
        words[i] = words[i].rstrip('\n')
    in_file.close
    return words


def get_word(words):
    selection = randint(0, len(words) - 1)
    return words[selection]


def guessed_letters(word, guesses):
    display = ""
    for i in range(len(word)):
        is_guessed = False
        for j in range(len(guesses)):
            if word[i] == guesses[j]:
                display += guesses[j]
                is_guessed = True
        if not is_guessed:
            display += "_"
    return display


def is_word_guessed(display, word):
    if display == word:
        return True
    return False


def is_repeat(guess, correct, incorrect):
    for letter in correct:
        if guess == letter:
            return True
    for letter in incorrect:
        if guess == letter:
            return True


def play_game(word):
    display_guesses = ""
    for _ in range(len(word)):
        display_guesses += "_"
    incorrect_guesses = []

    print("================ Hangman ================")
    print(display_guesses)

    guess = input("Guess a letter: ")

    correct_letter = ""
    correct_guesses = []
    for letter in word:
        if guess == letter and not \
                is_repeat(guess, correct_guesses, incorrect_guesses):
            correct_letter = guess
            correct_guesses += correct_letter
            display_guesses = guessed_letters(word, correct_guesses)
            break
    if not correct_letter and not \
            is_repeat(guess, correct_guesses, incorrect_guesses):
        incorrect_guesses += guess

    while len(incorrect_guesses) < 7:
        print(display_guesses)
        print("\nIncorrect guesses:", len(incorrect_guesses))
        print("Letters guessed:", end=" ")
        for i in range(len(incorrect_guesses)):
            if i != len(incorrect_guesses) - 1:
                print(incorrect_guesses[i], end=", ")
            else:
                print(incorrect_guesses[i])

        guess = input("Guess a letter: ")

        correct_letter = ""
        for letter in word:
            if guess == letter and not \
                    is_repeat(guess, correct_guesses, incorrect_guesses):
                correct_letter = guess
                correct_guesses += correct_letter
                display_guesses = guessed_letters(word, correct_guesses)
                break
        if not correct_letter and not \
                is_repeat(guess, correct_guesses, incorrect_guesses):
            incorrect_guesses += guess

        if len(incorrect_guesses) == 7:
            print("\nOut of guesses. You lose!\n\tCorrect word:", word)
            break
        if is_word_guessed(display_guesses, word):
            print("\nYou win!\n\tCorrect word:", word)
            break


def main():
    words = word_list("wordlist.txt")
    word = get_word(words)
    play_game(word)
    pass


main()
