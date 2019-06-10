from particle import Particle

class Predator(Particle):

    def __init__(self, id, x, y, colour):
        Particle.__init__(self, id, x, y, colour)

    def move(self, boardWidth, boardHeight, particles):
        #TODO: 