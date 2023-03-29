phone_book = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Please enter name and phone number separated by space"
        except IndexError:
            return "Please enter contact name"
        except:
            return "An error occurred"

    return inner


@input_error
def add_contact(name, phone):
    phone_book[name.lower()] = phone
    return f"Contact {name} with phone number {phone} has been added"


@input_error
def change_contact(name, phone):
    phone_book[name.lower()] = phone
    return f"Phone number for {name} has been changed to {phone}"


@input_error
def get_phone(name):
    return phone_book[name.lower()]


def show_all():
    if not phone_book:
        return "Phone book is empty"
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in phone_book.items())


def handle_command(command):
    command = command.lower()
    if command == "hello":
        return "How can I help you?"
    elif command in ("", "close", "exit"):
        return "Good bye!"
    elif command.startswith("add"):
        parts = command.split()
        if len(parts) < 3:
            return "Please enter contact name and phone number"
        _, name, phone = parts
        return add_contact(name, phone)
    elif command.startswith("change"):
        parts = command.split()
        if len(parts) < 3:
            return "Please enter contact name and phone number"
        _, name, phone = parts
        return change_contact(name, phone)
    elif command.startswith("phone"):
        parts = command.split()
        if len(parts) < 2:
            return "Please enter contact name"
        _, name = parts
        return get_phone(name)
    elif command == "show all":
        return show_all()
    else:
        return "Unknown command"


def main():
    while True:
        command = input("Enter command: ")
        result = handle_command(command)
        print(result)
        if result == "Good bye!":
            break


if __name__ == '__main__':
    main()
