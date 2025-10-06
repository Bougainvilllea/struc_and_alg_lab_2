def solve_sudoku(matrix):
    if not find_empty(matrix):
        return True
    
    row, col = find_empty(matrix)
    
    for num in range(1, 5):
        if is_valid(matrix, row, col, num):
            matrix[row][col] = num
            
            if solve_sudoku(matrix):
                return True
            
            matrix[row][col] = 0
    
    return False

def find_empty(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return i, j
    return None  

def is_valid(matrix, row, col, num):
    for j in range(4):
        if matrix[row][j] == num:
            return False
    
    for i in range(4):
        if matrix[i][col] == num:
            return False
    
    start_row = 2 * (row // 2)
    start_col = 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if matrix[i][j] == num:
                return False
    
    return True

if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 0, 0],
        [3, 0, 0, 4]
    ]
    
    if solve_sudoku(sudoku):
        for row in sudoku:
            print(''.join(map(str, row)))
    else:
        print("Решение не найдено")