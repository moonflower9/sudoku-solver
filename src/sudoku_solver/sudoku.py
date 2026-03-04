Board = list[list[int]]


def is_valid(board: Board, row: int, col: int, num: int) -> bool:
    # row
    for c in range(9):
        if board[row][c] == num:
            return False

    # column
    for r in range(9):
        if board[r][col] == num:
            return False

    # box
    box_r = (row // 3) * 3
    box_c = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_r + i][box_c + j] == num:
                return False

    return True


def solve(board: Board) -> bool:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True
