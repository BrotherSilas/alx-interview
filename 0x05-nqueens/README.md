# N Queens

## Overview
This project contains a solution to the N Queens puzzle, a classic problem in computer science and mathematics. The challenge is to place N non-attacking queens on an N×N chessboard, meaning that no two queens can share the same row, column, or diagonal.

## Background
The N Queens puzzle is a well-known example of a constraint satisfaction problem and is often used to demonstrate backtracking algorithms. The solution implemented here uses a backtracking approach to find all possible arrangements of queens that satisfy the non-attacking constraints.

## Features
- Solves the N Queens problem for any board size N ≥ 4
- Prints all possible solutions
- Implements proper error handling
- Follows Python best practices and PEP 8 style guidelines

## Requirements
- Ubuntu 20.04 LTS
- Python 3.4.3
- Allowed editors: vi, vim, emacs
- All files should be executable
- Code should use PEP 8 style (version 1.7.*)
- Only the `sys` module is allowed to be imported

## File Structure
- `0-nqueens.py`: Main program file containing the N Queens solver
- `README.md`: Documentation file (you're reading it!)

## Installation
Clone this repository:
```bash
git clone [repository-url]
cd 0x05-nqueens
```

Make the program executable:
```bash
chmod +x 0-nqueens.py
```

## Usage
Run the program with a single integer argument N:
```bash
./0-nqueens.py N
```

### Arguments
- N: An integer greater than or equal to 4 representing both the size of the chessboard and the number of queens to place

### Output Format
- Each solution is printed as a list of queen positions
- Each position is represented as [row, column]
- Solutions are printed one per line

### Example Usage
```bash
./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

### Error Cases
The program will exit with status code 1 and display an error message in the following cases:
1. Wrong number of arguments:
   ```bash
   Usage: nqueens N
   ```
2. N is not an integer:
   ```bash
   N must be a number
   ```
3. N is less than 4:
   ```bash
   N must be at least 4
   ```

## Algorithm
The solution uses a backtracking algorithm with the following approach:
1. Start in the leftmost column
2. If all queens are placed, return the solution
3. For each row in the current column:
   - If the queen can be placed safely, mark that position
   - Recursively check if placing the queen leads to a solution
   - If placing the queen doesn't lead to a solution, backtrack

## Time Complexity
- Time Complexity: O(N!)
- Space Complexity: O(N²)

## Author
Silas Edet

## License
This project is part of the ALX Software Engineering curriculum.
