from particle import Particle
import util
import random

class Predator(Particle):

    def __init__(self, id, x, y, colour):
        Particle.__init__(self, id, x, y, colour)

    def move(self, boardWidth, boardHeight, particles):

        particleLocations = [p.getLocation() for p in particles]

        preyLocations = util.findClosestCoordsToTargetCoord(self.getLocation(), particleLocations)
        
        if len(preyLocations) < 1: return
        
        targetPreyLocation = random.choice(preyLocations)

        viableCoords = self.getViablePositionsToMove(boardWidth, boardHeight)

        bestCoords = util.findClosestCoordsToTargetCoord(targetPreyLocation, viableCoords)
        
        if len(bestCoords) > 0:
            chosenBestCoord = random.choice(bestCoords)
            self.x = chosenBestCoord[0]
            self.y = chosenBestCoord[1]