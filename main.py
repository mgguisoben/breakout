import pygame as pg

from blocks import Blocks

pg.init()
pg.display.set_caption("Breakout")

window = pg.display.set_mode((500, 600))
blocks_ = Blocks(window)

running = True

while running:

    window.fill("white")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    blocks_.draw_blocks()

    pg.display.update()

pg.quit()