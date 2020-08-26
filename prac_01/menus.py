user_name = input("Enter name: ")
menu = "(H)ello\n" \
       "(G)oodbye\n" \
       "(Q)uit\n" \
       ">>> "
menu_choice = input(menu).upper()

while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello", user_name)
    elif menu_choice == "G":
        print("Goodbye", user_name)
    else:
        print("Invalid choice")
    menu_choice = input(menu).upper()
print("Finished")
