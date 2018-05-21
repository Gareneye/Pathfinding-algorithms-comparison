import pygame
import math
import random
import sys

import astar
import bfs
import dfs
import dijstra
import astar
from itertools import cycle


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TRANS = (1, 2, 3)
GREY = (100, 100, 100)

# GLOBAL VARIABLES:
row = 0
column = 0

board_height = 20
board_width = 20


algorithms=[("astar",astar),("bfs",bfs),("dfs",dfs),("dijkstra",dijstra)]

algorithms_pool = cycle(algorithms)

# CONSTANTS:
RECT_SIZE = 30
RECT_PADDING = 1
WIDTH = RECT_SIZE * board_width + board_width * RECT_PADDING + RECT_PADDING
HEIGHT = RECT_SIZE * board_height + board_height * RECT_PADDING + RECT_PADDING

class Game:

    def __init__(self):
        
        self.seeker_x = 0
        self.seeker_y = 0

        self.goal_x = board_width - 1
        self.goal_y = board_height - 1


        self.obsticles = []
        self.path = []
        self.presentation = []
        self.font = pygame.font.SysFont("monospace", 25)
        self.font.set_bold(True)

        self.next_algorithm()

        self.moving_seeker = False
        self.moving_goal = False



        
        


    def evaluate_click(self, mouse_pos):
        row, column = get_clicked_row(mouse_pos), get_clicked_column(mouse_pos)
        if(self.moving_seeker == True):
            self.seeker_x = column
            self.seeker_y = row
            self.find_path()
            self.moving_seeker = False
        elif(row==self.seeker_y and column ==self.seeker_x):
            self.moving_seeker = True
        elif(self.moving_goal == True):
            self.goal_x = column
            self.goal_y = row
            self.find_path()
            self.moving_goal = False
        elif(row==self.goal_y and column ==self.goal_x):
            self.moving_goal = True
        else:
            self.toggle_obsticle(row, column)

    def draw(self):
        # draw board
        for x in range(board_width):
            for y in range(board_height):
                pygame.draw.rect(screen, GREY, self.getPixelCoords(x, y) + (RECT_SIZE, RECT_SIZE), 0)

        for node in self.presentation:
            pygame.draw.rect(screen, self.presentation[node], self.getPixelCoords(node[0], node[1]) + (RECT_SIZE, RECT_SIZE), 0)

        # draw path
        #for node in self.path:
        #    pygame.draw.rect(screen, (160, 160, 160), self.getPixelCoords(node[0], node[1]) + (RECT_SIZE, RECT_SIZE), 0)

        # draw start and goal
        if (self.moving_seeker == False):
            pygame.draw.rect(screen, YELLOW, self.getPixelCoords(self.seeker_x, self.seeker_y) + (RECT_SIZE, RECT_SIZE), 0)
        
        if (self.moving_goal == False):
            pygame.draw.rect(screen, GREEN, self.getPixelCoords(self.goal_x, self.goal_y) + (RECT_SIZE, RECT_SIZE), 0)

        # draw arrows
        lastNode = None
        for node in self.path:
            if lastNode:
                start = self.getPixelCoords(lastNode[0], lastNode[1])
                start = (start[0] + RECT_SIZE/2, start[1] + RECT_SIZE/2)
                end = self.getPixelCoords(node[0], node[1])
                end = (end[0] + RECT_SIZE/2, end[1] + RECT_SIZE/2)
                pygame.draw.line(screen, WHITE, start, end, 5)

            lastNode = node


        # draw obsticles
        for node in self.obsticles:
            pygame.draw.rect(screen, BLACK, self.getPixelCoords(node[0], node[1]) + (RECT_SIZE, RECT_SIZE), 0)

        #draw text with algorithm name
        screen.blit(self.label, (10,HEIGHT-35))

    def getPixelCoords(self, x, y):
        return (
            x*RECT_SIZE+x*RECT_PADDING+RECT_PADDING,
            y*RECT_SIZE+y*RECT_PADDING+RECT_PADDING
        )

    def toggle_obsticle(self, row, column):
        node = (column, row)
        if node in self.obsticles:
            self.obsticles.remove(node)
        else:
            self.obsticles.append(node)

        self.find_path()

    def find_path(self):
        self.presentation, self.path = self.algorithm[1].resolve(
            start_node=(self.seeker_x, self.seeker_y),
            goal_node=(self.goal_x, self.goal_y),
            inactive=self.obsticles,
            width=board_width,
            height=board_height
        )

    def next_algorithm(self):
        self.algorithm = next(algorithms_pool)
        self.label = self.font.render(self.algorithm[0]+" <press SPACE to change>", 1, RED)
        self.find_path()





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
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            entry = str(event.key)
            if event.key==32:
                game.next_algorithm()
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
