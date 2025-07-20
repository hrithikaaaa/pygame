import pygame
from constants import *

class Grid:
    def __init__(self):
        self.grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.start = None
        self.end = None

    def draw_grid(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, WHITE, rect, 1)

    def draw_nodes(self, window):
        for row in range(ROWS):
            for col in range(COLS):
                node = self.grid[row][col]
                if node == "START":
                    color = GREEN
                elif node == "END":
                    color = RED
                elif node == "WALL":
                    color = GRAY
                elif node == "VISITED":
                    color = BLUE
                elif node == "PATH":
                    color = PURPLE
                else:
                    continue
                pygame.draw.rect(window, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def handle_click(self, pos, node_type):
        row, col = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
        if 0 <= row < ROWS and 0 <= col < COLS:
            if node_type == "START":
                if self.start:
                    self.grid[self.start[0]][self.start[1]] = None
                self.start = (row, col)
            elif node_type == "END":
                if self.end:
                    self.grid[self.end[0]][self.end[1]] = None
                self.end = (row, col)
            self.grid[row][col] = node_type