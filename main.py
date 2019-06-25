import sys, pygame, random
from colours import Colours
from particle import Particle
from predator import Predator
pygame.init()

# TODO:
# -> Change snake_case to camelCase

BOARD_WIDTH = 80
BOARD_HEIGHT = 60
PARTICLE_DIAMETER = 10
NUMBER_OF_PARTICLES = 1
NUMBER_OF_PREDATORS = 1

BOARD_WIDTH_PIXELS = BOARD_WIDTH * PARTICLE_DIAMETER
BOARD_HEIGHT_PIXELS = BOARD_HEIGHT * PARTICLE_DIAMETER

colours = Colours()

def findRandomPosition(width, height):
    x = random.randint(0, width)
    y = random.randint(0, height)
    return (x, y)

def createParticles(numberOfParticles, gridWidth, gridHeight):
    particles = []
    for i in range(numberOfParticles):
        randomPosition = findRandomPosition(gridWidth, gridHeight)
        particles.append(
            Particle(
                id='Particle-' + str(i), 
                x=randomPosition[0], 
                y=randomPosition[1],
                colour=colours.getColour("GREEN")
            )
        )
    return particles

def createPredators(numberOfPredators, gridWidth, gridHeight):
    predators = []
    for i in range(numberOfPredators):
        randomPosition = findRandomPosition(gridWidth, gridHeight)
        predators.append(
            Predator(
                id='Predator-' + str(i), 
                x=randomPosition[0], 
                y=randomPosition[1],
                colour=colours.getColour("RED")
            )
        )
    return predators

def setupScreen():
    screen = pygame.display.set_mode((BOARD_WIDTH_PIXELS, BOARD_HEIGHT_PIXELS))
    pygame.display.set_caption("Pygame test")
    clock = pygame.time.Clock()
    return screen, clock

def gridLocationToPixelLocation(location):
    pixelLocationX = (location[0] * PARTICLE_DIAMETER) + (PARTICLE_DIAMETER // 2) 
    pixelLocationY = (location[1] * PARTICLE_DIAMETER) + (PARTICLE_DIAMETER // 2)
    return (pixelLocationX, pixelLocationY)

def handleEvents(events, particles, predators, running):
    running = True
    for event in events:
        if event.type == pygame.QUIT: running = False

    return running

def drawBoard(screen, particles, predators):
    screen.fill(colours.getColour("BLACK"))
    for p in particles:
        pygame.draw.circle(screen, p.getColour(), gridLocationToPixelLocation(p.getLocation()), PARTICLE_DIAMETER // 2)    
    for p in predators:
        pygame.draw.circle(screen, p.getColour(), gridLocationToPixelLocation(p.getLocation()), PARTICLE_DIAMETER // 2)

def gameLoop(screen, clock, particles, predators):

    running = True
    while running:
        
        running = handleEvents(pygame.event.get(), particles, predators, running) 
        
        drawBoard(screen, particles, predators)
        
        for p in particles:
            p.move(BOARD_WIDTH, BOARD_HEIGHT, particles)
        for p in predators:
            p.move(BOARD_WIDTH, BOARD_HEIGHT, particles)
            
        pygame.display.update()
        clock.tick(15)

def main():
    screen, clock = setupScreen()
    particles = createParticles(NUMBER_OF_PARTICLES, BOARD_WIDTH, BOARD_HEIGHT)
    predators = createPredators(NUMBER_OF_PREDATORS, BOARD_WIDTH, BOARD_HEIGHT)

    gameLoop(screen, clock, particles, predators)

if __name__ == "__main__":
    main()