class Snake(object):
    def __init__(self, length = 1 , pos= [0,0]):
        self.length = length
        self.pos = pos
        self.body = []
    def __len__(self):
        return self.length
    def __repr__(self):
        return 'Length: {} \nPos: {}'.format(self.length,self.pos)

class Food(object):
    def __init__(self, pos = [0,0]):
        self.pos = pos
    def __repr__(self):
        return 'Pos: {}'.format(self.pos)
    def getPos(self):
        return self.pos
    def setPos(self, pos):
        self.pos = pos
