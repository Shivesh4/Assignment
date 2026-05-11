import sys
def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return
    for row in range(y):
        current_line = ""
        for col in range(x):
            # Top-left and top-right corners
            if row == 0 and (col == 0 or col == x - 1):
                current_line += "A"
            # Bottom-left and bottom-right corners
            elif row == y - 1 and (col == 0 or col == x - 1):
                current_line += "C"
            # Borders
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                current_line += "B"
            # Inner spaces
            else:
                current_line += " "
        print(current_line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 rush-1-3.py <x> <y>")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        rush(x, y)

        