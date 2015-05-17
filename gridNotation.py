def defaultColor():
	# takes the notation and makes a dictionary out of it.
	# A value of 1 means default color - pale yellow
	# A value of 2 means number entered color - green
	# A value of 3 means mouse hover color - orange

	# This function gives everything a value of 1 by default
	return dict([(square, 1) for square in notation_list])

def refreshHoverColor(square_dict):
	# At the begining of every cycle, we need to remove all the previous hover colors
	# thus if any of the values is 2, we make it one.
	# This function is called at the begining of the application loop
	for square in square_dict.keys():
		if square_dict[square] == 2:
			square_dict[square] = 1
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


