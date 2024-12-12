# Prime Game

## Overview
Maria and Ben are playing a game called "Prime Game." The game involves a series of rounds where they take turns choosing prime numbers and removing them and their multiples from a set of integers. The player unable to make a move loses the round. This project implements a Python solution to determine the overall winner after multiple rounds.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3 (version 3.4.3).
- Files should end with a new line.
- The first line of all files must be exactly `#!/usr/bin/python3`.
- A `README.md` file is mandatory at the root of the project.
- Code must adhere to **PEP 8 style** (version 1.7.x).
- All files must be executable.

## Function Prototype

```python
isWinner(x, nums)
```

- **Arguments**:
  - `x`: The number of game rounds (integer).
  - `nums`: A list of integers representing the set size for each round.
- **Returns**:
  - The name of the player who won the most rounds (`"Maria"` or `"Ben"`).
  - `None` if there is no overall winner.

## Example

```python
x = 3
nums = [4, 5, 1]
print("Winner:", isWinner(x, nums))  # Output: "Winner: Ben"
```

### Explanation
1. **Round 1 (`n=4`)**: Ben wins.
2. **Round 2 (`n=5`)**: Maria wins.
3. **Round 3 (`n=1`)**: Ben wins.

Ben wins more rounds than Maria, so Ben is the overall winner.

## File Structure

```plaintext
.
├── 0-prime_game.py
├── main_0.py
├── README.md
```

- **`0-prime_game.py`**: Contains the implementation of the `isWinner` function.
- **`main_0.py`**: Sample script to test the function.
- **`README.md`**: This file, explaining the project.

## How to Run

1. Make the Python files executable:
   ```bash
   chmod +x 0-prime_game.py main_0.py
   ```

2. Run the test script:
   ```bash
   ./main_0.py
   ```

## Implementation Details

### Prime Calculation
The solution uses the **Sieve of Eratosthenes** to precompute all prime numbers up to the maximum value of `n` in the `nums` array. This ensures optimal performance by avoiding redundant calculations.

### Game Simulation
For each round:
- Maria and Ben take turns picking primes and removing their multiples from the set.
- The player unable to pick a prime loses the round.

### Optimized Logic
- Precompute prime numbers for the largest possible `n` to reduce runtime.
- Use a set to track remaining numbers efficiently during each round.

## Example Output

```bash
$ ./main_0.py
Winner: Ben
```

## Author
[Silas Edet](https://github.com/BrotherSilas)


