# 0x09. Island Perimeter

This project contains a Python function to calculate the perimeter of an island described in a grid.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style guide (version 1.7)
- No external modules

## Usage

To use the function, import `island_perimeter` from the `0-island_perimeter.py` file:

```python
from 0-island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12

