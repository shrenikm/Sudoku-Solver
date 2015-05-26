# A MODULE TO WORK WITH THE GRIDS.
# IT PERFORMS NECESSARY GRID CALCULATIONS AND ALSO HAS FUNCTIONS TO HELP IN 
# GRID NOTATIONS

def defaultColor():
	# takes the notation and makes a dictionary out of it.
	# A value of 1 means default color - pale yellow
	# A value of 2 means number entered color - green
	# A value of 3 means mouse hover color - orange
	# A value of 4 means a darker yellow - for color separation of 3*3 units

	# This function gives everything a value of 1 by default
	coldict = {}
	for square in notation_list:
		x = square[0]
		y = square[1]
		if x in 'ABC' and y in '456':
			coldict[square] = 1
		elif x in 'DEF' and y in '123':
			coldict[square] = 1
		elif x in 'DEF' and y in '789':
			coldict[square] = 1
		elif x in 'GHI' and y in '456':
			coldict[square] = 1
		else:
			coldict[square] = 4
	return coldict




def refreshHoverColor(square_dict):
	# At the begining of every cycle, we need to remove all the previous hover colors
	# thus if any of the values is 3, we make it the previous base dual color.
	# This function is called at the begining of the application loop
	# we need to check the position of the square to give it one of the dual colors

	for square in square_dict.keys():
		x = square[0]
		y = square[1]
		if x in 'ABC' and y in '456':
			if square_dict[square] == 3:
				square_dict[square] = 1
		elif x in 'DEF' and y in '123':
			if square_dict[square] == 3:
				square_dict[square] = 1
		elif x in 'DEF' and y in '789':
			if square_dict[square] == 3:
				square_dict[square] = 1
		elif x in 'GHI' and y in '456':
			if square_dict[square] == 3:
				square_dict[square] = 1
		else:
			if square_dict[square] == 3:
				square_dict[square] = 4

	return square_dict

def calcPos(st):
	# calculates the grid position of the square. Returns a list of [x,y,w,h]
	x = 140+(47*(int(st[1])-1)) # A1 will have x coordinate of 140. Refer the gui code
	y = 55+(47*(abs(ord('A')-ord(st[0])))) # B1 will have y coord of 50+47
	w = 45
	h = 45
	return [x,y,w,h]

def squarePos():
	return dict([(square,calcPos(square)) for square in notation_list])
	

rows = 'ABCDEFGHI'
cols = '123456789'
notation_list = [r+c for r in rows for c in cols]


