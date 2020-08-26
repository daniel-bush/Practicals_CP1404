MIN_LENGTH = 10


def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    for char in password:
        print("*", end="")


def get_password(MIN_LENGTH):
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("Password must be at least {} characters!".format(MIN_LENGTH))
        password = input("Password: ")
    return password


main()
