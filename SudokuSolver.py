board = [
    [3, 0, 0, 7, 0, 0, 0, 0, 0],
    [1, 8, 6, 5, 0, 0, 7, 0, 0],
    [0, 0, 5, 0, 0, 2, 0, 0, 0],
    [9, 0, 7, 0, 4, 0, 0, 3, 0],
    [0, 0, 0, 3, 0, 7, 0, 0, 0],
    [0, 5, 0, 0, 2, 0, 8, 0, 4],
    [0, 0, 0, 9, 0, 0, 6, 0, 0],
    [0, 0, 2, 0, 0, 8, 9, 5, 3],
    [0, 0, 0, 0, 0, 3, 0, 0, 7]
]


def solve_Sudoku(bo):
    find = findEmpty(bo)
    if not find:
        return True
    row, col = find

    for i in range(1, 10):
        if right_Number(bo, i, (row, col)):
            bo[row][col] = i
            if solve_Sudoku(bo):
                return True

            bo[row][col] = 0

    return False


def right_Number(bo, num, position):
    for i in range(len(bo[0])):
        if bo[position[0]][i] == num and position[1] != i:
            return False

    for i in range(len(bo[0])):
        if bo[i][position[1]] == num and position[0] != i:
            return False

    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != position:
                return False

    return True


def printBo(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - -')

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end='')


def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row,col

    return None


print("Unsolved Board-")
printBo(board)
print("--------------------------------")
solve_Sudoku(board)
print("Solved Board-")
printBo(board)
