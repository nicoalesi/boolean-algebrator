# This file contains all the printer functions used for displaying messages by
# the main program.

# This function prints the purpose of the program and the list of available
# commands.
def print_header() -> None:
    print()

    print("+----------------- BOOLEAN CALCULATOR -----------------+")
    print("|                                                      |")
    print("|  Use this program to generate the truth table or     |")
    print("|  the minimal form of a boolean expression.           |")
    print("|                                                      |")
    print("|  Commands:                                           |")
    print("|    /t-table            - Generate the truth table    |")
    print("|    /min-form           - Generate the minimal form   |")
    print("|    /help               - Print this message again    |")
    print("|    /exit               - Exit the program            |")
    print("|                                                      |")
    print("+------------------------------------------------------+")
