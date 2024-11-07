from libraries.message_printers import *

# MAIN function
def main():
    # Print instructions
    print_header()

    # Loop to catch commands.
    while True:
        # Get the command as input.
        command = input("Command: ")

        # Perform matching operations.
        match command:
            case "/t-table":
                ...
            case "/min-form":
                ...
            case "/help":
                print_header()
            case "/info":
                print_information()
            case "/exit":
                break
            case _:
                print("Command not found.")

def calculate(equation: str) -> int:
    final_equation = " "
    stack_levels = 0
    parentheses_stack = []
    start = len(equation) - 1

    parentheses = {
        '(': ')',
        '[': ']',
        '{': '}',
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for i in range(start, 0, -1):
        char = equation[i]

        if char in [')', ']', '}']:
            if stack_levels:
                if parentheses_stack[-1][-1] not in ['(', '[', '{', ' ']:
                    parentheses_stack[-1] += " and "
            else:
                if final_equation[-1] not in ['(', '[', '{', ' ']:
                    final_equation += " and "

            stack_levels += 1
            parentheses_stack.append(parentheses[char])
            continue

        if char in ['(', '[', '{']:
            parentheses_stack[-1] += parentheses[char]
            if stack_levels <= 1:
                final_equation += parentheses_stack[-1]
            else:
                parentheses_stack[-2] += parentheses_stack[-1]
            
            parentheses_stack.pop()
            stack_levels -= 1
            continue

        if stack_levels:
            match char:
                case "'":
                    if parentheses_stack[-1][-1] == " " or parentheses_stack[-1][-1] in ['(', '[', '{']:
                        parentheses_stack[-1] += " not "
                    elif parentheses_stack[-1][-1] == "+":
                        parentheses_stack[-1] += " or not "
                    else:
                        parentheses_stack[-1] += " and not "
                case "+":
                    parentheses_stack[-1] += " or "
                case _:
                    if parentheses_stack[-1][-1] == " " or parentheses_stack[-1][-1] in ['(', '[', '{']:
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


    if equation[0] in ['(', '[', '{']:
        parentheses_stack[-1] += parentheses[equation[0]]
        final_equation += parentheses_stack[-1]
    else:
        if final_equation[-1] == " ":
            final_equation += equation[0]
        else:
            final_equation = final_equation + " and " + equation[0]

    return final_equation

if __name__ == "__main__":
    main()
