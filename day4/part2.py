import sys

def solve(path):
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
        # Check each neighbouring cell using the direction offsets
        neighbour_count = 0
        for row_offset, column_offset in directions:
            neighbour_row = row + row_offset
            neighbour_column = column + column_offset

            # Only count this neighbour if it is inside the grid and contains a roll
            if (
                0 <= neighbour_row < rows
                and 0 <= neighbour_column < cols
                and grid[neighbour_row][neighbour_column] == "@"
            ):
                neighbour_count += 1

        return neighbour_count


    # overall logic:
    # 1. use nested for loops to scan every cell in the grid.
    # 2. for each roll, check whether it has fewer than four neighbouring rolls.
    # 3. collect all such accessible rolls in a list for this round.
    # 4. remove all collected rolls at once.
    # 5. repeat the scan until no more rolls are removable.
    # repeat.
    total_removed = 0
    while True:
        to_remove = []
        # First pass: find all rolls that are currently accessible
        for row in range(rows):
            for column in range(cols):
                if grid[row][column] == "@" and adjacent_count(row, column) < 4:
                    to_remove.append((row, column))

        # stop when no more rolls can be removed
        if not to_remove:
            break

        # remove all rolls discovered in this round
        for row, column in to_remove:
            grid[row][column] = "."

        total_removed += len(to_remove)

    return total_removed

if __name__ == "__main__":
    print(solve("data.txt"))