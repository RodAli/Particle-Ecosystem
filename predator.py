from particle import Particle
import util
import random

class Predator(Particle):

    def __init__(self, id, x, y, colour):
        Particle.__init__(self, id, x, y, colour)
        self.particlesEaten = 0

    def move(self, boardWidth, boardHeight, particles):

        # If there are no particles, default to random movement
        if len(particles) <= 0:
            Particle.move(self, boardWidth, boardHeight, particles)
            return
        
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
    
    def eat(self, particles):
        newParticles = []
        for p in particles:
            if p.getLocation() != self.getLocation():
                newParticles.append(p)
            else:
                self.particlesEaten += 1
        return newParticles