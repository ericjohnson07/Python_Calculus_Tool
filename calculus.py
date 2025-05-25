#!/usr/bin/env python3

import re
import sympy

from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

def defineNumerator(function):
    match = re.match(r'^\((.*?)\)/\((.*?)\)$', function)
    if match:
        return match.group(1)
    return None

def defineDenominator(function):
    match = re.match(r'^\((.*?)\)/\((.*?)\)$', function)
    if match:
        return match.group(2)
    return None

def validateInput():
    while True:
        function = input("Enter function in form of (numerator)/(denominator): ")
        count_open_parenthesis = function.count('(')
        count_closed_parenthesis = function.count(')')
        total_parenthesis = count_open_parenthesis + count_closed_parenthesis

        if count_open_parenthesis != count_closed_parenthesis or total_parenthesis % 2 != 0:
            print("Error: Unbalanced parenthesis in function " + function + "...Please try again.")
        else:
            return function

# Definition of function to find aymptotes. numerator and denominator parameter values defined in main
def undefined(numerator, denominator):

    # Variable to concatenate numerator and denominator into single object
    function = "(" + numerator + ")/(" + denominator + ")"

    # Variable to store solution to check if it is real 
    solution = solve(denominator, x)
    real_solutions = [s for s in solution if s.is_real]

    # If solutions are real, output solutions
    if real_solutions:
        print("In function  " + function + "  undefined at", solve(denominator,x))
    # Else output no undefined points
    else:
        print("Function is not undefined at any point in function " + function)

#def limit(numerator, denominator, x):
#   
#    h = 0.0001
#
#    function = "(" + numerator + ")/(" + denominator + ")"
#
#    rightsub = solve(x + h)
#    leftsub = solve(x - h)
#
#    subfunctionright = function.replace("x", rightsub)
#    subfunctionleft = function.replace("x", leftsub)
#
#    print("f(x) right = ", subfunctionright)
#    print("f(x) left = ", subfunctionleft)
#
#    if round(y_right) != round(y_left):
#        print("Limit does not exist")
    

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
                function = validateInput()
                numerator = defineNumerator(function)
                denominator = defineDenominator(function)
                
                # Checks if numerator and denominator is not null
                if numerator and denominator is not None:
                    undefined(numerator, denominator)
                # Otherwise, call main
                else:
                    main()

            #if option == "2":
             #   numerator = input("Enter numerator of function: ")
              #  numerator = input("Enter denominator of function: ")

            # Else statement for all option inputs
            else:
                main()
        else:
            print("invalid input. Please enter a number.")
            main()
main()
