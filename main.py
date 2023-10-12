import sys

grid = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 0, 1, 2, 3, 4, 5, 6],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 0]
]

def solve_sudoku(grid, choice):
    empty_cells = find_empty(grid)
    if not empty_cells:
        return True
    if choice == "backtrack":
        row, col = empty_cells[0]
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            print("\nIteration:")
            print_sudoku_grid(grid)
            if solve_sudoku(grid, choice):
                return True
            grid[row][col] = 0
    return False

def backtrack_sudoku_solver(grid):
    print("Using Backtracking Solver")
    print("Initial Sudoku Grid:")
    print_sudoku_grid(grid)
    if solve_sudoku(grid, "backtrack"):
        print("\nSudoku Solved")
        print_sudoku_grid(grid)
    else:
        print("\nNo solution found")

def is_valid(grid, num, pos):
    row, col = pos
    for i in range(9):
        if grid[i][col] == num or grid[row][i] == num:
            return False
    row_start, col_start = 3 * (row // 3), 3 * (col // 3)
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if grid[i][j] == num:
                return False
    return True

def print_sudoku_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(grid[i][j], end=" ")

def find_empty(grid):
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells

def main():
    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py [backtrack|bruteforce]")
        return

    choice = sys.argv[1]

    if choice == "backtrack":
        backtrack_sudoku_solver(grid)
    else:
        print("Invalid choice. Use 'backtrack' or 'bruteforce'.")

if __name__ == "__main__":
    main()
