# This file contains all the necessary functions to generate the truth table
# and minimal of the boolean expression.

from libraries.exceptions import *

# This list defines all the exportable functions to other files.
__all__ = [
    "generate_truth_table",
]

# This function takes
def generate_truth_table(expression: str) -> None:
    # Check expression elements
    try:
        for c in expression:
            if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ()'+":
                raise ElementError
    except ElementError:
        print("Element not allowed in the expression.")
        return
    
    # Convert the string to an executable string
    variables, expression = convert_symbols_and_get_variables(expression)
    # Calculate the number of variables and the table's width
    n_vars = len(variables)
    table_width = 2*(n_vars) + 1

    # Print the table
    print()
    print("+" + "-" * table_width + "+---+")
    print("| " + " ".join(variables) + " | Y |")
    print("+" + "-" * table_width + "+---+")
    for n in range(2**n_vars):
        # Use binary numbers to obtain input values:
        #  0 -> 0000 -> 0 0 0 0
        #  1 -> 0001 -> 0 0 0 1
        #  2 -> 0010 -> 0 0 1 0
        values = bin(n)[2:]
        if len(values) < n_vars:
            values = "0" * (n_vars - len(values)) + values
        
        # Replace all variables with actual values for security reasons
        #  (If you try to inject a function it is converted in a bunch of 0s and 1s)
        #  (i.e. import -> 001100)
        temp_expression = expression
        for i in range(len(variables)):
            temp_expression = temp_expression.replace(variables[i], values[i])
        # Obtain the output executing the expression
        result = str(int(eval(temp_expression)))

        print("|" + values.replace("", " ") + "| " + result + " |")
    print("+" + "-" * table_width + "+---+")


# This function converts all the symbols in the boolean expression to their
# correspondent words and keeps track of all the variales in it.
def convert_symbols_and_get_variables(equation: str) -> (str, list):
    # Useful variables
    variables = []
    final_equation = " "
    stack_levels = 0
    # Stack to keep track of parentheses structure
    parentheses_stack = []
    start = len(equation) - 1

    # Iterate through the expression charwise
    for i in range(start, 0, -1):
        # Get the current char
        char = equation[i]

        # Check if it's an open parenthesis
        if char == ")":
            # If stack_levels != 0 means there are some nested parentheses
            if stack_levels:
                if parentheses_stack[-1][-1] not in ["(", " "]:
                    parentheses_stack[-1] += " and "
            else:
                if final_equation[-1] not in ["(", " "]:
                    final_equation += " and "

            stack_levels += 1
            parentheses_stack.append("(")
            continue

        # Check if it's a closed parenthesis
        # If so merge the last to layers of the stack and pop the last one
        if char == "(":
            parentheses_stack[-1] += ")"
            if stack_levels <= 1:
                final_equation += parentheses_stack[-1]
            else:
                parentheses_stack[-2] += parentheses_stack[-1]
            
            parentheses_stack.pop()
            stack_levels -= 1
            continue

        # Add new (unique) variables to variables' list
        if char not in ["+", "'"] and char not in variables:
            variables.append(char)

        # Take care of all the cases in which char not in "()"
        # Translate ' in 'not', + in 'or', no-space in 'and'
        # Follow some strict rules to not create ambiguity

        # This is the logic when it is processing the content inside parentheses
        if stack_levels:
            match char:
                case "'":
                    # If char -> ', write 'not' or 'not or' based on other chars  
                    if parentheses_stack[-1][-1] == " " or parentheses_stack[-1][-1] == "(":
                        parentheses_stack[-1] += " not "
                    elif parentheses_stack[-1][-1] == "+":
                        parentheses_stack[-1] += " or not "
                    else:
                        parentheses_stack[-1] += " and not "

                case "+":
                    # If char -> +, write 'or'
                    parentheses_stack[-1] += " or "

                case _:
                    # If char -> <variable>, write '<variable>' or 'and <variable>'
                    # based on other chars
                    if parentheses_stack[-1][-1] == " " or parentheses_stack[-1][-1] == "(":
                        parentheses_stack[-1] += char
                    else:
                        parentheses_stack[-1] = parentheses_stack[-1] + " and " + char
        # This is the logic when it is processing the content outside parentheses
        else:
            match char:
                case "'":
                    # If char -> ', write 'not' or 'not or' based on other chars 
                    if final_equation[-1] == " ":
                        final_equation += " not "
                    elif final_equation[-1] == "+":
                        final_equation += " or not "
                    else:
                        final_equation += " and not "
                
                case "+":
                    # If char -> +, write 'or'
                    final_equation += " or "

                case _:
                    # If char -> <variable>, write '<variable>' or 'and <variable>'
                    # based on other chars
                    if final_equation[-1] == " ":
                        final_equation += char
                    else:
                        final_equation = final_equation + " and " + char

    # Re-do all the check for the last char 
    #  (It was not included in the loop)
    if equation[0] not in ["+", "'", "("] and equation[0] not in variables:
        variables.append(equation[0])

    if equation[0] == "(":
        parentheses_stack[-1] += ")"
        final_equation += parentheses_stack[-1]
    else:
        if final_equation[-1] == " ":
            final_equation += equation[0]
        else:
            final_equation = final_equation + " and " + equation[0]

    # Return the results: sorted variables and executable equation
    return sorted(variables), final_equation
