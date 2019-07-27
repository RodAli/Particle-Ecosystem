from particle import Particle
import util
import random

class Creep(Particle):

    def __init__(self, id, x, y, colour):
        Particle.__init__(self, id, x, y, colour)

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
        
        # Cannot move on top of another predator
        positionsOfAllOtherPrey = [p.getLocation() for p in world.getPrey() if p.id != self.id]
        viablePositions = [p for p in viablePositions if p not in positionsOfAllOtherPrey]

        return viablePositions

    def move(self, world):

        # If there are no predators, default to random movement
        if len(world.predators) <= 0:
            Particle.move(self, world)
            return
        
        # Get location of all predators
        predatorLocations = [p.getLocation() for p in world.predators]

        # Get the location of the predators that are the closest
        closestPredatorLocations = util.findClosestCoordsToTargetCoord(self.getLocation(), predatorLocations)
        
        if len(closestPredatorLocations) < 1: return
        
        # Choose a random prey from among the closest particles
        targetPredatorLocation = random.choice(closestPredatorLocations)
        
        # Get the positions that we can legally move to
        viableCoords = self.getViablePositionsToMove(world)
        
        # Take the move that brings us furthest to the nearsest predator
        bestCoords = util.findFurthestCoordsToTargetCoord(targetPredatorLocation, viableCoords)
        
        if len(bestCoords) > 0:
            chosenBestCoord = random.choice(bestCoords)
            self.x = chosenBestCoord[0]
            self.y = chosenBestCoord[1]
    
    def eat(self, world):
        pass