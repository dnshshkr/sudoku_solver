from ast import literal_eval
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, num, pos):
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # print(f'box_x: {box_x}, box_y: {box_y}')
    for i in range(box_y * 3, box_y * 3 + 3):
        # print(f'i: {i}')
        for j in range(box_x * 3, box_x * 3 + 3):
            # print(f'j: {j}')
            # print(f'board: {board[i][j]}, (i,j): {(i,j)}')
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(board):
    find = find_empty_location(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

board=[]
input_board=input('Input number, use "." to separate rows: ').split('.')
for row in input_board:
    board.append(literal_eval(f'[{",".join(_ for _ in row)}]'))
# print(board)

# board = [
#     [0,2,7,0,0,0,0,3,0],
#     [8,0,0,0,0,0,5,0,9],
#     [0,9,0,1,0,8,0,0,0],
#     [0,5,0,0,0,2,0,9,4],
#     [0,0,0,3,0,1,0,0,0],
#     [3,7,0,0,4,6,0,0,0],
#     [9,0,0,0,0,0,0,0,0],
#     [0,3,0,0,0,0,0,2,0],
#     [0,0,0,8,9,0,0,6,5]
# ]
try:
    print("Sudoku board to solve:")
    print_board(board)
except IndexError:
    print('Invalid board')
else:
    if solve_sudoku(board):
        print("\nSolution:")
        print_board(board)
    else:
        print("\nNo solution exists.")
