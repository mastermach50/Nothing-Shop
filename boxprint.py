# Box Print

# A module to print output in a neat little box.

charset1 = {"tr":"┓", "tl":"┏", "br":"┛", "bl":"┗", "vr":"┃", "hr":"━"}
charset2 = {"tr":"╗", "tl":"╔", "br":"╝", "bl":"╚", "vr":"║", "hr":"═"}
charset3 = {"tr":"╮", "tl":"╭", "br":"╯", "bl":"╰", "vr":"│", "hr":"─"}

chars = charset3

# Neatly print the output in a box
# Can be used to replace the print() function
def box(lines, width=40):
    """Print the output neatly in a box

    Accepts list of strings as argument and prints
    each string as a line in a box"""
    
    # if line is longer that width, then set it as width
    for line in lines:
        if len(line)>width:
            width = len(line)

    # pad the right of all lines with spaces
    newlines = []
    for line in lines:
        newlines.append(line+ " "*(width-len(line)))

    # print lines in a box
    print(chars["tl"] + chars["hr"]*(width+2) +chars["tr"]) # print top of box
    for line in newlines:
        print(chars["vr"]+" " + line + " "+chars["vr"])
    print(chars["bl"] + chars["hr"]*(width+2) +chars["br"]) # print bottom of box

# A function to add spaces to the end of a string to make it a given length
def pad(string, length):
    """Pad right side of a string with spaces"""

    string = str(string)
    if len(string) > length:
        return string
    else:
        new_string = string + (length-len(string))*" " # Adds spaces to end of string
        return new_string