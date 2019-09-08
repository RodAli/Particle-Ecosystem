from particle import Particle
import random

class RandomParticle(Particle):

    def __init__(self, id, x, y, colour):
        super().__init__(id, x, y, colour)
    
    # Cannot move on top of another prey
    # positionsOfAllOtherPrey = [p.getLocation() for p in world.getPrey() if p.id != self.id]
    # viablePositions = [p for p in viablePositions if p not in positionsOfAllOtherPrey]

    def move(self, world):
        viablePositions = super().getViablePositionsToMoveOnBoard(world)

        if len(viablePositions) > 0:
            selectedPosition = random.choice(viablePositions)
            self.setLocation(selectedPosition)
    
    def eat(self, world):
        pass