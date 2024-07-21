def isSafe(board, row, col):
    # Vertical up 
    for i in range(row - 1, -1, -1):
        if board[i][col] == 'Q':
            return False

    # Diagonal left up 
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Diagonal right up 
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def nQueens(board, row):
    # Base Case 
    if row == len(board):
        print("---------Board--------- ")
        for r in board:
            print(' '.join(r))
        print()
        return

    # Column Loop 
    for j in range(len(board)):
        if isSafe(board, row, j):
            board[row][j] = 'Q'
            nQueens(board, row + 1)  # Function Call 
            board[row][j] = 'X'  # Backtracking

n = 4
board = [['X' for _ in range(n)] for _ in range(n)]  # N x N Board
nQueens(board, 0)
