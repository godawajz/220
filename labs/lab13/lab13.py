"""
Name: Joanna Godawa
lab13.py
"""
from graphics import *


def is_in_binary(searchVal, values):
    mid = len(values) // 2
    while values[mid] != searchVal and len(values) != 1:
        if values[mid] > searchVal:
            values = values[:mid]
        else:
            values = values[mid:]
        mid = len(values) // 2
    if values[mid] == searchVal:
        return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]
    return values


def calc_area(rect):
    x_side = abs(rect.getP1().getX() - rect.getP2().getX())
    y_side = abs(rect.getP1().getY() - rect.getP2().getY())
    return x_side * y_side


def rect_sort(rectangles):
    d = {}
    areas = []
    for rect in rectangles:
        d[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = d[areas[i]]
    return rectangles


def trade_alert(filename):
    f_in = open(filename, "r")
    volumes = []
    for line in f_in:
        volumes = line.split(" ")
    for i in range(len(volumes)):
        if int(volumes[i]) > 830:
            print("["+str(i)+" s]: Warning: volume exceeds 830!")
        elif int(volumes[i]) > 500:
            print("["+str(i)+" s]: Volumes have exceeded 500")
    f_in.close()


def main():
    pass


main()
