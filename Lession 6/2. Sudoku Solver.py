# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
# hard = [[1,0,0,0,0,7,0,9,0],
#         [0,3,0,0,2,0,0,0,8],
#         [0,0,9,6,0,0,5,0,0],
#         [0,0,5,3,0,0,9,0,0],
#         [0,1,0,0,8,0,0,0,2],
#         [6,0,0,0,0,4,0,0,0],
#         [3,0,0,0,0,0,0,1,0],
#         [0,4,0,0,0,0,0,0,7],
#         [0,0,7,0,0,0,3,0,0]]

def check_sudoku(grid):
    num_elements_sudoku = 9
    
    num_row = len(grid)
    if num_row != num_elements_sudoku:
        return None
    for i in range( 0, num_elements_sudoku ):
        num_col = len(grid[i])
        if num_col != num_elements_sudoku:
            return None
        valid_sudoku = {}
        for j in range(0,  num_elements_sudoku ):
            val = grid[i][j]
            if (val < 1 or val > 9) and val != 0:
                return None
            if val != 0 and val in valid_sudoku:
                return False
            valid_sudoku[val] = 0
            
    for i in range( 0, num_elements_sudoku ):
        valid_sudoku = {}
        for j in range(0,  num_elements_sudoku ):
            val = grid[j][i]
            if val != 0 and val in valid_sudoku:
                return False
            valid_sudoku[val] = 0       
                      
    num_grid = 9
	grid_edge = 3
    for idx_grid in range( 0, num_grid ):
        valid_sudoku = {}
        
        row = ( idx_grid % grid_edge ) * grid_edge
        col = ( idx_grid / grid_edge ) * grid_edge
        
        for i in range( 0 , grid_edge ):
            for j in range( 0 , grid_edge ):
                val = grid[row + i][col + j]
                if val != 0 and val in valid_sudoku:
                    return False
                valid_sudoku[val] = 0
    
    return True
    pass

import copy;
import sys;

def solve_sudoku (_grid):
    res = check_sudoku(_grid)
    if res is None or res is False:
        return res
        
    grid = copy.deepcopy(_grid)
    
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                for n in range(1,10):
                    grid[row][col] = n
                    new = solve_sudoku(grid)
                    if new is not False:
                        return new
                return False
    return grid    
    pass 

solve_sudoku(easy)