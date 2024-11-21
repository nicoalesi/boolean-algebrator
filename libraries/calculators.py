# This file contains all the necessary functions to generate the truth table
# of the boolean expression.

from libraries.exceptions import *
from libraries.message_printers import print_syntax_information

# This list defines all the exportable functions to other files.
__all__ = [
    "start_generation",
    "generate_truth_table",
    "convert_symbols_and_get_variables",
]

# This function starts the process of generation, it prints syntax
# rules, gets the expression as input and calls the generating function.
def start_generation() -> None:
    # Print rules.
    print_syntax_information()
    # Ask the user for a boolean expression.
    expression = input("Expression: ").upper()
    # Call the generating function and pass the expression.
    generate_truth_table(expression)


# This function takes an expression and generate its truth table.
def generate_truth_table(expression: str) -> None:
    # Check expression elements.
    try:
        for c in expression:
            # If one of the elements is not allowed raise and exception
            # and stop the generating process.
            if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ()'+":
                raise ElementError
    except ElementError:
        print("Element not allowed in the expression.")
        return
    
    # Convert the string to an executable string and obtain the list
    # of all the unique variables used in it, sorted alphabetically.
    variables, expression = convert_symbols_and_get_variables(expression)
    # Calculate the number of variables and the table's width.
    n_vars = len(variables)
    table_width = 2*(n_vars) + 1

    # Print the table.

    # Print table's heading.
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
        
        # Replace all variables with actual values for security reasons.
        #  (If you try to inject a function it is converted in a bunch of 0s and 1s)
        #  (i.e. import -> 001100)
        temp_expression = expression
        for i in range(len(variables)):
            temp_expression = temp_expression.replace(variables[i], values[i])
        # Obtain the output executing the expression.
        result = str(int(eval(temp_expression)))

        # Print current row with inputs and output.
        print("|" + values.replace("", " ") + "| " + result + " |")
    
    # Print table's lower border.
    print("+" + "-" * table_width + "+---+")


# This function converts all the symbols in the boolean expression to their
# correspondent words and keeps track of all the variales in it.
def convert_symbols_and_get_variables(equation: str) -> (str, list):
    # Useful variables

    # List of unique variables.
    variables = []
    # This string stores the result (executable boolean expression),
    # the space is needed in order to make the algorithm work.
    final_equation = " "
    # Number of nested parentheses -> Stack's layers.
    stack_levels = 0
    # Stack to keep track of parentheses structure.
    parentheses_stack = []
    # Starting index to read, the expression is read from right to left.
    start = len(equation) - 1

    # Iterate through the expression charwise.
    for i in range(start, 0, -1):
        # Get the current char
        char = equation[i]

        # Check if it's an open parenthesis.
        if char == ")":
            # If stack_levels != 0 means the char is inside one or more
            # parentheses so perform actions on the stack.
            if stack_levels:
                if parentheses_stack[-1][-1] not in ["(", " "]:
                    parentheses_stack[-1] += " and "
            # Otherwise the char is outside all of the parentheses, hence
            # perform actions on the final equation's string.
            else:
                if final_equation[-1] not in ["(", " "]:
                    final_equation += " and "

            # Since the char was an opening parenthesis add a layer
            # to the stack and increment its levels' counter.
            stack_levels += 1
            parentheses_stack.append("(")
            continue

        # Check if it's a closed parenthesis.
        # If so merge the last to layers of the stack and pop the last one.
        if char == "(":
            # Add the closing parenthesis.
            parentheses_stack[-1] += ")"
            # Merge this layer with the lower one if it exists, otherwise
            # merge it with the final equation.
            if stack_levels <= 1:
                final_equation += parentheses_stack[-1]
            else:
                parentheses_stack[-2] += parentheses_stack[-1]
            
            # Take the last layer out of the stack and decrement the
            # number of layers' counter.
            parentheses_stack.pop()
            stack_levels -= 1
            continue

        # If char is a new variable, add it to the list.
        #   (No duplicates, unique variables)
        if char not in ["+", "'"] and char not in variables:
            variables.append(char)

        # Take care of all the cases in which char not in "()".
        # Translate ' in 'not', + in 'or', no-space in 'and'.
        # Follow some strict rules to not create ambiguity.

        # This is the logic when it is processing the content inside parentheses.
        if stack_levels:
            match char:
                case "'":
                    # If char -> {'}, write 'not' or 'not or' or 'and not'
                    # based on previous char.
                    if parentheses_stack[-1][-1] == " " or parentheses_stack[-1][-1] == "(":
                        parentheses_stack[-1] += " not "
                    elif parentheses_stack[-1][-1] == "+":
                        parentheses_stack[-1] += " or not "
                    else:
                        parentheses_stack[-1] += " and not "

                case "+":
                    # If char -> {+}, write 'or'.
                    parentheses_stack[-1] += " or "

                case _:
                    # If char -> <variable>, write '<variable>' or 'and <variable>'
                    # based on previous chars.
                    if parentheses_stack[-1][-1] == " " or parentheses_stack[-1][-1] == "(":
                        parentheses_stack[-1] += char
                    else:
                        parentheses_stack[-1] = parentheses_stack[-1] + " and " + char
        # This is the logic when it is processing the content outside parentheses.
        else:
            match char:
                case "'":
                    # If char -> {'}, write 'not' or 'not or' or 'and not'
                    # based on previous char.
                    if final_equation[-1] == " ":
                        final_equation += " not "
                    elif final_equation[-1] == "+":
                        final_equation += " or not "
                    else:
                        final_equation += " and not "
                
                case "+":
                    # If char -> {+}, write 'or'.
                    final_equation += " or "

                case _:
                    # If char -> <variable>, write '<variable>' or 'and <variable>'
                    # based on previous chars.
                    if final_equation[-1] == " ":
                        final_equation += char
                    else:
                        final_equation = final_equation + " and " + char

    # Re-do all the check for the last char.
    #  (It was not included in the loop)

    # If it is a new variable, add it to the list.
    if equation[0] not in ["+", "'", "("] and equation[0] not in variables:
        variables.append(equation[0])

    # Check if it's a closed parenthesis.
    # If so merge the last to layers of the stack and pop the last one.
    if equation[0] == "(":
        # Add the closing parenthesis.
        parentheses_stack[-1] += ")"
        # Merge this layer with the final equation.
        final_equation += parentheses_stack[-1]
    else:
        # Check the previous char and add the current one accordingly.
        if final_equation[-1] == " ":
            # If there is a symol before, just add it.
            final_equation += equation[0]
        else:
            # Otherwise write an 'and', then add it.
            final_equation = final_equation + " and " + equation[0]

    # Return the results: sorted variables and executable equation
    return sorted(variables), final_equation
