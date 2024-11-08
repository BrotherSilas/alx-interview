#!/usr/bin/python3
"""
N Queens solver - places N non-attacking queens on an NxN chessboard
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be placed on board[row][col]

    Args:
        board: 2D array representing the board
        row: Row to check
        col: Column to check
        N: Size of the board

    Returns:
        Boolean indicating if the position is safe
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N Queens problem and return all solutions

    Args:
        N: Size of the board and number of queens

    Returns:
        List of solutions, where each solution is a list of queen positions
    """
    solutions = []
    board = [[0 for x in range(N)] for y in range(N)]

    def solve_util(board, col):
        # Base case: If all queens are placed, return True
        if col >= N:
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        # Consider this column and try placing this queen in all rows one by
        # one
        for i in range(N):
            if is_safe(board, i, col, N):
                # Place this queen in board[i][col]
                board[i][col] = 1

                # Recur to place rest of the queens
                solve_util(board, col + 1)

                # If placing queen in board[i][col] doesn't lead to a solution,
                # then remove queen from board[i][col]
                board[i][col] = 0

    solve_util(board, 0)
    return solutions


def main():
    """Main function to handle input and print solutions"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
