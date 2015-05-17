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
SQUARE_HOVER = (89,181,36)
SQUARE_FILLED = (252, 179, 43)

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

# dictionary of rectangles. pygame.Rect(x,y,w,h)
square_rect = dict([(square, pygame.Rect(square_pos[square][0], square_pos[square][1], 45, 45)) for square in square_pos])


mouseCollideSquare = False





# Game functions-------------------------------------------------------------------
def calcSquareColor():
	# Makes a dictionary with colors for the squares using square_color_number
	for square in square_notation:
		if square_color_number[square] == 1:
			square_color[square] = SQUARE_DEFAULT # pale yellow
		elif square_color_number[square] == 2:
			square_color[square] = SQUARE_FILLED # green
		else:
			square_color[square] = SQUARE_HOVER # orange




# pygame initializations -----------------------------------------------------------
# size of the screen
size = [700, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku Solver")

app_done = False # variable to stop the application loop
clock = pygame.time.Clock() # managing screen update time





# All the drawing functions---------------------------------------------------------

# The main draw function that is called. It calls all the other drawing functions
def main_draw(screen):
	screen.fill(APP_BACKGROUND)
	draw_grid(screen)
	draw_square_color(screen)

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








# Main application loop--------------------------------------------------------------
while not app_done:

	# refreshing hover color fill
	square_color_number = gn.refreshHoverColor(square_color_number)
	mouseCollideSquare = False

	# Event processing --------------------------------------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			app_done = True # Quits the app on the next iteration
		elif event.type == pygame.MOUSEMOTION:
			mousex, mousey = event.pos




	# Game logic --------------------------------------------------------------------
	
	# check if the mouse coordinates collides with the squares
	for square in square_rect:
		if square_rect[square].collidepoint(mousex, mousey):
			square_color_number[square] = 2
			mouseCollideSquare = True
			break



	# display calls -----------------------------------------------------------------
	main_draw(screen)
	pygame.display.flip()
	clock.tick(60)

pygame.quit()

