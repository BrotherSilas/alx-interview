#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A 2D list representing the grid.

    Returns:
        int: The perimeter of the island.
    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Found land
                # Check all four directions
                # Check up
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check down
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
