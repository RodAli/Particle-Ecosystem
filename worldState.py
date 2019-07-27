import util
from particle import Particle
from predator import Predator
from creep import Creep
from colours import getColour

class WorldState:

    def __init__(self, gridWidth, gridHeight):
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.particles = []
        self.predators = []
        self.creeps = []
        self.walls = []
        self.particleCounter = 0
        self.predatorCounter = 0
        self.creepCounter = 0
        self.isRunning = True
    
    def moveEntities(self):
        for e in self.getEntities():
            e.move(self)
            e.eat(self)
    
    def getEntities(self):
        return self.particles + self.predators + self.creeps
    
    def getPrey(self):
        return self.particles + self.creeps

    def createParticles(self, numberOfParticles):
        for i in range(numberOfParticles):
            randomPosition = util.findRandomPosition(self.gridWidth, self.gridHeight)
            self.createParticle(randomPosition)
            
    def createParticle(self, location):
        particleName = 'Particle-' + str(self.particleCounter)
        self.particles.append(
                Particle(
                    id=particleName, 
                    x=location[0], 
                    y=location[1],
                    colour=getColour("GREEN")
                )
            )
        self.particleCounter += 1

    def createPredators(self, numberOfPredators):
        for i in range(numberOfPredators):
            randomPosition = util.findRandomPosition(self.gridWidth, self.gridHeight)
            self.createPredator(randomPosition)
    
    def createPredator(self, location):
        predatorName = 'Predator-' + str(self.predatorCounter)
        self.predators.append(
            Predator(
                id=predatorName, 
                x=location[0], 
                y=location[1],
                colour=getColour("RED")
            )
        )
        self.predatorCounter += 1

    def createCreeps(self, numberOfCreeps):
        for i in range(numberOfCreeps):
            randomPosition = util.findRandomPosition(self.gridWidth, self.gridHeight)
            self.createCreep(randomPosition)
    
    def createCreep(self, location):
        creepName = 'Creep-' + str(self.creepCounter)
        self.creeps.append(
            Creep(
                id=creepName, 
                x=location[0], 
                y=location[1],
                colour=getColour("BLUE")
            )
        )
        self.creepCounter += 1
