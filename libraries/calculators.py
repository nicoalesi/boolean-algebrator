# This file contains all the necessary functions to generate the truth table
# and minimal of the boolean expression.

# This list defines all the exportable functions to other files.
__all__ = [
    "generate_truth_table",
]

# This function takes 
def generate_truth_table(expression: str) -> None:
    # check user input for security
    variables, expression = convert_symbols_and_get_variables(expression)
    n_vars = len(variables)
    table_width = 2*(n_vars) + 1

    print()
    print("+" + "-" * table_width + "+---+")
    print("| " + " ".join(variables) + " | Y |")
    print("+" + "-" * table_width + "+---+")
    for n in range(2**n_vars):
        values = bin(n)[2:]
        if len(values) < n_vars:
            values = "0" * (n_vars - len(values)) + values
        print("|" + values.replace("", " ") + "|")
    print("+" + "-" * table_width + "+---+")


# This function converts all the symbols in the boolean expression to their
# correspondent words and keeps track of all the variales in it.
def convert_symbols_and_get_variables(equation: str) -> (str, list):
    variables = []
    final_equation = " "
    stack_levels = 0
    parentheses_stack = []
    start = len(equation) - 1

    parentheses = {
        "(": ")",
        "[": "]",
        "{": "}",
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for i in range(start, 0, -1):
        char = equation[i]

        if char in [")", "]", "}"]:
            if stack_levels:
                if parentheses_stack[-1][-1] not in ["(", "[", "{", " "]:
                    parentheses_stack[-1] += " and "
            else:
                if final_equation[-1] not in ["(", "[", "{", " "]:
                    final_equation += " and "

            stack_levels += 1
            parentheses_stack.append(parentheses[char])
            continue

        if char in ["(", "[", "{"]:
            parentheses_stack[-1] += parentheses[char]
            if stack_levels <= 1:
                final_equation += parentheses_stack[-1]
            else:
                parentheses_stack[-2] += parentheses_stack[-1]
            
            parentheses_stack.pop()
            stack_levels -= 1
            continue

        if char not in ["+", "'"] and char not in variables:
            variables.append(char.upper())

        if stack_levels:
            match char:
                case "'":
                    if parentheses_stack[-1][-1] == " " or parentheses_stack[-1][-1] in ["(", "[", "{"]:
                        parentheses_stack[-1] += " not "
                    elif parentheses_stack[-1][-1] == "+":
                        parentheses_stack[-1] += " or not "
                    else:
                        parentheses_stack[-1] += " and not "
                case "+":
                    parentheses_stack[-1] += " or "
                case _:
                    if parentheses_stack[-1][-1] == " " or parentheses_stack[-1][-1] in ["(", "[", "{"]:
                        parentheses_stack[-1] += char
                    else:
                        parentheses_stack[-1] = parentheses_stack[-1] + " and " + char
        else:
            match char:
                case "'":
                    if final_equation[-1] == " ":
                        final_equation += " not "
                    elif final_equation[-1] == "+":
                        final_equation += " or not "
                    else:
                        final_equation += " and not "
                
                case "+":
                    final_equation += " or "
                case _:
                    if final_equation[-1] == " ":
                        final_equation += char
                    else:
                        final_equation = final_equation + " and " + char

    if equation[0] not in ["+", "'"] and equation[0] not in variables:
        variables.append(equation[0].upper())

    if equation[0] in ["(", "[", "{"]:
        parentheses_stack[-1] += parentheses[equation[0]]
        final_equation += parentheses_stack[-1]
    else:
        if final_equation[-1] == " ":
            final_equation += equation[0]
        else:
            final_equation = final_equation + " and " + equation[0]

    return sorted(variables), final_equation
