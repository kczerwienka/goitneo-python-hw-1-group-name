def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact does not exist, unable to change."

def phone_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return str(contacts[name])
    else:
        return "Contact does not exist, unable to call."
    
def all_contacts():
    global contacts
    str=""
    for k, v in contacts.items:
        str += ('{:<10} {:<10}\n'.format(k, v))
    return str

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
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        elif command == "all":
            print(all_contacts())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()