import pygame as pg


class Ball:

    def __init__(self, window):
        self.window = window

        self.ball = pg.Rect(0, 0, 20, 20)
        self.ball.center = (250, 450)

        self.move_x = 3
        self.move_y = 3

    def draw_ball(self):
        pg.draw.rect(self.window, "yellow", self.ball, 0, 10)

    def move(self):
        self.ball.x -= self.move_x
        self.ball.y -= self.move_y

    def reverse_movement(self):
        self.move_x *= -1
        self.move_y *= -1

    def bounce(self, blocks1, blocks2, blocks3, paddle):
        index1 = self.ball.collidelist(blocks1)
        index2 = self.ball.collidelist(blocks2)
        index3 = self.ball.collidelist(blocks3)

        if index3 != -1:
            print("BOUNCE")
            blocks3.pop(index3)
            self.move_y *= -1

        elif index2 != -1:
            print("BOUNCE")
            blocks2.pop(index2)
            self.move_y *= -1

        elif index1 != -1:
            print("BOUNCE")
            blocks1.pop(index1)
            self.move_y *= -1

        elif self.ball.colliderect(0, 0, 2, 500) or self.ball.colliderect(500, 0, 2, 500):
            self.move_x *= -1

        elif self.ball.colliderect(paddle) or self.ball.colliderect(0, 0, 500, 2):
            self.move_y *= -1
