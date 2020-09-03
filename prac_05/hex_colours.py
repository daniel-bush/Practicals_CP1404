"""hex_colours exercise."""

HEX_TO_COLOUR = {"aquamarine": "#7fffd4", "beige": "#f5f5dc", "brown": "#a52a2a",
                    "blue": "#0000ff", "coral": "#ff7f50", "darkviolet": "#9400d3", "gold": "#ffd700",
                    "gray": "#bebebe", "orange": "#ffa500", "orchid": "#da70d6"}

colour = input("Colour: ").lower()
while colour != "":
    if colour in HEX_TO_COLOUR:
        print("The hex code for {} is {}.".format(colour, HEX_TO_COLOUR[colour]))
    else:
        print("Incorrect colour!")
    colour = input("Colour: ").lower()
print("Thank you!")


