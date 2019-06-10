import sys, pygame, random
from colours import Colours
from particle import Particle
pygame.init()

# TODO:
# -> Change snake_case to camelCase

BOARD_WIDTH = 80
BOARD_HEIGHT = 60
PARTICLE_DIAMETER = 10
NUMBER_OF_PARTICLES = 5

BOARD_WIDTH_PIXELS = BOARD_WIDTH * PARTICLE_DIAMETER
BOARD_HEIGHT_PIXELS = BOARD_HEIGHT * PARTICLE_DIAMETER

def findRandomPosition(width, height):
    x = random.randint(0, width)
    y = random.randint(0, height)
    return (x, y)

def createEntities(numberOfEntities, gridWidth, gridHeight):
    colours = Colours()
    entities = []
    for i in range(numberOfEntities):
        randomPosition = findRandomPosition(gridWidth, gridHeight)
        entities.append(
            Particle(
                id=str(i), 
                x=randomPosition[0], 
                y=randomPosition[1],
                colour=colours.getColour("BLUE")
            )
        )
    return entities

def setupScreen():
    screen = pygame.display.set_mode((BOARD_WIDTH_PIXELS, BOARD_HEIGHT_PIXELS))
    pygame.display.set_caption("Pygame test")
    clock = pygame.time.Clock()
    return screen, clock

def gridLocationToPixelLocation(location):
    pixelLocationX = (location[0] * PARTICLE_DIAMETER) + (PARTICLE_DIAMETER // 2) 
    pixelLocationY = (location[1] * PARTICLE_DIAMETER) + (PARTICLE_DIAMETER // 2)
    return (pixelLocationX, pixelLocationY)

def gameLoop(screen, clock, entities):

    colours = Colours()
    running = True
    while running:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: running = False
        
        screen.fill(colours.getColour("BLACK"))
        
        for e in entities:
            pygame.draw.circle(screen, e.getColour(), gridLocationToPixelLocation(e.getLocation()), PARTICLE_DIAMETER // 2)
            e.moveRandom(BOARD_WIDTH, BOARD_HEIGHT)

        pygame.display.update()
        clock.tick(15)

def main():
    screen, clock = setupScreen()
    entities = createEntities(NUMBER_OF_PARTICLES, BOARD_WIDTH, BOARD_HEIGHT)

    gameLoop(screen, clock, entities)

if __name__ == "__main__":
    main()