"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    subject_details(data)


def subject_details(data):
    """Takes data in list form and prints it into English on the screen."""
    for line in data:
        print("{} is taught by {} and has {} students".format(line[0], line[1], line[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students. Return 'master list'"""
    master_list = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        master_list.append(parts)
    input_file.close()
    return master_list


main()
