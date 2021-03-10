from numpy import array, zeros, matrix

puzzle = array(
		 [[5,3,0,0,7,0,0,0,0],  
		  [6,0,0,1,9,5,0,0,0],  
		  [0,9,8,0,0,0,0,6,0],  
		  [8,0,0,0,6,0,0,0,3],
		  [4,0,0,8,0,3,0,0,1],
		  [7,0,0,0,2,0,0,0,6],
		  [0,6,0,0,0,0,2,8,0],
		  [0,0,0,4,1,9,0,0,5],
		  [0,0,0,0,8,0,0,7,0]])


def box(grid, x, y):
	return grid[3*(x//3): 3*(x//3) +3, 3*(y//3): 3*(y//3) +3]
			
def possible(grid, x, y, n):
	return True if (n not in grid[x] and n not in grid[:,y] and n not in box(grid, x, y)) else False

def sudoku(grid):
	for i in range(9):
		for j in range(9):
			if not(grid[i, j]): 
				for n in range(1, 10):
					if possible(grid, i, j, n):
						grid[i, j] = n
						sudoku(grid)
						grid[i, j] = 0
				return
	print(grid)

print(puzzle)
sudoku(puzzle)