#!/usr/bin/python3
''' island perimeter challenge '''


def island_perimeter(grid):
    '''
    Calculate the perimeter of the island described in the grid.

    Args: Grid - A 2D list representing the grid where:
                - 0 represents water.
                - 1 represents land.

    Returns: The perimeter of the island.
    '''
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check each side of the cell
                if i == 0 or grid[i-1][j] == 0:  # Top side
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:  # Bottom side
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left side
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:  # Right side
                    perimeter += 1

    return perimeter
