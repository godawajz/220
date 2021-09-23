"""
Name: Joanna Godawa
file: mean.py

Calculates RMS average, harmonic mean, and geometric mean and outputs result.

Certificate of Authenticity:
I certify that this assignment is my own work."""
import math


def main():
    mean = 0
    rms_average = 0
    harmonic_mean = 0
    geometric_mean = 1

    iterations = eval(input("enter the values to be entered: "))

    for _ in range(iterations):
        temp = eval(input("enter value: "))

        mean += temp ** 2
        harmonic_mean += (1 / temp)
        geometric_mean *= temp

    rms_average = math.sqrt(mean / iterations)
    harmonic_mean = iterations / harmonic_mean
    geometric_mean = math.pow(geometric_mean, 1 / iterations)

    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))


if __name__ == "__main__":
    main()
