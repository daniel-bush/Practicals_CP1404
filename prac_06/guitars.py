"""CP1404 guiters.py task."""

from prac_06.guitar import Guitar


def main():
    """Gets user to input guitars."""
    guitars = []

    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: "))
    #     guitar_to_add = Guitar(name, year, cost)
    #     guitars.append(guitar_to_add)
    #     print("{} added".format(guitar_to_add))
    #     name = input("Name: ")


    # test code to avoid input
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i in guitars:
        print(i)

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {}: {:<20} ({}), worth $ {:10,.2f}{}"
                  .format(i, guitar.name, guitar.year, guitar.cost, vintage_string))
    else:
        print("No guitars.")


main()
