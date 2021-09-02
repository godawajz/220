"""
Name: Joanna Godawa
lab1.py

problem: this function calculates the area of a rectangle.
"""


def calcArea():
    length = 20
    width = 5
    area = length*width

    print("\nArea:", area)


def calcRecArea():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    area = length*width

    print("\nArea:", area)


def calcVolume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length*width*height

    print("\nVolume:", volume)


def shootingPercentage():
    total_shots = eval(input("Enter total shots:"))
    shots_made = eval(input("Enter shots made:"))
    shots_percentage = (shots_made/total_shots)*100

    print("\nPercent of shots made:", shots_percentage, "%")


def coffee():
    coffee_pounds = eval(input("Please enter the total weight of coffee in pounds:"))
    cost_for_weight = coffee_pounds*10.5
    cost_for_shipping = coffee_pounds*.86
    total_cost = round(cost_for_weight+cost_for_shipping+1.5, 2)

    print("\nTotal cost: $", total_cost)


def kilometersToMiles():
    distance_kilometers = eval(input("Please enter the distance traveled in kilometers:"))
    distance_miles = round(distance_kilometers/1.61, 2)

    print("\nDistance in miles:", distance_miles, " miles")
