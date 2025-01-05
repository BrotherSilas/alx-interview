# 0x08. Making Change

## Description
This project focuses on solving the problem of determining the fewest number of coins needed to meet a given amount total. It includes a single task where you implement a Python function to achieve this goal. The solution must meet specific runtime requirements and adhere to coding standards.

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code must follow the **PEP 8 style** (version 1.7.x)
- All files must be executable

## Tasks

### 0. Change comes from within
**Mandatory**

Write a function `makeChange(coins, total)` that determines the fewest number of coins needed to meet a given amount total.

#### Prototype:
```python
def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount total."""

Requirements:
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
Assume you have an infinite number of each denomination of coin in the list

Example:
python
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7

print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1

Evaluation
Your solution’s runtime will be evaluated.

Repository
GitHub repository: alx-interview
Directory: 0x08-making_change
File: 0-making_change.py
Author
Silas Edet - https://github.com/BrotherSilas
