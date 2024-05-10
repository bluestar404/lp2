# Global variable to keep track of the number of moves
g = 0  

# Function to print the current state of the board
def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()  # Print newline after every third element
        if elements[i] == -1:
            print("_", end=" ")  # Print underscore for empty tile
        else:
            print(elements[i], end=" ")  # Print the number for non-empty tile
    print()  # Print newline after printing the board

# Function to check if the puzzle is solvable
def solvable(start):
    inv = 0

    for i in range(9):
        if start[i] <= 1:  # Skip empty tile (-1)
            continue
        for j in range(i + 1, 9):
            if start[j] == -1:  # Skip empty tile (-1)
                continue
            if start[i] > start[j]:  # Count inversions
                inv += 1
    if inv % 2 == 0:  # If the number of inversions is even, puzzle is solvable
        return True
    return False

# Function to calculate the heuristic value (Manhattan distance) between current and goal state
def heuristic(start, goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:  # Calculate Manhattan distance
                h += (abs(j - i)) // 3 + (abs(j - i)) % 3
    return h + g  # Add the current move count to the heuristic value

# Functions to perform tile movements
def moveleft(start, position):
    start[position], start[position - 1] = start[position - 1], start[position]

def moveright(start, position):
    start[position], start[position + 1] = start[position + 1], start[position]

def moveup(start, position):
    start[position], start[position - 3] = start[position - 3], start[position]

def movedown(start, position):
    start[position], start[position + 3] = start[position + 3], start[position]

# Function to select the best move based on heuristic value and perform the move
def movetile(start, goal):
    emptyat = start.index(-1)  # Find the index of the empty tile
    row = emptyat // 3  # Calculate the row of the empty tile
    col = emptyat % 3  # Calculate the column of the empty tile
    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]  # Create temporary states for potential moves
    f1, f2, f3, f4 = 100, 100, 100, 100  # Initialize heuristic values for potential moves

    # Check if moving left is valid and calculate heuristic value for left move
    if col - 1 >= 0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)

    # Check if moving right is valid and calculate heuristic value for right move
    if col + 1 < 3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)

    # Check if moving down is valid and calculate heuristic value for down move
    if row + 1 < 3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)

    # Check if moving up is valid and calculate heuristic value for up move
    if row - 1 >= 0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2, f3, f4)  # Find the minimum heuristic value among potential moves

    # Perform the move corresponding to the minimum heuristic value
    if f1 == min_heuristic:
        moveleft(start, emptyat)
    elif f2 == min_heuristic:
        moveright(start, emptyat)
    elif f3 == min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)

# Function to recursively solve the 8-puzzle using A* algorithm
def solveEight(start, goal):
    global g
    g += 1  # Increment the move count
    movetile(start, goal)  # Perform the best move based on heuristic
    print_board(start)  # Print the current state of the board
    f = heuristic(start, goal)  # Calculate the heuristic value for the current state
    if f == g:  # If the heuristic value equals the move count, the goal is reached
        return
    solveEight(start, goal)  # Recursively call solveEight function

# Main function to get user input and start the solving process
def main():
    global g
    start = list()
    goal = list()
    print("Enter the start state:(Enter -1 for empty):")
    for i in range(9):
        start.append(int(input()))

    print("Enter the goal state:(Enter -1 for empty):")
    for i in range(9):
        goal.append(int(input()))

    print_board(start)  # Print the initial state of the board

    # Check if the start state is solvable
    if solvable(start):
        solveEight(start, goal)  # Start solving the puzzle
        print("Solved in {} moves".format(g))  # Print the number of moves taken to solve
    else:
        print("Not possible to solve")  # Print if the puzzle is not solvable

# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()



# Test Cases

# 1
# 2
# 3
# -1
# 4 
# 6
# 7 
# 5 
# 8 

# 1 
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8
# -1