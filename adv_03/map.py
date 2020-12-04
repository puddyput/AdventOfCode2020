
def slide(lines, right, down):
    width = len(lines[0])
    z_pos = 0
    x_pos = 0
    trees = 0
    while z_pos < len(lines):
        dbg_line = lines[z_pos][:x_pos]
        if lines[z_pos][x_pos] == "#":
            trees += 1
            dbg_line += "X"
        else:
            dbg_line += "O"
        dbg_line += lines[z_pos][x_pos + 1:]
        #print(dbg_line)
        z_pos += down
        x_pos = (x_pos + right) % width

    print("Right {} Down {}: {}".format(right, down, trees))


with open("input.txt") as file:
    lines = file.read().splitlines()
    slide(lines, 1, 1)
    slide(lines, 3, 1)
    slide(lines, 5, 1)
    slide(lines, 7, 1)
    slide(lines, 1, 2)
