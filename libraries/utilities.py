# This contains all the useful functions, used by the progam to connect
# other function or to perform secondary operations

# This function manages the choice of the conversion mode
def choose_conversion_mode():
    print_conversion_modes()
    expression = input("Expression: ")
    mode = input("Mode: ")

    match mode:
        case "1":
            calculate_truth_table(expression)
        case "2":
            # min form
            ...
        case "3":
            # min form
            calculate_truth_table(expression)
        case _:
            print("Command not found.")