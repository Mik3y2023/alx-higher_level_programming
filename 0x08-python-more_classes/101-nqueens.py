#!/usr/bin/python3
"""program that solves the N Queen problem"""


import sys


def init_board(n):
    """initializes chessboard"""
    board = []
    [board.append([]) for x in range(n)]
    [row.append(' ') for x in range(n) for row in board]
    return (board)


def board_deepcopy(new_board):
    """defines the deepcopy of the chessboard"""
    if isinstance(new_board, list):
        return list(map(board_deepcopy, new_board))
    return (new_board)


def get_solution(new_board):
    """return representation of solved board"""
    solution = []
    for j in range(len(new_board)):
        for k in range(len(new_board)):
            if new_board[j][k] == "Q":
                solution.append([j, k])
            break
    return (solution)


def xout(new_board, row, col):
    """define chessboard attributes"""
    # X out all forward spots
    for k in range(col + 1, len(new_board)):
        new_board[row][k] = "x"
    # X out all backward spots
    for k in range(col - 1, -1, -1):
        new_board[row][k] = "x"
    # X out all spots below
    for j in range(row + 1, len(new_board)):
        new_board[j][col] = "x"
    # X out all spots above
    for j in range(row - 1, -1, -1):
        new_board[j][col] = "x"
    # X out all spots diagonally down to the right
    k = col + 1
    for j in range(row + 1, len(new_board)):
        if k >= len(new_board):
            break
        new_board[j][k] = "x"
        k += 1
    #
    # X out all spots diagonally up to the left
    k = col - 1
    for j in range(row - 1, -1, -1):
        if k < 0:
            break
        new_board[j][k]
        k -= 1
    # X out all spots diagonally up to the right
    k = col + 1
    for j in range(row - 1, -1, -1):
        if k >= len(new_board):
            break
        new_board[j][k] = "x"
        k += 1
    # X out all spots diagonally down to the left
    k = col - 1
    for j in range(row + 1, len(new_board)):
        if k < 0:
            break
        new_board[j][k] = "x"
        k -= 1


def recursive_solve(new_board, row, queens, solutions):
    """Solves the puzzle recursively"""
    if queens == len(new_board):
        solutions.append(get_solution(new_board))
        return (solutions)

    for k in range(len(new_board)):
        if new_board[row][k] == " ":
            tmp_board = board_deepcopy(new_board)
            tmp_board[row][k] = "Q"
            xout(tmp_board, row, k)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    new_board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(new_board, 0, 0, [])
    for sol in solutions:
        print(sol)
