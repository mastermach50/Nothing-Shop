charset1 = {"tr":"┓", "tl":"┏", "br":"┛", "bl":"┗", "vr":"┃", "hr":"━"}
charset2 = {"tr":"╗", "tl":"╔", "br":"╝", "bl":"╚", "vr":"║", "hr":"═"}
charset3 = {"tr":"╮", "tl":"╭", "br":"╯", "bl":"╰", "vr":"│", "hr":"─"}

chars = charset3

def box(lines, width=40):
    """Print the output neatly in a box"""
    
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

def pad(string, length):
    string = str(string)
    newstring = string + (length-len(string))*" "
    return newstring