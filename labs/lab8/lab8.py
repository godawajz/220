"""
Name: Joanna Godawa
lab8.py
"""

import encryption


def number_words(in_file_name, out_file_name):
    f_in = open(in_file_name, "r")
    f_out = open(out_file_name, "w+")

    lines = f_in.readlines()
    ct = 1
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        words = lines[i].split(" ")
        for j in range(len(words)):
            f_out.write(str(ct) + " " + words[j] + "\n")
            ct += 1
    f_in.close()
    f_out.close()


def hourly_wages(in_file_name, out_file_name):
    f_in = open(in_file_name, "r")
    f_out = open(out_file_name, "w+")

    for line in f_in:
        s = line.split(" ")
        s[-1] = s[-1].strip('\n')
        wage = float(s[-2]) + 1.65
        wage *= int(s[-1])

        f_out.write(s[0] + ' ' + s[1] + ': $' + str(wage) + '\n')
    f_in.close()
    f_out.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(0, 10):
        acc += (int(isbn[i : i + 1]) * (10 - i))
    return acc



def send_message(file, friend):
    f_in = open(file, "r")
    f_out = open(friend + ".txt", "w+")
    for line in f_in:
        f_out.write(line)
    f_in.close()
    f_out.close()


def send_safe_message(file, friend, key):
    f_in = open(file, "r")
    f_out = open(friend + ".txt", "w+")
    for line in f_in:
        f_out.write(encryption.encode(line, key))
    f_in.close()
    f_out.close()


def send_uncrackable_message(file, friend, pad):
    f_in = open(file, "r")
    f_out = open(friend + ".txt", "w+")
    f_key = open(pad, "r")
    for line in f_in:
        key = f_key.readline()
        key.strip('\n')
        f_out.write(encryption.encode_better(line, key))


def main():
    number_words("Walrus.txt", "Walrus_Out.txt")
    hourly_wages("hourly_wages.txt", "new_hourly_wages.txt")

    x = calc_check_sum("0072946520")
    print(x)

    send_message("message.txt", "bob")
    send_safe_message("secret_message.txt", "sam", 3)
    send_uncrackable_message("safest_message.txt", "jim", "pad.txt")
    pass


main()
