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

def limit(xval, expr, numerator, denominator):
   
    h = 0.00001

    rightsub = str(xval + h)
    leftsub = str(xval - h)

    subexprright = expr.replace("x", rightsub)
    subexprleft = expr.replace("x", leftsub)

    limitright = eval(subexprright)
    limitleft = eval(subexprleft)

    print("f(x) right = ", limitright)
    print("f(x) left = ", limitleft)

    if round(limitright) != round(limitleft):
        print("Limit does not exist")
    

# MAIN MAIN MAIN
def main():
    
    # Print options 
    print("List of operations: ")
    print("1. Find where a function is undefined")
    
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
