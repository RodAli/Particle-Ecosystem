import random
import util

class Particle:

    def __init__(self, id, x, y, colour):
        self.id = id
        self.x = x
        self.y = y
        self.colour = colour

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def getLocation(self):
        return (self.x, self.y)

    def setLocation(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def getColour(self):  
        return self.colour
    
    def getViablePositionsToMove(self, world):
        viablePositions = [self.getLocation()]

        if self.x > 0:
            viablePositions.append((self.x - 1, self.y))
        if self.x < world.gridWidth - 1:
            viablePositions.append((self.x + 1, self.y))
        if self.y > 0:
            viablePositions.append((self.x, self.y - 1))
        if self.y < world.gridHeight - 1:
            viablePositions.append((self.x, self.y + 1))
        
        # Cannot move on top of another prey
        positionsOfAllOtherPrey = [p.getLocation() for p in world.getPrey() if p.id != self.id]
        viablePositions = [p for p in viablePositions if p not in positionsOfAllOtherPrey]

        return viablePositions

    def move(self, world):
        viablePositions = self.getViablePositionsToMove(world)

        if len(viablePositions) > 0:
            selectedPosition = random.choice(viablePositions)
            self.setLocation(selectedPosition)
    
    def eat(self, world):
        pass