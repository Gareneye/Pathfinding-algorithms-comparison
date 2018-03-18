import pygame
import math
import random
import sys

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)
TRANS    = (   1,   2,   3)

# CONSTANTS:
WIDTH = 700
HEIGHT = 700
MARK_SIZE = 50

#GLOBAL VARIABLES:
row = 0
column = 0

board_height = 10
board_width = 10

seeker_start_x = 0
seeker_start_y = 0

goal_x = board_width-1
goal_y = board_height-1 

class Game:

	def __init__(self):

		self.game_board = [[0 for x in range(board_width)] for y in range(board_height)]

		for i in range(board_width):
			for j in range (board_height):
				self.game_board[i][j]='-'

		self.game_board[seeker_start_x][seeker_start_y]='s'
		self.game_board[goal_x][goal_y]='G'		

	def evaluate_click(self, mouse_pos):

		row, column = get_clicked_row(mouse_pos), get_clicked_column(mouse_pos)
		self.toggle_obsticle(row,column)
		
	
	def draw(self):

		for i in range(board_width+1):
			pygame.draw.line(screen, WHITE, [i * WIDTH / board_width, 0], [i * WIDTH / board_width, HEIGHT], 5)
		for i in range(board_height+1):
		 	pygame.draw.line(screen, WHITE, [0, i * HEIGHT / board_height], [WIDTH, i * HEIGHT / board_height], 5)
		font = pygame.font.SysFont('Calibri', MARK_SIZE, False, False)
		for r in range(len(self.game_board)):
			for c in range(len(self.game_board[r])):
				mark = self.game_board[r][c]
				if mark != '-':
					mark_text = font.render(self.game_board[r][c], True, RED)
					x = WIDTH / board_width * c + WIDTH / (board_width*2)
					y = HEIGHT / board_height * r + HEIGHT / (board_height*2)
					screen.blit(mark_text, [x - mark_text.get_width() / 2, y - mark_text.get_height() / 2])


	def toggle_obsticle(self,row,column):
		if(self.game_board[row][column]=='o'):
			self.game_board[row][column]='-'
		else:
			self.game_board[row][column]='o'
		

# Helper functions:
def get_clicked_column(mouse_pos):
	x = mouse_pos[0]
	for i in range(1, board_width):
		if x < i * WIDTH / board_width:
			return i - 1
	return board_width - 1

def get_clicked_row(mouse_pos):
	y = mouse_pos[1]
	for i in range(1, board_height):
		if y < i * HEIGHT / board_height:
			return i - 1
	return board_height - 1


# start pygame:
pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
game = Game()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# game loop:
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            entry = str(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
        	mouse_x, mouse_y = pygame.mouse.get_pos()
        	game.evaluate_click(pygame.mouse.get_pos())

 
    # First, clear the screen to black. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    # draw the game board and marks:
    game.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()