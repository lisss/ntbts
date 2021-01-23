from typing import List

n = 5


def is_safe(x: int, y: int, board: List[List[int]]):
    return x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1


def print_solution(board: List[List[int]]):
    for row in board:
        print(*row)


def _do(x: int, y: int, board: List[List[int]], x_move: int, y_move: int, pos: int):
    if pos == n ** 2:
        return True

    for i in range(8):
        new_x = x + x_move[i]
        new_y = y + y_move[i]

        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = pos
            if _do(new_x, new_y, board, x_move, y_move, pos + 1):
                return True
            board[new_x][new_y] = -1
    return False


def knight_problem():
    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[0][0] = 0

    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    if not _do(0, 0, board, x_move, y_move, 1):
        print('No solution')
    else:
        print_solution(board)


knight_problem()
