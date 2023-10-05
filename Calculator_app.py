# A simple calculator application implementing the concepts of defensive programming

import os

# Define a number input function to get user inputs
def number_inputs(nums):
    while True:
        # Using try-except block as a part of defensive programming to encounter the anticipated errors
        try:
            number = float(input(nums))
            return number
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Define a operator input function
def operator_input():
    operators_list = ["+", "-", "*", "/"]
    # Using a while loop to iterate through the list of operators
    while True:
        operator = input("Please enter an operator(+, -, *, /): ")
        # Using if statements to encounter the errors that occurs when entering unavailable operators
        if operator in operators_list:
            return operator
        else:
            print("Invalid input! Please enter a valid operator.")


# Define a function to write the equation to a text file
def write_file(equation):
    with open("equations.txt", "a") as file:
        file.write(equation+"\n")


# Define a function to read equations from the text file
def read_file(filename):
    try:
        with open(filename, "r") as file:
            equations = file.readlines()
            return equations
    except FileNotFoundError:
        return None


# Define the calculation function to carry out desired calculation upon various comparison
def calculation():
    while True:
        # Taking user input to determine user's preference of calculation
        calculation_option = input("""
Please select the choice of your calculation:
S- Self Inputs
R- Read from the file
: """).lower()
        if calculation_option == "s":
            # Taking user inputs while calling the defined functions
            number1 = number_inputs("Please enter the first number: ")
            number2 = number_inputs("Please enter the second number: ")
            operation = operator_input()
            if operation == "+":
                result = number1 + number2
            elif operation == "-":
                result = number1 - number2
            elif operation == "*":
                result = number1 * number2
            elif operation == "/":
                result = number1 / number2
            else:
                print("Invalid input! Please enter a valid operator.")

            equation = f"{number1} {operation} {number2} = {result}"
            print(equation)
            # Writing equation to the file
            write_file(equation)
            break

        elif calculation_option == "r":
            filename = input("Please enter the file name: ")
            # Reading equation from the file
            read_file(filename)
            equations = read_file(filename)
            # Displaying every equation from the input file if the file with provided name exists
            if equations is not None:
                for eq in equations:
                    print(eq)
            else:
                print("Invalid filename input! Please try again.")


# Calling out the calculation function
calculation()
