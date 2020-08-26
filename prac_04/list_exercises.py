def main():
    numbers = collect_numbers()
    calculate_stats(numbers)


def collect_numbers() -> list:
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))
    return numbers


def calculate_stats(number_list: list):
    print("The first number is {}".format(number_list[0]))
    print("The last number is {}".format(number_list[-1]))
    print("The smallest number is {}".format(min(number_list)))
    print("The largest number is {}".format(max(number_list)))
    average = sum(number_list) / len(number_list)
    print("The average of the numbers is {}".format(average))


main()