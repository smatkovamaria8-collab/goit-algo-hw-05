#Exercise 4
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return f"Current name was not found in dictionary."
        except IndexError:
            return f"Please provide an argument"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        variable = "added"
    else:
        contacts[name] = phone
        variable = "changed"
    return f"Contact {variable}."

@input_error
def what_number(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def all_contacts(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in ["add", "change"]:
            print(add_contact(args, contacts))
        elif command == "phone":
            print(what_number(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()