import pygame
from colours import Colours
from worldState import WorldState
pygame.init()

# TODO:
# -> Make creeps have a an energy count
# -> Add prevention of unit collision

BOARD_WIDTH = 140
BOARD_HEIGHT = 80
AGENT_DIAMETER = 10
NUMBER_OF_RANDOM_AGENTS = 0
NUMBER_OF_CHASE_AGENTS = 25
NUMBER_OF_FLEE_AGENTS = 300

BOARD_WIDTH_PIXELS = BOARD_WIDTH * AGENT_DIAMETER
BOARD_HEIGHT_PIXELS = BOARD_HEIGHT * AGENT_DIAMETER


def setup_screen():
    screen = pygame.display.set_mode((BOARD_WIDTH_PIXELS, BOARD_HEIGHT_PIXELS))
    pygame.display.set_caption("Particle Ecosystem")
    clock = pygame.time.Clock()
    return screen, clock


def grid_location_to_pixel_location(location):
    pixel_location_x = (location[0] * AGENT_DIAMETER) + (AGENT_DIAMETER // 2)
    pixel_location_y = (location[1] * AGENT_DIAMETER) + (AGENT_DIAMETER // 2)
    return pixel_location_x, pixel_location_y


def handle_click(click_position, world):
    grid_location = (click_position[0] // AGENT_DIAMETER, click_position[1] // AGENT_DIAMETER)
    #world.create_flee_agent(grid_location)
    world.create_random_agent(grid_location, 'randomAgent')


def handle_events(events, world):
    for event in events:
        if event.type == pygame.QUIT:
            world.isRunning = False
        elif event.type == pygame.MOUSEBUTTONUP:
            handle_click(pygame.mouse.get_pos(), world)


def draw_board(screen, world):
    screen.fill(Colours.BLACK.value)
    for e in world.get_all_agents():
        pygame.draw.circle(screen, e.colour, grid_location_to_pixel_location(e.get_location()), AGENT_DIAMETER // 2)


def game_loop(screen, clock, world):
    
    while world.isRunning:
        
        handle_events(pygame.event.get(), world)
        
        draw_board(screen, world)
        
        world.move_all_agents()
        
        pygame.display.update()
        clock.tick(15)


def main():
    screen, clock = setup_screen()
    world = WorldState(BOARD_WIDTH, BOARD_HEIGHT)
    # make these functions apart of the world class
    world.create_random_agents(NUMBER_OF_RANDOM_AGENTS, 'randomAgent')

    world.create_chase_agents(NUMBER_OF_CHASE_AGENTS, 'chaseAgent1', ['randomAgent', 'fleeAgent'])

    world.create_flee_agents(NUMBER_OF_FLEE_AGENTS, 'fleeAgent', ['chaseAgent'])

    game_loop(screen, clock, world)


if __name__ == "__main__":
    main()
