def main():
    numbers = collect_numbers()
    calculate_stats(numbers)

def collect_numbers() -> list:
    numbers = []
    for i in range(5):
        numbers.append(input("Number: "))
    return numbers


def calculate_stats(number_list: list):



main()