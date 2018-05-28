import pygame as pg
import random
from snake import *

width = 900; height = 900
xVel = 0; yVel = 0
done = False
blockSize = 20
snake = Snake()
food = Food()
score = 0

pg.init()
screen = pg.display.set_mode((width,height))
pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 15)

pg.display.set_caption('Snake')
clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            key = event.key
            #### ARROW KEYS ####
            if key == pg.K_DOWN:
                yVel = blockSize
                xVel = 0
            if key == pg.K_UP:
                yVel = -blockSize
                xVel = 0
            if key == pg.K_LEFT:
                xVel = -blockSize
                yVel = 0
            if key == pg.K_RIGHT:
                xVel = blockSize
                yVel = 0
            #### ESC ####
            if key == pg.K_ESCAPE:
                done = True

    #Make the screen white
    screen.fill((255,255,255))

    #draw the food
    if food.getPos() == [0,0]:
        food.setPos([random.randint(0,width/blockSize-1)*blockSize,
                     random.randint(0,height/blockSize-1)*blockSize])

    pg.draw.rect(screen, (255,0,0),
                [food.pos[0], food.pos[1], blockSize, blockSize])

    #Check if the head of the snake is on top of the food
    if snake.pos == food.pos:
        snake.length += 1
        score += 10
        food.setPos([random.randint(0,width/blockSize-1)*blockSize,
                     random.randint(0,height/blockSize-1)*blockSize])

    #Update the position of the snake
    snake.pos = [(snake.pos[0]+xVel)%width, (snake.pos[1]+yVel)%height]

    #check if head in on the body
    if snake.pos in snake.body and snake.pos != [0,0]:
        done = True

    #insert the position into the snake body
    snake.body.insert(0, snake.pos)
    if len(snake.body) > snake.length:
        snake.body.pop()

    #draw the body
    for i in range(0, len(snake.body)):
        pg.draw.rect(screen, (0,0,0),
                    [snake.body[i][0], snake.body[i][1], blockSize, blockSize])

    #Update the screen
    textSurface = myfont.render('Score: {}'.format(score), False, (0,0,0))
    screen.blit(textSurface, (30,30))
    pg.display.flip()
    clock.tick(30)
