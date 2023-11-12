import pygame as pg


class Paddle:

    def __init__(self, window):
        self.window = window

        self.paddle = pg.Rect(0, 0, 120, 15)
        self.paddle.center = (250, 470)

        self.move_l = False
        self.move_r = False

    def draw_paddle(self):
        pg.draw.rect(self.window, "black", self.paddle)

    def handle_events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.move_l = True
            elif event.key == pg.K_RIGHT:
                self.move_r = True
        elif event.type == pg.KEYUP:
            self.move_r = False
            self.move_l = False

    def move(self):
        if self.move_l and not self.paddle.colliderect(0, 0, 2, 500):
            self.paddle.x -= 10
        elif self.move_r and not self.paddle.colliderect(498, 0, 2, 500):
            self.paddle.x += 10
