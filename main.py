import pygame as pg

from ball import Ball
from blocks import Blocks
from paddle import Paddle

pg.init()
pg.display.set_caption("Breakout")

window = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
blocks_ = Blocks(window)
paddle = Paddle(window)
ball = Ball(window)

running = True

while running:

    window.fill("white")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        paddle.handle_events(event)

    blocks_.draw_blocks()
    paddle.draw_paddle()
    ball.draw_ball()

    paddle.move()
    ball.move()

    ball.bounce(blocks_.blocks1, blocks_.blocks2, blocks_.blocks3, paddle.paddle)

    pg.display.update()

    clock.tick(120)

pg.quit()
