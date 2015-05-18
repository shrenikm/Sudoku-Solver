import pygame
import os
import gridNotation as gn

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
SQUARE_FILLED = (89,181,36)
SQUARE_HOVER = (252, 179, 43)
OPTIONS_TEXT = (30,50,40)
OPTIONS_CIRCLE = (124,162,252)

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

# dictionary of rectangles. pygame.Rect(x,y,w,h)
square_rect = dict([(square, pygame.Rect(square_pos[square][0], square_pos[square][1], 45, 45)) for square in square_pos])
# The rectangle for the whole grid
grid_rect = pygame.Rect(135, 50, 431, 431)
# store the number that was selected in the options
number_selected = -1
# stores the last selected square
last_selected_square = ''



mouseCollideSquare = False
mouseClick = False
drawOptionsMenu = False
selectDrawOptions = False





# Game functions-------------------------------------------------------------------
def calcSquareColor():
	# Makes a dictionary with colors for the squares using square_color_number
	for square in square_notation:
		if square_color_number[square] == 1:
			square_color[square] = SQUARE_DEFAULT # pale yellow
		elif square_color_number[square] == 2:
			square_color[square] = SQUARE_FILLED # green
		elif square_color_number[square] == 3:
			square_color[square] = SQUARE_HOVER # orange
		else:
			pass

# function that checks if the mouse hovers over any of the options
def optionHover():
	ishovering = False
	global number_selected
	for i in xrange(9):

		# using equation of circle
		dst = ((mousex-625.0)**2 + (mousey-(87+45*i))**2)**0.5
		if dst<=20:
			number_selected = i
			ishovering = True
			break
	if not ishovering:
		number_selected = -1





# pygame initializations -----------------------------------------------------------
# size of the screen
size = [700, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku Solver")

pygame.init()

# font initialization
options_font = pygame.font.SysFont("comicsansms", 16)
options_text = [options_font.render(str(i), True, OPTIONS_TEXT) for i in xrange(1,10)]

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
	pygame.draw.rect(screen, GRID_BASE, [185,55,2,422])
	pygame.draw.rect(screen, GRID_BASE, [232,55,2,422])
	pygame.draw.rect(screen, GRID_BASE, [279,55,2,422])
	pygame.draw.rect(screen, GRID_BASE, [326,55,2,422])
	pygame.draw.rect(screen, GRID_BASE, [373,55,2,422])
	pygame.draw.rect(screen, GRID_BASE, [420,55,2,422])
	pygame.draw.rect(screen, GRID_BASE, [467,55,2,422])
	pygame.draw.rect(screen, GRID_BASE, [514,55,2,422])

	# Inner row grids
	pygame.draw.rect(screen, GRID_BASE, [140,100,422,2])
	pygame.draw.rect(screen, GRID_BASE, [140,147,422,2])
	pygame.draw.rect(screen, GRID_BASE, [140,194,422,2])
	pygame.draw.rect(screen, GRID_BASE, [140,241,422,2])
	pygame.draw.rect(screen, GRID_BASE, [140,288,422,2])
	pygame.draw.rect(screen, GRID_BASE, [140,335,422,2])
	pygame.draw.rect(screen, GRID_BASE, [140,382,422,2])
	pygame.draw.rect(screen, GRID_BASE, [140,429,422,2])

# Colors the squares
def draw_square_color(screen):
	
	# filling the squares with coordinates using square_pos and colors depending on 
	# square_color
	# calculate colors
	calcSquareColor()
	for square in square_notation:
		pygame.draw.rect(screen, square_color[square], square_pos[square])

# draw number options
def draw_options(screen):
	if number_selected!=-1:
		# The cursor hovers over a number
		pygame.draw.circle(screen, OPTIONS_CIRCLE, (625, 87+45*number_selected), 20)
	for i in xrange(9):
		screen.blit(options_text[i], (620, 75+45*i))
		pygame.draw.circle(screen, OPTIONS_CIRCLE, (625, 87+45*i), 20, 1 )








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
			mousex, mousey = pygame.mouse.get_pos()
			mouseClick = True
			





	# Game logic --------------------------------------------------------------------
	
	# check if the mouse coordinates collides with the squares
	if not drawOptionsMenu: # freeze if number options is drawn
		for square in square_rect:
			if square_rect[square].collidepoint(mousex, mousey):
				if square_color_number[square]!=2: # to prevent overwriting filled green
					square_color_number[square] = 3
				mouseCollideSquare = True
				break
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
		if not grid_rect.collidepoint(mousex, mousey):
			if number_selected == -1:
				drawOptionsMenu = False
				square_color_number[last_selected_square] = 1
			else:
				# put the number that the user selected to the grid
				square_user_values[last_selected_square] = number_selected+1
				drawOptionsMenu = False





	# display calls -----------------------------------------------------------------
	main_draw(screen)
	pygame.display.flip()
	clock.tick(60)

pygame.quit()

