import pygame

from constants import *
import basic_classes
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900


def setup():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    view_box = basic_classes.ViewPort(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    view_box.grid_lines()
    
    return screen, view_box


def plot_DE(screen, view_box, DE, dx, color, initial_conditions):

        line_start = view_box.screen_coords((initial_conditions[0], initial_conditions[1]))
        g = DE.eulers_method(dx, initial_conditions)

        for i in range(10000):
            line_end = view_box.screen_coords(next(g))
            if not(0 <= line_end[0] <= SCREEN_WIDTH) or not(0 <= line_end[1] <= SCREEN_HEIGHT):
                break
            else:
                pygame.draw.line(screen, color, line_start, line_end, SOLUTION_THICKNESS)
                pygame.display.flip()
                line_start = line_end

def main():
    screen, view_box = setup()
    DE1 = basic_classes.DifferentialEquation("d3y = d2y - x*y", 3)
    plot_DE(screen, view_box, DE1, 0.01, RED, (0, 0, 1, 0))
    plot_DE(screen, view_box, DE1, -0.01, RED, (0, 0, 1, 0))

    DE2 = basic_classes.DifferentialEquation("d2y = -y", 2)
    plot_DE(screen, view_box, DE2, 0.01, BLUE, (0, 0, 1))
    plot_DE(screen, view_box, DE2, -0.01, BLUE, (0, 0, 1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()

main()
