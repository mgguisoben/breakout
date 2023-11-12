import pygame as pg


class Blocks:

    def __init__(self, window):
        self.window = window

        self.blocks3 = []
        self.blocks2 = []
        self.blocks1 = []

        self.create_blocks()

    def create_blocks(self):
        for x in range(5):
            for y in range(2):
                rect = pg.Rect(x * 94 + (x + 1) * 5,
                               y * 40 + (y + 1) * 5,
                               94, 40)
                self.blocks3.append(rect)

        for x in range(5):
            for y in range(4):
                rect = pg.Rect(x * 94 + (x + 1) * 5,
                               y * 40 + (y + 1) * 5,
                               94, 40)
                self.blocks2.append(rect)

        for x in range(5):
            for y in range(6):
                rect = pg.Rect(x * 94 + (x + 1) * 5,
                               y * 40 + (y + 1) * 5,
                               94, 40)
                self.blocks1.append(rect)

    def draw_blocks(self):
        for block in self.blocks1:
            pg.draw.rect(self.window, "red", block)
        for block in self.blocks2:
            pg.draw.rect(self.window, "green", block)
        for block in self.blocks3:
            pg.draw.rect(self.window, "blue", block)
