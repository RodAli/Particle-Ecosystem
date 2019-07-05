from particle import Particle
import util
import random

class Predator(Particle):

    def __init__(self, id, x, y, colour):
        Particle.__init__(self, id, x, y, colour)
        self.particlesEaten = 0

    def move(self, world):

        # If there are no particles, default to random movement
        if len(world.particles) <= 0:
            Particle.move(self, boardWidth, boardHeight, particles)
            return
        
        particleLocations = [p.getLocation() for p in world.particles]

        preyLocations = util.findClosestCoordsToTargetCoord(self.getLocation(), particleLocations)
        
        if len(preyLocations) < 1: return
        
        targetPreyLocation = random.choice(preyLocations)

        viableCoords = self.getViablePositionsToMove(world.gridWidth, world.gridHeight)
        
        bestCoords = util.findClosestCoordsToTargetCoord(targetPreyLocation, viableCoords)
        
        if len(bestCoords) > 0:
            chosenBestCoord = random.choice(bestCoords)
            self.x = chosenBestCoord[0]
            self.y = chosenBestCoord[1]
    
    def eat(self, world):
        newParticles = [p for p in world.particles if p.getLocation() != self.getLocation()]
        self.particlesEaten += abs(len(world.particles) - len(newParticles))
        world.particles = newParticles