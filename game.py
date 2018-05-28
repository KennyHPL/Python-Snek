import pygame as pg
import random

class Snake(object):
    def __init__(self, length, pos):
        self.length = length
        self.pos = pos
        self.body = []

    def __len__(self):
        return self.length
    def __repr__(self):
        return 'Length: {} \nPos: {}'.format(self.length,self.pos)

class Food(object):
    def __init__(self, pos):
        self.pos = pos
    def __repr__(self):
        return 'Pos: {}'.format(self.pos)
pg.init()
screen = pg.display.set_mode((700,700))
pg.display.set_caption('Snake')
###############################################################################

done = False
clock = pg.time.Clock()
snake = Snake(1, [0,0])
food = Food([random.randint(0,34)*20, random.randint(0,34)*20])

xVel = 0
yVel = 0
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            key = event.key
            if key == pg.K_DOWN:
                yVel = 20
                xVel = 0
            if key == pg.K_UP:
                yVel = -20
                xVel = 0
            if key == pg.K_LEFT:
                xVel = -20
                yVel = 0
            if key == pg.K_RIGHT:
                xVel = 20
                yVel = 0

    #Make the screen white
    screen.fill((255,255,255))

    #draw the food
    pg.draw.rect(screen, (255,0,0), [food.pos[0], food.pos[1], 20, 20])

    #Check if the head of the snake is on top of the food
    if snake.pos == food.pos:
        snake.length += 1
        food.pos = [random.randint(0,34)*20, random.randint(0,34)*20]

    #Update the position of the snake
    snake.pos = [(snake.pos[0]+xVel)%700, (snake.pos[1]+yVel)%700]

    #check if head in on the body
    if snake.pos in snake.body and snake.pos != [0,0]:
        done = True

    #insert the position into the snake body
    snake.body.insert(0, snake.pos)
    if len(snake.body) > snake.length:
        snake.body.pop()

    #draw the body
    for i in range(0, len(snake.body)):
        pg.draw.rect(screen, (0,0,0), [snake.body[i][0], snake.body[i][1], 20, 20])

    #Update the screen
    pg.display.flip()
    clock.tick(24)
