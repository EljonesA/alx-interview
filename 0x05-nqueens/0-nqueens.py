#!/usr/bin/python3

"""
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.
"""

import sys


def is_valid(board, row, col):
    """ Check if it's valid to place a quen at board """
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """ Use backtracking to find all solutions """
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1


def print_solutions(solutions):
    """ Print all solutions in the required format """
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)


def main():
    """ Entry point """
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

    solutions = []
    board = [-1] * N
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
