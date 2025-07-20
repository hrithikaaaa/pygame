import pygame
from grid import Grid
from algorithms import dijkstra
from constants import *

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")
    grid = Grid()
    running = True
    algorithm = None

    def draw():
        grid.draw_grid(window)
        grid.draw_nodes(window)
        pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:  # Left-click
                pos = pygame.mouse.get_pos()
                if not grid.start:
                    grid.handle_click(pos, "START")
                elif not grid.end:
                    grid.handle_click(pos, "END")
                else:
                    grid.handle_click(pos, "WALL")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and grid.start and grid.end:
                    dijkstra(grid, grid.start, grid.end, draw)
                elif event.key == pygame.K_c:  # Clear grid
                    grid.__init__()

        draw()

if __name__ == "__main__":
    main()