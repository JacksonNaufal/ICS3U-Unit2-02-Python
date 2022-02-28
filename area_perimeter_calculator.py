#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: Feb 2022
# This is a Area and perimeter calculator with the dimensions of 5cm x 3cm


def main():
    # This is a calculator that calculates the area and perimeter of a rectangle
    # input
    Length = int(input("Enter Length of rectangle (mm)"))
    Width = int(input("Enter Width of rectangle (mm)"))
    # process
    area = Length * Width
    perimeter = 2 * (Length + Width)
    # output
    print("")
    print("The area of your rectangle is {0} cm².".format(area))
    print("The perimeter of your rectangle is {0} cm.".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
