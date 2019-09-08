from randomParticle import RandomParticle
import util
import random

# Cannot move on top of another predator
# positionsOfAllOtherPredators = [p.getLocation() for p in world.predators if p.id != self.id]
# viablePositions = [p for p in viablePositions if p not in positionsOfAllOtherPredators]

class PredatorParticle(RandomParticle):

    def __init__(self, id, x, y, colour):
        super().__init__(id, x, y, colour)
        self.particlesEaten = 0

    def move(self, world):
        print(self.particlesEaten)
        allPrey = world.getPrey()

        # If there are no particles, default to random movement
        if len(allPrey) <= 0:
            super().move(world)
            return
        
        # Get location of all particles
        particleLocations = [p.getLocation() for p in allPrey]

        # Get the location of the particles that are the closest
        preyLocations = util.findClosestCoordsToTargetCoord(self.getLocation(), particleLocations)
        
        if len(preyLocations) < 1: return
        
        # Choose a random prey from among the closest particles
        targetPreyLocation = random.choice(preyLocations)
        
        # Get the positions that we can legally move to
        viableCoords = super().getViablePositionsToMoveOnBoard(world)
        
        # Take the move that brings us closest to our prey
        bestCoords = util.findClosestCoordsToTargetCoord(targetPreyLocation, viableCoords)
        
        if len(bestCoords) > 0:
            chosenBestCoord = random.choice(bestCoords)
            self.setLocation(chosenBestCoord)
            
    
    def eat(self, world):
        newParticles = [p for p in world.randomParticles if p.getLocation() != self.getLocation()]
        self.particlesEaten += abs(len(world.randomParticles) - len(newParticles))
        world.randomParticles = newParticles