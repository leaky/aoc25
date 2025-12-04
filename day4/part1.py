import sys

# solve the puzzle by scanning the grid and counting all rolls that have
# fewer than four neighbouring rolls around them.
def solve(path):
    # read the input file and turn each nonempty line into a list of characters
    with open(path) as f:
        grid = [list(line.strip()) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    # offsets for all eight surrounding neighbours in the grid
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def adjacent_count(row, column):
        # check each neighbouring cell using the direction offsets
        neighbour_count = 0
        for row_offset, column_offset in directions:
            neighbour_row = row + row_offset
            neighbour_column = column + column_offset

            # only count this neighbour if it is inside the grid and contains a roll
            if (
                0 <= neighbour_row < rows
                and 0 <= neighbour_column < cols
                and grid[neighbour_row][neighbour_column] == "@"
            ):
                neighbour_count += 1

        return neighbour_count

    accessible = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "@":
                neighbours = adjacent_count(row, col)
                if neighbours < 4:
                    accessible += 1

    return accessible

if __name__ == "__main__":
    print(solve("data.txt"))