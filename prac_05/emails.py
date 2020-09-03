"""
Emails.py prac. Created by Daniel Bush.
"""


def main():
    address_dict = {}
    exit_program = False
    while not exit_program:
        email = input("Email: ")
        if email != "":
            name = get_name(email)
            name_correct = input("Is your name {} (Y/n) ".format(name)).upper()
            if name_correct in ["", "Y"]:
                address_dict[name] = email
            elif name_correct == "N":
                name = input("Name: ")
                address_dict[name] = email
            else:
                print("Invalid choice:")
        else:
            exit_program = True

    for name, email in address_dict.items():
        print("{} ({})".format(name, email))


def get_name(email):
    prefix = email.split("@")[0]
    name = prefix.split(".")
    name = " ".join(name).title()
    return name


main()
