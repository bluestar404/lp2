def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_util(board, row, N):
    if row >= N:
        return True
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, N):
                return True
            board[row][col] = 0
    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return False
    print("Solution exists. Here's the board:")
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    return True

n = 4
solve_n_queens(n)




#--------------------------------------- Branch and Bound----------------------------------------------------#




def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_util(board, row, n, result):
    if row == n:
        result.append([row[:] for row in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, result)
            board[row][col] = 0

def solve_n_queens(n):
    result = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board, 0, n, result)
    return result

n = 4
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens problem: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(' '.join(['Q' if col == 1 else '.' for col in row]))
    print()
