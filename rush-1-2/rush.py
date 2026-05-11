import sys
def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return
    for row in range(y):
        current_line = ""
        for col in range(x):
            # Top-left corner
            if row == 0 and col == 0:
                current_line += "/"
            # Top-right corner
            elif row == 0 and col == x - 1:
                current_line += "\\"
            # Bottom-left corner
            elif row == y - 1 and col == 0:
                current_line += "\\"
            # Bottom-right corner
            elif row == y - 1 and col == x - 1:
                current_line += "/"
            # Borders
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                current_line += "*"
            # Inner space
            else:
                current_line += " "
        print(current_line)

# x = int(sys.argv[1])
# y = int(sys.argv[2])
# rush(x, y) 