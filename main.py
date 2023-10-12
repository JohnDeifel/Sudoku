import sys
import copy 

grid = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 0, 0, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
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

def brute_force_sudoku_solver(grid, row=0, col=0):
    if row == 9:
        if is_solved(grid):  
            return True

    next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)

    if grid[row][col] == 0:
        for num in range(1, 10):
            newgrid = copy.deepcopy(grid)
            newgrid[row][col] = num

            print("\nIteration:")
            print_sudoku_grid(newgrid)
            
            if is_valid(grid, num, (row, col)):
                grid[row][col] = num

                print("\nValid Iteration:")
                print_sudoku_grid(grid)  

                if brute_force_sudoku_solver(grid, next_row, next_col):
                    return True
                break

    elif brute_force_sudoku_solver(grid, next_row, next_col):
        return True

    grid[row][col] = 0
    return False



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

def is_solved(grid):
    for row in grid:
        if 0 in row:
            return False

    for col in range(9):
        col_values = [grid[row][col] for row in range(9)]
        if len(set(col_values)) != 9:
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box_values = []
            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    box_values.append(grid[row][col])
            if len(set(box_values)) != 9:
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
    elif choice == "bruteforce":
        print("Using Brute Force Solver")
        print("Initial Sudoku Grid:")
        print_sudoku_grid(grid)
        if brute_force_sudoku_solver(grid):
            print("\nSudoku Solved")
            print_sudoku_grid(grid)
        else:
            print("\nNo solution found")
    else:
        print("Invalid choice. Use 'backtrack' or 'bruteforce'.")

if __name__ == "__main__":
    main()
