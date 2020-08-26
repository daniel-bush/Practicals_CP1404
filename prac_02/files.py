# 1 write to file
name_file = open("name.txt", "w")
name = input("What is your name: ")
print(name, file=name_file)
name_file.close()

# 2 open file and read entire contents
name_file = open("name.txt", "r")
name = name_file.read().strip()
name_file.close()
print("Your name is {}".format(name))

# 3 summing first 2 lines of a
number_file = open("numbers.txt", "r")
first_no = int(number_file.readline())
second_no = int(number_file.readline())
number_file.close()
print(first_no + second_no)

# 4 summing all numbers in a file
number_file = open("numbers.txt", "r")
total = 0
for line in number_file:
    number = int(line)
    total += number
number_file.close()
print(total)
