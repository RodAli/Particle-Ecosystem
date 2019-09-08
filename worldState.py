import util
from randomParticle import RandomParticle
from predatorParticle import PredatorParticle
from preyParticle import Prey
from colours import getColour

class WorldState:

    def __init__(self, gridWidth, gridHeight):
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.randomParticles = []
        self.predatorParticles = []
        self.preyParticles = []
        self.walls = []
        self.randomParticleCounter = 0
        self.predatorCounter = 0
        self.preyCounter = 0
        self.isRunning = True
    
    def moveEntities(self):
        for e in self.getEntities():
            e.move(self)
            e.eat(self)
    
    def getEntities(self):
        return self.randomParticles + self.predatorParticles + self.preyParticles
    
    def getPrey(self):
        return self.randomParticles + self.preyParticles

    def createRandomParticles(self, numberOfParticles):
        for _ in range(numberOfParticles):
            randomPosition = util.findRandomPosition(self.gridWidth, self.gridHeight)
            self.createRandomParticle(randomPosition)
            
    def createRandomParticle(self, location):
        particleName = 'RandomParticle-' + str(self.randomParticleCounter)
        self.randomParticles.append(
                RandomParticle(
                    id=particleName, 
                    x=location[0], 
                    y=location[1],
                    colour=getColour("GREEN")
                )
            )
        self.randomParticleCounter += 1

    def createPredators(self, numberOfPredators):
        for _ in range(numberOfPredators):
            randomPosition = util.findRandomPosition(self.gridWidth, self.gridHeight)
            self.createPredator(randomPosition)
    
    def createPredator(self, location):
        predatorName = 'Predator-' + str(self.predatorCounter)
        self.predatorParticles.append(
            PredatorParticle(
                id=predatorName, 
                x=location[0], 
                y=location[1],
                colour=getColour("RED")
            )
        )
        self.predatorCounter += 1

    def createPreys(self, numberOfPrey):
        for _ in range(numberOfPrey):
            randomPosition = util.findRandomPosition(self.gridWidth, self.gridHeight)
            print(randomPosition)
            self.createPrey(randomPosition)
    
    def createPrey(self, location):
        preyName = 'Prey-' + str(self.preyCounter)
        self.preyParticles.append(
            Prey(
                id=preyName, 
                x=location[0], 
                y=location[1],
                colour=getColour("BLUE")
            )
        )
        self.preyCounter += 1
