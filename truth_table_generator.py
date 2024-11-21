from libraries.converters import start_generation
from libraries.message_printers import print_header, print_information

# MAIN function.
def main() -> None:
    # Print instructions.
    print_header()

    # Loop to catch commands.
    while True:
        # Get the command as input.
        command = input("Command: ")

        # Perform matching operations.
        match command:
            case "/generate":
                start_generation()
            case "/help":
                print_header()
            case "/info":
                print_information()
            case "/exit":
                break
            case _:
                print("Command not found.")


if __name__ == "__main__":
    main()
