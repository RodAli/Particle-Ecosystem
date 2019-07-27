from particle import Particle
import util
import random

class Predator(Particle):

    def __init__(self, id, x, y, colour):
        Particle.__init__(self, id, x, y, colour)
        self.particlesEaten = 0

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
        positionsOfAllOtherPredators = [p.getLocation() for p in world.predators if p.id != self.id]
        viablePositions = [p for p in viablePositions if p not in positionsOfAllOtherPredators]

        return viablePositions

    def move(self, world):

        allPrey = world.getPrey()

        # If there are no particles, default to random movement
        if len(allPrey) <= 0:
            Particle.move(self, world)
            return
        
        # Get location of all particles
        particleLocations = [p.getLocation() for p in allPrey]

        # Get the location of the particles that are the closest
        preyLocations = util.findClosestCoordsToTargetCoord(self.getLocation(), particleLocations)
        
        if len(preyLocations) < 1: return
        
        # Choose a random prey from among the closest particles
        targetPreyLocation = random.choice(preyLocations)
        
        # Get the positions that we can legally move to
        viableCoords = self.getViablePositionsToMove(world)
        
        # Take the move that brings us closest to our prey
        bestCoords = util.findClosestCoordsToTargetCoord(targetPreyLocation, viableCoords)
        
        if len(bestCoords) > 0:
            chosenBestCoord = random.choice(bestCoords)
            self.x = chosenBestCoord[0]
            self.y = chosenBestCoord[1]
    
    def eat(self, world):
        newParticles = [p for p in world.particles if p.getLocation() != self.getLocation()]
        self.particlesEaten += abs(len(world.particles) - len(newParticles))
        world.particles = newParticles