MIN_LENGTH = 10
password = input("Password: ")
while len(password) < MIN_LENGTH:
    print("Password must be at least {} characters!".format(MIN_LENGTH))
    password = input("Password: ")
for char in password:
    print("*", end="")