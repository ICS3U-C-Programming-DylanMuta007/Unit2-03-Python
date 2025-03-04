#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :23-02-2025
# This program calculates total cost of a pizza

import math
import constant


def main():
    # Creates variables pizza_amount & pizza_diameter and asks the user to assign a value
    pizza_amount = int(input("How many pizzas are you getting? "))
    pizza_diameter = int(input("What is the diameter of your pizza? "))
    print("")  # whitespace

    # Calculates the subtotal, tax, and total of the pizza
    labour_cost = (2.00) * pizza_amount
    rental_cost = (2.25) * pizza_amount
    subtotal = float(labour_cost + rental_cost + pizza_diameter * 1.5)
    tax = float(constant.HST * subtotal)
    total = subtotal + tax

    # Displays the result
    print("Your total rounds up to ${:.2f}".format(total))


if __name__ == "__main__":
    main()
