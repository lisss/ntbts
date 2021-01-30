from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]):
        self.solved = False

        n = len(board)

        def get_box(x: int, y: int):
            return (x//3) * 3 + y // 3

        def is_allowed(num: int, row: int, col: int):
            is_in_row = rows[row][num]
            is_in_col = columns[col][num]
            is_in_box = boxes[get_box(row, col)][num]

            return not (is_in_row or is_in_col or is_in_box)

        def add_num(num, row, col):
            board[row][col] = str(num)
            rows[row][num] += 1
            columns[col][num] += 1
            boxes[get_box(row, col)][num] += 1

        def remove_num(num, row, col):
            board[row][col] = '.'
            rows[row][num] -= 1
            columns[col][num] -= 1
            boxes[get_box(row, col)][num] -= 1

        def move(row, col):
            if row == n - 1 and col == n - 1:
                self.solved = True
            else:
                if col == n - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row: int, col: int):
            if board[row][col] == '.':
                for num in range(1, 10):
                    if is_allowed(num, row, col):
                        add_num(num, row, col)
                        move(row, col)

                        if not self.solved:
                            remove_num(num, row, col)
            else:
                move(row, col)

        k = n + 1
        rows = [{i: 0 for i in range(1, k)} for _ in range(n)]
        columns = [{i: 0 for i in range(1, k)} for _ in range(n)]
        boxes = [{i: 0 for i in range(1, k)} for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    add_num(d, i, j)

        backtrack(0, 0)


s = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s.solveSudoku(board)
print(*board, sep='\n')
