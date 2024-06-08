def reverse_list(l: list):
    """
    Reverse a list without using any built-in functions.

    The function should return a sorted list.
    Input l is a list which can contain any type of data.
    """
    reversed_list = []
    for item in l:
        reversed_list.insert(0, item)
    
    # Sort the reversed list
    sorted_list = sorted(reversed_list)
    
    return sorted_list

def is_valid_move(matrix, row, col, num):
    # Check if the number is already in the row
    if num in matrix[row]:
        return False
    
    # Check if the number is already in the column
    if num in [matrix[i][col] for i in range(9)]:
        return False
    
    # Check if the number is already in the 3x3 subgrid
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if matrix[i][j] == num:
                return False
    
    return True

def solve_sudoku(matrix):
    empty_cell = find_empty_cell(matrix)
    if not empty_cell:
        return True  # All cells filled, puzzle solved
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(matrix, row, col, num):
            matrix[row][col] = num
            if solve_sudoku(matrix):
                return True
            matrix[row][col] = 0  # Backtrack
    return False  # No valid number found for this cell

def find_empty_cell(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                return (i, j)
    return None  # No empty cell found, puzzle solved

if __name__ == "__main__":
    # sorted_list = reverse_list([2, 4, 3, 1, 6])
    # print(sorted_list)

    sudoku = [
        [5, 3, 0, 0, 7, 0, 9, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(sudoku):
        print("Sudoku puzzle solved:")
        for row in sudoku:
            print(row)
    else:
        print("No solution found for the Sudoku puzzle.")