"""
Name: Joanna Godawa
file: weighted_average.py

Calculates the weighted average of a student's grades and outputs them in a separate file

Certificate of Authenticity:
I certify that this assignment is my own work."""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+")

    class_sum = 0
    num_of_students = 0
    for line in in_file:
        sum_grades = 0
        total_weight = 0

        line = line.strip("\n")
        temp = line.split(": ")

        name = temp[0]
        grades = temp[1].split(" ")

        out_file.write(name + '\'s average: ')

        for i in range(len(grades)):
            if i % 2 == 0:
                total_weight += int(grades[i])

        if total_weight >= 101:
            out_file.write("Error: The weights are more than 100.\n")
        elif total_weight <= 99:
            out_file.write("Error: The weights are less than 100.\n")
        else:
            j = 0
            while j < len(grades):
                grade_x_weight = int(grades[j]) * int(grades[j + 1])
                sum_grades += grade_x_weight
                j += 2
            average = round(sum_grades / 100, 1)
            class_sum += average
            out_file.write(str(average) + '\n')
            num_of_students += 1

    class_average = round(class_sum / num_of_students, 1)
    out_file.write("Class average: " + str(class_average))

    in_file.close()
    out_file.close()


def main():
    weighted_average("grades.txt", "outgrades.txt")


main()
