from randomAgent import RandomAgent
import util
import random

# Cannot move on top of another predator
# positionsOfAllOtherPredators = [p.getLocation() for p in world.predators if p.id != self.id]
# viablePositions = [p for p in viablePositions if p not in positionsOfAllOtherPredators]


class ChaseAgent(RandomAgent):

    def __init__(self, id, x, y, colour):
        super().__init__(id, x, y, colour)
        self.eat_count = 0

    def move(self, world):
        all_prey = world.get_prey()

        # If there are no particles, default to random movement
        if len(all_prey) <= 0:
            super().move(world)
            return
        
        # Get location of all particles
        particle_locations = [p.get_location() for p in all_prey]

        # Get the location of the particles that are the closest
        prey_locations = util.find_closest_coords_to_target_coord(self.get_location(), particle_locations)
        
        if len(prey_locations) < 1: return
        
        # Choose a random prey from among the closest particles
        target_prey_location = random.choice(prey_locations)
        
        # Get the positions that we can legally move to
        viable_coords = super().get_positions_to_move_on_board(world)
        
        # Take the move that brings us closest to our prey
        best_coords = util.find_closest_coords_to_target_coord(target_prey_location, viable_coords)
        
        if len(best_coords) > 0:
            chosen_best_coord = random.choice(best_coords)
            self.set_location(chosen_best_coord)

    def eat(self, world):
        new_particles = [p for p in world.random_agents if p.get_location() != self.get_location()]
        self.eat_count += abs(len(world.random_agents) - len(new_particles))
        world.randomParticles = new_particles
