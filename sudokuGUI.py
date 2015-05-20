import pygame
import os
import sudokuGridNotation as gn
import sudokuAlgo as alg 
import sudokuConv as conv 

# Centering the window -------------------------------------------------------------
os.environ['SDL_VIDEO_CENTERED'] = '1'
# Main applications code begins ----------------------------------------------------


# Variable declarations and initializations ----------------------------------------
# defining colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
APP_BACKGROUND = (200, 255, 255)
GRID_BASE = (190,190,190)
GRID_BASE_SHADE_HIGH = (100,100,100)
GRID_BASE_SHADE_MED = (150,150,150)
SQUARE_DEFAULT = (255,217,92)
SQUARE_DEFAULT_DARKER = (255,240,150)
SQUARE_FILLED = (89,181,36)
SQUARE_HOVER = (252, 179, 43)
OPTIONS_TEXT = (30,50,40)
OPTIONS_CIRCLE = (124,162,252)
NUMBER = (10,20,30)
BUTTON = (227,84,84)
BUTTON_CLICK = (255, 20, 20)
NUMBER_SOLUTION = (200,50,20)

# mouse coordinates
mousex = mousey = -1



# application variables ------------------------------------------------------------
# dictionary for list of square notations
square_notation = gn.notation_list

# dictionary for colors for the squares
square_color_number = gn.defaultColor() # gives default color to all squares

# dictionary for actual colors
square_color = {}

# dictionary for the position values of each square. In the form of [x,y,w,h]
square_pos = gn.squarePos()

# dictionary that stores all user entered numbers
square_user_values = dict([(sq, 0) for sq in square_notation])

# dictionary that stores the pygame string representations of square_user_values
square_user_values_text = {}

# dictionary that stores the solution
square_solution_values = {}

# dictionary that stores the pygame string representations of square_solution_values
square_solution_values_text = {}

# dictionary of rectangles. pygame.Rect(x,y,w,h)
square_rect = dict([(square, pygame.Rect(square_pos[square][0], square_pos[square][1], 45, 45)) for square in square_pos])

# The rectangle for the whole grid
grid_rect = pygame.Rect(135, 50, 431, 431)

# Rectangles for the 3 buttons
# These represent 3 buttons
# The solve button solves the Sudoku and displays the result
# The reset button resets the current sudoku, retaining the user entered values
# The clear button clears the whole sudoku.
solve_rect = pygame.Rect(288, 510, 125, 50)
reset_rect = pygame.Rect(138, 510, 125, 50)
clear_rect = pygame.Rect(438, 510, 125, 50)

# stores the current number selected in the options menu
number_selected = -1

# stores the last selected square
last_selected_square = ''




mouseCollideSquare = False
mouseClick = False
drawOptionsMenu = False
selectDrawOptions = False
# to set when solve button is clicked
solveGrid = False 
# Print error message if solution is wrong
error_print = False

# checking for button hover
solveClick = False
clearClick = False
resetClick = False





# Game functions-------------------------------------------------------------------

# Initialize everything to default, for clearing, etc.
def initClear():
	global square_notation
	global square_user_values
	global square_user_values_text
	global square_solution_values
	global square_solution_values_text
	global square_color_number
	square_user_values = dict([sq, 0] for sq in square_notation)
	square_user_values_text = {}
	square_solution_values = {}
	square_solution_values_text = {}
	square_color_number = gn.defaultColor()

def initReset():
	global square_solution_values
	global square_solution_values_text
	square_solution_values = {}
	square_solution_values_text = {}


def calcSquareColor():
	# Makes a dictionary with colors for the squares using square_color_number
	global square_notation
	global square_color_number
	global square_color
	for square in square_notation:
		if square_color_number[square] == 1:
			square_color[square] = SQUARE_DEFAULT # pale yellow
		elif square_color_number[square] == 2:
			square_color[square] = SQUARE_FILLED # green
		elif square_color_number[square] == 3:
			square_color[square] = SQUARE_HOVER # orange
		elif square_color_number[square] == 4:
			square_color[square] = SQUARE_DEFAULT_DARKER # dual base color
		else:
			pass

# function that checks if the mouse hovers over any of the options
def optionHover():
	global number_selected
	ishovering = False
	for i in xrange(10):

		# using equation of circle
		dst = ((mousex-625.0)**2 + (mousey-(65+45*i))**2)**0.5
		if dst<=20:
			number_selected = i
			ishovering = True
			break
	if not ishovering:
		number_selected = -1

# Makes the square_user_values to a set of pygame texts to blit
def makeNumberText():
	global square_notation
	global square_user_values
	global square_user_values_text
	for square in square_notation:
		# If it is a zero, keep the dict value as 0
		# else convert to text
		if square_user_values[square] == 0:
			square_user_values_text[square] = 0
		else:
			square_user_values_text[square] = number_font.render(str(square_user_values[square]), True, NUMBER)

# Converts the solution dictionary to a pygame text dictionary
def makeNumberSolutionText():
	global square_notation
	global square_solution_values
	global square_solution_values_text
	for square in square_notation:
		square_solution_values_text[square] = number_font.render(str(square_solution_values[square]), True, NUMBER_SOLUTION)


# set proper dual color
def setDualColor():
	global square_notation
	global square_color_number
	for square in square_notation:
		x = square[0]
		y = square[1]
		if x in 'ABC' and y in '456':
			square_color_number[last_selected_square] = 1
		elif x in 'DEF' and y in '123':
			square_color_number[last_selected_square] = 1
		elif x in 'DEF' and y in '789':
			square_color_number[last_selected_square] = 1
		elif x in 'GHI' and y in '456':
			square_color_number[last_selected_square] = 1
		else:
			square_color_number[last_selected_square] = 4

# set dual color for a single square
def setDualColorSquare(sq):
	x = sq[0]
	y = sq[1]
	if x in 'ABC' and y in '456':
		square_color_number[sq] = 1
	elif x in 'DEF' and y in '123':
		square_color_number[sq] = 1
	elif x in 'DEF' and y in '789':
		square_color_number[sq] = 1
	elif x in 'GHI' and y in '456':
		square_color_number[sq] = 1
	else:
		square_color_number[sq] = 4

# checks if the user entered values are empty
def isUserValuesEmpty():
	global square_user_values
	global square_notation
	c = 0 # count for zeroes

	for square in square_notation:
		if square_user_values[square] == 0:
			c+=1
	if c==81:
		return True # user has not entered anything
	else:
		return False









# pygame initializations -----------------------------------------------------------
# size of the screen
size = [700, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku Solver")

pygame.init()

# font initialization
options_font = pygame.font.SysFont("comicsansms", 16)
number_font = pygame.font.SysFont("comicsansms", 18)
button_font = pygame.font.SysFont("courier", 28, 1)

# text creation using the fonts
options_text = [options_font.render(str(i), True, OPTIONS_TEXT) for i in xrange(0,10)]
solve_text = button_font.render("SOLVE", True, WHITE)
reset_text = button_font.render("RESET", True, WHITE)
clear_text = button_font.render("CLEAR", True, WHITE)

number_text = {}

app_done = False # variable to stop the application loop
clock = pygame.time.Clock() # managing screen update time





# All the drawing functions---------------------------------------------------------

# The main draw function that is called. It calls all the other drawing functions
def main_draw(screen):
	screen.fill(APP_BACKGROUND)
	draw_grid(screen)
	draw_square_color(screen)
	if drawOptionsMenu:
		# draw options
		draw_options(screen)
	draw_user_numbers(screen)
	draw_buttons(screen)
	# if solve is clicked, display the solution
	if solveGrid:
		draw_solution(screen)
	# print error message if invalid user values
	if error_print:
		draw_error(screen)

# Draws the sudoku grid
def draw_grid(screen):
	# Drawing the outer thick square. 
	# It is made of rectangles with 3 shades
	pygame.draw.rect(screen, GRID_BASE, [135, 50, 5, 431]) # left base shade
	pygame.draw.rect(screen, GRID_BASE_SHADE_HIGH, [135, 50, 2, 431] ) # left high shade
	pygame.draw.rect(screen, GRID_BASE_SHADE_MED, [137, 50, 1, 431] ) # left med shade

	pygame.draw.rect(screen, GRID_BASE, [561, 50, 5, 431]) # right base shade
	pygame.draw.rect(screen, GRID_BASE_SHADE_HIGH, [564, 50, 2, 431]) # right high shade
	pygame.draw.rect(screen, GRID_BASE_SHADE_MED, [563, 50, 1, 431]) # right med shade

	pygame.draw.rect(screen, GRID_BASE, [135, 50, 431, 5]) # top base shade
	pygame.draw.rect(screen, GRID_BASE_SHADE_HIGH, [135, 50, 431, 2]) # top high shade
	pygame.draw.rect(screen, GRID_BASE_SHADE_MED, [135, 52, 431, 1]) # top med shade

	pygame.draw.rect(screen, GRID_BASE, [135, 476, 431, 5]) # bot base shade
	pygame.draw.rect(screen, GRID_BASE_SHADE_HIGH, [135, 479, 431, 2]) # bot high shade
	pygame.draw.rect(screen, GRID_BASE_SHADE_MED, [135, 478, 431, 1]) # bot med shade

	# Inner column grids
	for i in xrange(9):
		pygame.draw.rect(screen, GRID_BASE, [185+i*47,55,2,422])
	

	# Inner row grids
	for i in xrange(9):
		pygame.draw.rect(screen, GRID_BASE, [140,100+i*47,422,2])


# Colors the squares
def draw_square_color(screen):
	
	# filling the squares with coordinates using square_pos and colors depending on 
	# square_color
	# calculate colors
	global square_notation
	calcSquareColor()
	for square in square_notation:
		pygame.draw.rect(screen, square_color[square], square_pos[square])

# draw number options
def draw_options(screen):
	global number_selected
	if number_selected!=-1:
		# The cursor hovers over a number
		pygame.draw.circle(screen, OPTIONS_CIRCLE, (625, 65+45*number_selected), 20)
	for i in xrange(10):
		screen.blit(options_text[i], (620, 53+45*i))
		pygame.draw.circle(screen, OPTIONS_CIRCLE, (625, 65+45*i), 20, 1 )

# draws the user entered numbers on the grid		
def draw_user_numbers(screen):
	makeNumberText()
	global square_notation
	global square_user_values_text
	global square_user_values
	for square in square_notation:
		#finding position based on the notation value
		xpos = int(square[1])-1
		ypos = ord(square[0])-ord('A')
		if square_user_values[square]!=0:
			screen.blit(square_user_values_text[square], (155+xpos*47, 65+ypos*47))

def draw_buttons(screen):
	# draw the solve, reset and clear buttons
	pygame.draw.rect(screen, BUTTON, (288, 510, 125, 50))
	pygame.draw.rect(screen, BUTTON, (138, 510, 125, 50))
	pygame.draw.rect(screen, BUTTON, (438, 510, 125, 50))
	if solveClick:
		pygame.draw.rect(screen, BUTTON_CLICK, (288, 510, 125, 50))
	if resetClick:
		pygame.draw.rect(screen, BUTTON_CLICK, (138, 510, 125, 50))
	if clearClick:
		pygame.draw.rect(screen, BUTTON_CLICK, (438, 510, 125, 50))




	# draw the text in the buttons
	screen.blit(solve_text, (307, 517))
	screen.blit(reset_text, (157, 517))
	screen.blit(clear_text, (457, 517))

def draw_solution(screen):
	makeNumberSolutionText()
	global square_notation
	global square_solution_values
	global square_solution_values_text
	for square in square_notation:
		xpos = int(square[1])-1
		ypos = ord(square[0])-ord('A')
		screen.blit(square_solution_values_text[square], (155+xpos*47, 65+ypos*47))
	# we call this function to overwrite
	# All the numbers are in red
	# but to keep the original in black, we overwrite it again
	draw_user_numbers(screen)

# write error message
def draw_error(screen):
	txt = button_font.render("INVALID VALUES", True, NUMBER_SOLUTION)
	screen.blit(txt, (235,10))











# Main application loop--------------------------------------------------------------
while not app_done:

	# refreshing hover color fill
	square_color_number = gn.refreshHoverColor(square_color_number)

	# Resetting values
	mouseCollideSquare = False
	mouseClick = False

	# mouse position
	mousex, mousey = pygame.mouse.get_pos()

	# Event processing --------------------------------------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			app_done = True # Quits the app on the next iteration
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouseClick = True
			error_print = False
		if event.type == pygame.MOUSEBUTTONUP:
			# if button is clicked and released, restore original color
			if solve_rect.collidepoint(mousex, mousey):
				solveClick = False
			if reset_rect.collidepoint(mousex, mousey):
				resetClick = False
			if clear_rect.collidepoint(mousex, mousey):
				clearClick = False
			




	# If solve is clicked, freeze screen
	if not solveGrid:
		# Game logic --------------------------------------------------------------------
		
		# check if the mouse coordinates collides with the squares
		if not drawOptionsMenu: # freeze if number options is drawn
			for square in square_rect:
				if square_rect[square].collidepoint(mousex, mousey):
					if square_color_number[square]!=2: # to prevent overwriting filled green
						square_color_number[square] = 3
						# reset button color change
					mouseCollideSquare = True
					break # because the mouse can hover over only one square at a time

		if not drawOptionsMenu: # dont allow selection unless the options menu is gone
			if mouseClick:
				for square in square_rect:
					if square_rect[square].collidepoint(mousex, mousey):
						square_color_number[square] = 2
						last_selected_square = square
						drawOptionsMenu = True
						break
		if drawOptionsMenu: # menu is drawn
			optionHover()
			# print number_selected
		# If there was a mouse click outside the grid, then remove the options menu
		if mouseClick:
			if not grid_rect.collidepoint(mousex, mousey) and not solve_rect.collidepoint(mousex, mousey) and not clear_rect.collidepoint(mousex, mousey) and not reset_rect.collidepoint(mousex, mousey):
				if number_selected == -1:
					drawOptionsMenu = False
					setDualColorSquare(last_selected_square)
					# we need to make sure to remove the number if the user clicks away
					# without selecting a number.
					# this case is for when the user comes back to square to remove the 
					# number
					square_user_values[last_selected_square] = 0
					
				else:
					# put the number that the user selected to the grid
					square_user_values[last_selected_square] = number_selected
					drawOptionsMenu = False
					# if 0 is selected. Clear the green square
					# The user can input 0 to clear
					if number_selected == 0:
						setDualColorSquare(last_selected_square)
	if mouseClick:
		# If the solve button is clicked
		if solve_rect.collidepoint(mousex, mousey):
			square_solution_values = alg.solve(conv.convToString(square_user_values))
			# square_solution_values stores False if the user entered solution is invalid
			solveClick = True
			if square_solution_values == False or isUserValuesEmpty() :
				error_print = True
			else:
				solveGrid = True
		# If the clear button is clicked
		if clear_rect.collidepoint(mousex, mousey):
			# clears the screen
			clearClick = True
			solveGrid = False
			initClear()

		# If the reset is clicked, it removes all the computed solutions
		if reset_rect.collidepoint(mousex, mousey):
			resetClick = True
			solveGrid = False
			initReset()
	if not grid_rect.collidepoint(mousex, mousey) and not solve_rect.collidepoint(mousex, mousey) and not clear_rect.collidepoint(mousex, mousey) and not reset_rect.collidepoint(mousex, mousey):
		solveClick = resetClick = clearClick = False # to reset button click color







	# display calls -----------------------------------------------------------------
	main_draw(screen)
	pygame.display.flip()
	clock.tick(60)


pygame.quit()

