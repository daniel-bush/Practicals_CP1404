"""hex_colours exercise."""

HEX_COLOURS_DICT = {"aquamarine": "#7fffd4", "beige": "#f5f5dc", "brown": "#a52a2a",
                    "blue": "#0000ff", "coral": "#ff7f50", "darkviolet": "#9400d3", "gold": "#ffd700",
                    "gray": "#bebebe", "orange": "#ffa500", "orchid": "#da70d6"}

colour = input("Colour: ").lower()
while colour != "":
    if colour in HEX_COLOURS_DICT:
        print("The hex code for {} is {}.".format(colour, HEX_COLOURS_DICT[colour]))
    else:
        print("Incorrect colour!")
    colour = input("Colour: ").lower()
print("Thank you!")


