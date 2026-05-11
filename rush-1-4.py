import sys
def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return
    for row in range(y):
        current_line = ""
        for col in range(x):
            # Left-side corners
            if (row == 0 or row == y - 1) and col == 0:
                current_line += "A"
            # Right-side corners
            elif (row == 0 or row == y - 1) and col == x - 1:
                current_line += "C"
            # Borders
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                current_line += "B"
            # Inner area
            else:
                current_line += " "
        print(current_line)

# x = int(sys.argv[1])
# y = int(sys.argv[2])
# rush(x, y) 

