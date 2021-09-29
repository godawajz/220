"""
Name: Joanna Godawa
traffic.py

Calculates average number of cars on a road per day, total cars on all roads, and average cars per
road for a specified set of roads and days.

Certificate of authenticity:
I certify that this assignment is my own work."""


def main():
    average_per_day = int
    road_total = int
    total_vehicles = 0
    total_average = 0

    roads_surveyed = eval(input("How many roads were surveyed? "))

    for i in range(1, roads_surveyed + 1):
        average_per_day = 0
        road_total = 0

        inquiry = 'How many days was road ' + str(i) + ' surveyed? '
        days_surveyed = eval(input(inquiry))

        for j in range(1, days_surveyed + 1):
            inquiry = '\tHow many cars traveled on day ' + str(j) + ' ? '
            road_total += eval(input(inquiry))

        average_per_day = road_total / days_surveyed
        total_vehicles += road_total

        print("Road", i, "average vehicles per day:", round(average_per_day, 2))

    total_average = total_vehicles / roads_surveyed

    print("Total number of vehicles on all roads:", round(total_vehicles, 2))
    print("Average number of vehicles per road:", round(total_average, 2))


if __name__ == "__main__":
    main()
