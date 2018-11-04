import pygame

class Component:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 1
        self.h = 1
        self.layout_manager = None

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def set_layout_manager(self, manager):
        self.layout_manager = manager

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.get_rect())