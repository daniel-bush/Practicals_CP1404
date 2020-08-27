def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    user = input("Please enter username: ")
    if user in usernames:
        print("Access granted:")
        numbers = collect_numbers()
        calculate_stats(numbers)
    else:
        print("Access denied")


def collect_numbers() -> list:
    """Collect numbers as integers from user and adds them to a list. The list is returned."""
    numbers = []
    number = int(input("Number {}: ".format(len(numbers) + 1)))
    while number >= 0:
        numbers.append(number)
        number = int(input("Number {}: ".format(len(numbers) + 1)))
    return numbers


def calculate_stats(number_list: list) -> None:
    """Print statistics to the screen based on the number list that it is passed."""
    print("The first number is {}".format(number_list[0]))
    print("The last number is {}".format(number_list[-1]))
    print("The smallest number is {}".format(min(number_list)))
    print("The largest number is {}".format(max(number_list)))
    average = sum(number_list) / len(number_list)
    print("The average of the numbers is {}".format(average))



main()