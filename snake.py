import pygame as pg

class Snake(object):
    def __init__(self, length):
        self.length = length
    def __repr__(self):
        return 'I am a snake of length {}'.format(self.length)
    def __lshift__(self, other):
        if(self.length > other.length):
            self.length += other.length
            other.length = 0
            return self
        else:
            self.length = 0
            return self
    def __rshift__(self, other):
        if(self.length < other.length):
            self.length = 0
            return self
        else:
            self.length += other.length
            other.length = 0
            return self

class Food(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'Food with value {}'.format(self.value)

pg.init()
a = Snake(10)
b = Snake(2)

print(a<<b)
print(a>>b)

screen = pg.display.set_mode((700,500))
pg.display.set_caption('Snake')

done = False
clock = pg.time.Clock()

xPos = 0
yPos = 0
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            key = event.key
            if key == pg.K_DOWN:
                yPos+=20
            if key == pg.K_UP:
                yPos-=20
            if key == pg.K_LEFT:
                xPos-=20
            if key == pg.K_RIGHT:
                xPos+=20

    screen.fill((255,255,255))
    pg.draw.rect(screen, (0,0,0),[xPos, yPos, 20, 20])
    pg.display.flip()
    clock.tick(60)

print('Done')
