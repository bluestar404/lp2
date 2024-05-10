def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:  # If there is a queen in the same column, return False
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:  # If there is a queen on the upper left diagonal, return False
            return False
    
    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:  # If there is a queen on the upper right diagonal, return False
            return False
    
    return True  # If no queen is attacking the current position, return True

def solve_n_queens_util(board, row, N):
    if row >= N:
        return True  # If all queens are placed (base case), return True
    
    for col in range(N):
        if is_safe(board, row, col, N):  # If it's safe to place a queen in this position
            board[row][col] = 1  # Place the queen
            
            # Recur to place the remaining queens
            if solve_n_queens_util(board, row + 1, N):
                return True  # If a solution is found, return True
            
            board[row][col] = 0  # Backtrack: Remove the queen if no solution is found
    
    return False  # If no solution is found, return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]  # Initialize the chessboard with all 0s (empty squares)
    
    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")  # If no solution exists, print a message
        return False
    
    print("Solution exists. Here's the board:")  # If a solution exists, print the board
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")  # Print the board
        print()
    return True

# Example usage
n = 4
solve_n_queens(n)





#--------------------------Branch and bound-----------------------------------------------------------







# Function to check if placing a queen at position (row, col) on the board is safe
def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


# Function to recursively solve the N Queens problem
def solve_n_queens_util(board, row, n, result):
    # Base case: If all queens are placed, append the current board configuration to the result
    if row == n:
        result.append([row[:] for row in board])
        return

    # Try placing queen in each column of the current row
    for col in range(n):
        # Check if it's safe to place a queen at this position
        if is_safe(board, row, col, n):
            # Place the queen at this position
            board[row][col] = 1
            # Recursively solve for the next row
            solve_n_queens_util(board, row + 1, n, result)
            # Backtrack: Remove the queen from this position for exploring other possibilities
            board[row][col] = 0


# Function to solve the N Queens problem and return all solutions
def solve_n_queens(n):
    result = []  # List to store all solutions
    # Create an empty chessboard of size n x n
    board = [[0 for _ in range(n)] for _ in range(n)]
    # Start the recursive process to solve the problem
    solve_n_queens_util(board, 0, n, result)
    return result


# Example usage:
n = 4
# Solve the N Queens problem for n = 4
solutions = solve_n_queens(n)
# Print the total number of solutions
print(f"Total solutions for {n}-Queens problem: {len(solutions)}")
# Print each solution
for solution in solutions:
    for row in solution:
        # Print each row of the board, replacing 1 with 'Q' and 0 with '.'
        print(' '.join(['Q' if col == 1 else '.' for col in row]))
    print()  # Empty line between solutions
