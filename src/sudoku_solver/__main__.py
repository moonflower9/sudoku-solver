from .sudoku import solve

board = [
    [0, 0, 8, 0, 0, 0, 0, 1, 6],
    [5, 0, 0, 0, 9, 2, 0, 0, 8],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [9, 0, 0, 3, 0, 0, 8, 2, 0],
    [0, 2, 0, 0, 0, 0, 0, 7, 0],
    [0, 8, 4, 0, 0, 6, 0, 0, 5],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [4, 0, 0, 9, 6, 0, 0, 0, 2],
    [1, 6, 0, 0, 0, 0, 7, 0, 0],
]


def main():
    if solve(board):
        print("\n".join(" ".join(map(str, row)) for row in board))
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
