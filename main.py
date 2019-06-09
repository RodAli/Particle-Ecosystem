import sys, pygame, random
from colours import Colours
from dot import Dot
pygame.init()

# TODO:
# -> Change snake_case to camelCase

BOARD_WIDTH_PIXELS = 100
BOARD_HEIGHT_PIXELS = 100
DOT_DIAMETER = 10
NUMBER_OF_ENTITIES = 5
DOT_SPEED = DOT_DIAMETER // 2

def create_entities(number_of_entities, screen_width, screen_height):
    colours = Colours()
    entities = []
    for i in range(number_of_entities):
        entities.append(
            Dot(
                id=str(i), 
                x=random.randint(0, BOARD_WIDTH_PIXELS // DOT_DIAMETER) + DOT_DIAMETER // 2, 
                y=random.randint(0, BOARD_HEIGHT_PIXELS // DOT_DIAMETER) + DOT_DIAMETER // 2,
                radius=DOT_DIAMETER // 2,
                speed=DOT_SPEED,
                colour=colours.getRandomColor()
            )
        )
    return entities

def setupScreen():
    screen = pygame.display.set_mode((BOARD_WIDTH_PIXELS, BOARD_HEIGHT_PIXELS))
    pygame.display.set_caption("Pygame test")
    clock = pygame.time.Clock()
    return screen, clock

def gameLoop(screen, clock, entities):

    colours = Colours()
    running = True
    while running:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: running = False
        
        screen.fill(colours.colour_list["BLACK"])
        
        for e in entities:
            pygame.draw.circle(screen, e.getColour(), e.getLocation(), DOT_DIAMETER // 2)
            e.moveRandom(BOARD_WIDTH_PIXELS, BOARD_HEIGHT_PIXELS)

        pygame.display.update()
        clock.tick(15)

def main():
    screen, clock = setupScreen()
    entities = create_entities(NUMBER_OF_ENTITIES, BOARD_WIDTH_PIXELS, BOARD_HEIGHT_PIXELS)

    gameLoop(screen, clock, entities)

if __name__ == "__main__":
    main()