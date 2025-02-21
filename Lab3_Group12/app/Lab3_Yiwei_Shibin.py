# Author : Shibin Shaji, Yiwei Li
# Date : 19, Feb 2025
# Description : This is a program that calculates the area of different shapes

from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return pi * (r ** 2)

def trapezium_area(a, b, h):
    if a < 0 or b < 0 or h < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * (a + b) * h

def ellipse_area(a, b):
    if a < 0 or b < 0:
        raise ValueError("Axes must be non-negative")
    return pi * a * b

def rhombus_area(d1, d2):
    if d1 < 0 or d2 < 0:
        raise ValueError("Diagonals must be non-negative")
    return 0.5 * d1 * d2

def get_positive_float(prompt):
    try:
        value = float(input(prompt).strip())
        if value < 0:
            raise ValueError("Value must be non-negative.")
        return value
    except ValueError:
        print("Error: Invalid input. Please enter a positive number.")
        return get_positive_float(prompt)

def menu():
    while True:
        print("\nSelect a shape to calculate area:")
        print("C - Circle")
        print("T - Trapezium")
        print("E - Ellipse")
        print("R - Rhombus")
        print("Q - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'C':
            r = get_positive_float("Enter the radius: ")
            print(f"Circle Area: {circle_area(r):.2f}")
        elif choice == 'T':
            a = get_positive_float("Enter base1: ")
            b = get_positive_float("Enter base2: ")
            h = get_positive_float("Enter height: ")
            print(f"Trapezium Area: {trapezium_area(a, b, h):.2f}")
        elif choice == 'E':
            a = get_positive_float("Enter semi-major axis: ")
            b = get_positive_float("Enter semi-minor axis: ")
            print(f"Ellipse Area: {ellipse_area(a, b):.2f}")
        elif choice == 'R':
            d1 = get_positive_float("Enter diagonal 1: ")
            d2 = get_positive_float("Enter diagonal 2: ")
            print(f"Rhombus Area: {rhombus_area(d1, d2):.2f}")
        elif choice == 'Q':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()

