# This file contains all the printer functions used for displaying messages by
# the main program.

# This function prints the purpose of the program and the list of available
# commands.
def print_header() -> None:
    print()

    print("+-------------------- BOOLEAN CALCULATOR --------------------+")
    print("|                                                            |")
    print("|  Use this program to generate the truth table of           |")
    print("|  a boolean equation.                                       |")
    print("|                                                            |")
    print("|  Commands:                                                 |")
    print("|    /generate           - Generate the truth table          |")
    print("|    /help               - Print this message again          |")
    print("|    /info               - Print information                 |")
    print("|    /exit               - Exit the program                  |")
    print("|                                                            |")
    print("+------------------------------------------------------------+")


# This function prints syntax rules and usage information.
def print_syntax_information() -> None:
    print()

    print("+----------------------- SYNTAX INFO ------------------------+")
    print("|                                                            |")
    print("|  Write the boolean expression without any space.           |")
    print("|  Note: Only letters, boolean operations and                |")
    print("|  parentheses '( )' are allowed.                            |")
    print("|                                                            |")
    print("|  Operators:                                                |")
    print("|    NOT:   - single quote           not A    <->  A'        |")
    print("|    AND:   - multiplication         A and B  <->  AB        |")
    print("|    OR:    - addition               A or B   <->  A+B       |")
    print("|                                                            |")
    print("+------------------------------------------------------------+")

# This function prints information about the project.
def print_information() -> None:
    print()

    print("+----------------------- INFORMATION ------------------------+")
    print("|                                                            |")
    print("|  Author:                                                   |")
    print("|    Nicolo Alesi                                            |")
    print("|                                                            |")
    print("|  License: MIT License                                      |")
    print("|                                                            |")
    print("+------------------------------------------------------------+")
