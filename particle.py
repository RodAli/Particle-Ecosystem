import random
import util

class Particle:

    def __init__(self, id, x, y, colour):
        self.id = id
        self.x = x
        self.y = y
        self.colour = colour

    def getLocation(self):
        return (self.x, self.y)

    def setLocation(self, coord):
        self.x = coord[0]
        self.y = coord[1]
    
    def getViablePositionsToMoveOnBoard(self, world):
        viablePositions = [self.getLocation()]

        if self.x > 0:
            viablePositions.append((self.x - 1, self.y))
        if self.x < world.gridWidth - 1:
            viablePositions.append((self.x + 1, self.y))
        if self.y > 0:
            viablePositions.append((self.x, self.y - 1))
        if self.y < world.gridHeight - 1:
            viablePositions.append((self.x, self.y + 1))

        return viablePositions

    def move(self, world):
        pass
    
    def eat(self, world):
        pass