# A FUNCTION THAT ACCEPTS A DICTIONARY OF THE NOTATION VALUES
# THIS DICTIONARY IS CONVERTED TO A STRING FORMAT
# THIS IS DONE BECAUSE THE SUDOKUALGO PROGRAM IS ABLE TO CALCULATE THE SUDOKU SOLUTION
# ONLY IF THE INPUT 
def convToString(grid):
	# grid is the input dictionary
	global notation_list
	grid_str = "" # stores the final string to be returned
	for square in notation_list:
		# Find the value corresponding to the notations
		val = grid[square]
		if val == 0:
			grid_str = grid_str + "." # append dot for empty value
		else:
			grid_str = grid_str + str(val)
	return grid_str


rows = 'ABCDEFGHI'
cols = '123456789'
notation_list = [r+c for r in rows for c in cols]
