import pygame
from constants import *
class DifferentialEquation:
    #stores all the DE information
    def __init__(self, eq, order):
        self.eq = eq
        self.order = order
        self.num_init_cond = order + 1
        parameters = "x, y, " + ", ".join((f"d{n}y" for n in range(1, self.order)))
        self.dny_dxn = eval(f"lambda {parameters}: {self.eq[self.eq.index('=')+1:]}")

    #returns a generator object for (x,y) point pairs using initial conditions
    def eulers_method(self, dx, initial_conditions):
        
        if len(initial_conditions) != self.num_init_cond:
            raise ValueError(f"Expected {self.num_init_cond} inital conditions")

        state = list(initial_conditions)
        while True:
            dny_dxn = self.dny_dxn(*state) #inital final derivative
            state[0] += dx #updating the state vector
            for n in range(1, self.num_init_cond-1):
                state[n] += state[n+1] * dx
            state[self.num_init_cond-1] += dny_dxn * dx #using inital final derivative to update last entry
            yield (state[0], state[1])


class ViewPort:

    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.scale = 50


    #coordinate transform Cartesian -> pygame coords
    def screen_coords(self, p):
        x, y = p
        X = x * self.scale + self.width//2
        Y = -y * self.scale + self.height//2
        return (X, Y)

    def grid_lines(self):
        self.screen.fill(WHITE)
        for i in range(self.width):
            pygame.draw.line(self.screen, GRAY, (i*self.scale, 0), (i*self.scale, self.height))
        for j in range(self.height):
            pygame.draw.line(self.screen, GRAY, (0, j*self.scale), (self.width, j*self.scale))
        pygame.draw.line(self.screen, BLACK, (self.width//2, 0), (self.width//2, self.height))
        pygame.draw.line(self.screen, BLACK, (0, self.height//2), (self.width, self.height//2))
