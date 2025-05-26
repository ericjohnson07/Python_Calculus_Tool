#!/usr/bin/env python3

import re
import sympy

from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

# Function to separate numerator from given expression
def defineNumerator(expr):
    match = re.match(r'^\((.*?)\)/\((.*?)\)$', expr)
    if match:
        return match.group(1)
    return None

# Function to separate denominator from given expression
def defineDenominator(expr):
    match = re.match(r'^\((.*?)\)/\((.*?)\)$', expr)
    if match:
        return match.group(2)
    return None

# Function to validate the parenthesis syntax of expression
def validateInput():
    while True:
        expr = input("Enter expression in form of (numerator)/(denominator), 'q' to quit: ")
        count_open_parenthesis = expr.count('(')
        count_closed_parenthesis = expr.count(')')
        total_parenthesis = count_open_parenthesis + count_closed_parenthesis

        if count_open_parenthesis != count_closed_parenthesis or total_parenthesis % 2 != 0:
            print("Error: Unbalanced parenthesis in expression " + expr + "...Please try again.")
        else:
            return expr

# Definition of function to find aymptotes. numerator and denominator parameter values defined in main
def undefined(expr, numerator, denominator):

    # Variable to store solution to check if it is real 
    solution = solve(denominator, x)
    real_solutions = [s for s in solution if s.is_real]

    # If solutions are real, output solutions
    if real_solutions:
        print("In function  " + expr + "  undefined at", solve(denominator,x))
    # Else output no undefined points
    else:
        print("Function is not undefined at any point in function " + expr)

# Function to determine limit of given expression
def limit(xval, expr, numerator, denominator):
   
    # Small value of h to substitute into right and left limits
    h = 0.00001

    # Evaluate approaching to value
    rightsub = str(xval + h)
    leftsub = str(xval - h)

    # Replace all values of "x" within the given expression with the approaching to value
    subexprright = expr.replace("x", "(" + rightsub + ")")
    subexprleft = expr.replace("x", "(" + leftsub + ")")

    # Evaluate final expression to determine limits
    limitright = eval(subexprright)
    limitleft = eval(subexprleft)
   
    print("\nLimit from right (" + str(xval) + "+) = ", limitright)
    print("\nLimit from left (" + str(xval) + "-) = ", limitleft)

    if round(limitright) != round(limitleft):
        print("\nLimit does not exist at x =", xval)
    else:
        limit = eval(expr.replace("x",str(xval)))
        print("\nNo asymptote at given value of x = " + str(xval) + ", limit of function is " + str(limit) + "\n")
    

# MAIN MAIN MAIN
def main():
    
    # Print options 
    print("List of operations: ")
    print("1. Find where a function is undefined\n2. Find the limits of a function's aymptotes at a given value of x")
    
    # Gather user input for choice of operation
    option = input("Enter option: ")

    while True:
        # Filters non-numeric answers out
        if option.isnumeric():
            # If statement for option 1 (Undefined point of a function)
            if option == "1":
                expr = validateInput()
                numerator = defineNumerator(expr)
                denominator = defineDenominator(expr)
                
                # Checks if numerator and denominator is not null
                if numerator and denominator is not None:
                    undefined(expr, numerator, denominator)
                # Otherwise, call main
                else:
                    main()
            if option == "2":
                expr = validateInput()
                xval = float(input("Enter value of x where limit approaches: "))
                numerator = defineNumerator(expr)
                denominator = defineDenominator(expr)

                if numerator and denominator is not None:
                    limit(xval, expr, denominator, numerator)
                
                else:
                    main()

            # Else statement for all option inputs
            else:
                main()
        else:
            print("invalid input. Please enter a number.")
            main()
main()
