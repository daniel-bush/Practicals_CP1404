x = int(input("x = "))
y = int(input("y = "))

menu = "You choose x = {} and y = {}\n" \
       "1) Show the even numbers from x to y\n" \
       "2) Show the odd numbers from x to y\n" \
       "3) Show the squares from x to y\n" \
       "4) Exit the program\n" \
       ">>> ".format(x, y)

choice = int(input(menu))
