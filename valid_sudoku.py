from collections import defaultdict

def isValidSudoku(board):
    cols = defaultdict(set) # for column
    rows = defaultdict(set) # for row 
    squares = defaultdict(set) # for the 3*3 box 

    for r in range(9): 
        for c in range(9):
            if board[r][c] == '.':  # "." found , just continue
                continue
            
            if (board[r][c] in rows[r] # this check whether there is same number in row,column or in 3*3 box
                or board[r][c] in cols[c] 
                or board[r][c] in squares[(r // 3, c // 3)]):
                return False

            cols[c].add(board[r][c]) # if the number is not found it return it add to the sudoku 
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c]) 
    
    return True

# Add your input here
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "5", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

result = isValidSudoku(board)
print(result)
