import sys, pygame, random
from colours import getColour
from particle import Particle
from predator import Predator
from worldState import WorldState
pygame.init()

# TODO:
# -> Change snake_case to camelCase
# -> Particles cannot intersect with eachother or predators (they dont kill themselves)

BOARD_WIDTH = 150
BOARD_HEIGHT = 80
PARTICLE_DIAMETER = 10
NUMBER_OF_PARTICLES = 10
NUMBER_OF_PREDATORS = 3

BOARD_WIDTH_PIXELS = BOARD_WIDTH * PARTICLE_DIAMETER
BOARD_HEIGHT_PIXELS = BOARD_HEIGHT * PARTICLE_DIAMETER

def setupScreen():
    screen = pygame.display.set_mode((BOARD_WIDTH_PIXELS, BOARD_HEIGHT_PIXELS))
    pygame.display.set_caption("Particle Ecosystem")
    clock = pygame.time.Clock()
    return screen, clock

def gridLocationToPixelLocation(location):
    pixelLocationX = (location[0] * PARTICLE_DIAMETER) + (PARTICLE_DIAMETER // 2) 
    pixelLocationY = (location[1] * PARTICLE_DIAMETER) + (PARTICLE_DIAMETER // 2)
    return (pixelLocationX, pixelLocationY)

def handleClick(clickPosition, world):
    gridLocation = (clickPosition[0] // PARTICLE_DIAMETER, clickPosition[1] // PARTICLE_DIAMETER)
    world.createParticle(gridLocation)

def handleEvents(events, world):
    for event in events:
        if event.type == pygame.QUIT: world.isRunning = False
        
        if event.type == pygame.MOUSEBUTTONUP: 
            handleClick(pygame.mouse.get_pos(), world)

def drawBoard(screen, world):
    screen.fill(getColour("BLACK"))
    for p in world.particles:
        pygame.draw.circle(screen, p.getColour(), gridLocationToPixelLocation(p.getLocation()), PARTICLE_DIAMETER // 2)    
    for p in world.predators:
        pygame.draw.circle(screen, p.getColour(), gridLocationToPixelLocation(p.getLocation()), PARTICLE_DIAMETER // 2)

def gameLoop(screen, clock, world):
    
    while world.isRunning:
        
        handleEvents(pygame.event.get(), world) 
        
        drawBoard(screen, world)
        
        for p in world.predators:
            p.eat(world)
            p.move(world)
            p.eat(world)
        for p in world.particles:
            p.move(world)
        
        pygame.display.update()
        clock.tick(15)

def main():
    screen, clock = setupScreen()
    world = WorldState(BOARD_WIDTH, BOARD_HEIGHT)
    # make thse function apart of the world class
    world.createParticles(NUMBER_OF_PARTICLES)
    world.createPredators(NUMBER_OF_PREDATORS)

    gameLoop(screen, clock, world)

if __name__ == "__main__":
    main()