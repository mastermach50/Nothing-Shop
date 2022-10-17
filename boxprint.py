charset1 = {"tr":"┓", "tl":"┏", "br":"┛", "bl":"┗", "vr":"┃", "hr":"━"}
charset2 = {"tr":"╗", "tl":"╔", "br":"╝", "bl":"╚", "vr":"║", "hr":"═"}
charset3 = {"tr":"╮", "tl":"╭", "br":"╯", "bl":"╰", "vr":"│", "hr":"─"}

chars = charset3

def box(lines, width=40):

    newlines = []
    for line in lines:

        if len(line)>width: # split long lines into smaller lines

            # leave extra space for a hyphen at the end
            while len(line)>width-1:
                newlines.append(line[:width-1]+"-")
                line = line[width-1:]

            newlines.append(line + " "*(width-len(line)))

        else:
            newlines.append(line+ " "*(width-len(line)))

    # print lines in a box
    print(chars["tl"] + chars["hr"]*(width+2) +chars["tr"]) # print top of box
    for line in newlines:
        print(chars["vr"]+" " + line + " "+chars["vr"])
    print(chars["bl"] + chars["hr"]*(width+2) +chars["br"]) # print bottom of box