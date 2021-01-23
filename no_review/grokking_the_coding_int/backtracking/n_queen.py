n = 5


def place_queen(row, col, rows, hills, dales):
    rows[col] = 1
    hills[row - col] = 1
    dales[row + col] = 1


def remove_queen(row, col, rows, hills, dales):
    rows[col] = 0
    hills[row - col] = 0
    dales[row + col] = 0


def is_not_under_attack(row, col, rows, hills, dales):
    return not (rows[col] or hills[row - col] or dales[row + col])


def backtrack(row, count, rows, hills, dales):
    for col in range(n):
        # iterate through columns at the curent row.
        if is_not_under_attack(row, col, rows, hills, dales):
            # explore this partial candidate solution, and mark the attacking zone
            place_queen(row, col, rows, hills, dales)
            if row + 1 == n:
                # we reach the bottom, i.e. we find a solution!
                count += 1
            else:
                # we move on to the next row
                count = backtrack(row + 1, count, rows, hills, dales)
            # backtrack, i.e. remove the queen and remove the attacking zone.
            remove_queen(row, col, rows, hills, dales)
    return count


def place_nqueen():
    rows = [0 for _ in range(n)]
    hills = [0 for _ in range(n * 2 - 1)]
    dales = [0 for _ in range(n * 2 - 1)]

    return backtrack(0, 0, rows, hills, dales)


print(place_nqueen())
