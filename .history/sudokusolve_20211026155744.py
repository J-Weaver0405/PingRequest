import string
import random

#horizontal check
# vertical check 
# mini square check (6 blocks)

input_str = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"

grid = []
line = []

def line_to_grid(values):
    grid = []
    line = []
    for index, char in enumerate(values):
        if index and index % 9 == 0:
            grid.append(line)
            line = []
        line.append(int(char))

    grid.append(line)
    return grid