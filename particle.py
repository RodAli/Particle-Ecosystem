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
    
    def getViablePositionsToMove(self, boardWidth, boardHeight):
        viablePositions = []

        if self.x > 0:
            viablePositions.append((self.x - 1, self.y))
        if self.x < boardWidth - 1:
            viablePositions.append((self.x + 1, self.y))
        if self.y > 0:
            viablePositions.append((self.x, self.y - 1))
        if self.y < boardHeight - 1:
            viablePositions.append((self.x, self.y + 1))

        return viablePositions

    def move(self, boardWidth, boardHeight, particles):
        viablePositions = self.getViablePositionsToMove(boardWidth, boardHeight)

        if len(viablePositions) > 0:
            selectedPosition = random.choice(viablePositions)
            self.setLocation(selectedPosition)
    
    def filterSelfOutOfParticleList(self, particles):
        return list(filter(lambda p: p.id != self.id, particles))

    def findClosestParticle(self, particles):   # We dont need this function
        otherParticles = self.filterSelfOutOfParticleList(particles)
        particleCoords = [p.getLocation() for p in otherParticles]
        closestCoords = util.findClosestCoordsToTargetCoord(self.getLocation(), particleCoords)

        if len(closestCoords) > 0:
            return random.choice(closestCoords)