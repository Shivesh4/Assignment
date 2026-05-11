import sys
def rush(x, y):
    if x <= 0 or y <= 0:# Validate dimensions
        print("Invalid size", file=sys.stderr)
        return
    for row in range(y): #Row loop
        current_line = ""
        for col in range(x): #Column loop
            # Check if current position is a corner
            if ((row == 0 and col == 0) or (row == 0 and col == x - 1) or (row == y - 1 and col == 0) or (row == y - 1 and col == x - 1)):
                current_line += "o"
            # Top or bottom border
            elif row == 0 or row == y - 1:
                current_line += "-"
            # Left or right border
            elif col == 0 or col == x - 1:
                current_line += "|"
            # Inner empty space
            else:
                current_line += " "
        print(current_line)

rush(5,3)
rush(5,1)
rush(1,1)
rush(1,5)
rush(0,5) # Invalid case
rush(5,0) # Invalid case