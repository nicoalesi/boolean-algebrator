# This contains all the useful functions, used by the progam to connect
# other function or to perform secondary operations

from libraries.calculators import *
from libraries.message_printers import print_conversion_modes

# This list defines all the exportable functions to other files.
__all__ = [
    "choose_conversion_mode",
]

# This function manages the choice of the conversion mode
def choose_conversion_mode():
    print_conversion_modes()
    expression = input("Expression: ")
    mode = input("Mode: ")

    match mode:
        case "1":
            generate_truth_table(expression)
        case "2":
            # min form
            ...
        case "3":
            # min form
            generate_truth_table(expression)
        case _:
            print("Command not found.")