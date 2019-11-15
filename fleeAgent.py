from agent import Agent
import util
import random


class FleeAgent(Agent):

    def __init__(self, id: str, x: int, y: int, colour: tuple, type: str, flee_types: list):
        Agent.__init__(self, id, x, y, colour, type)
        self.flee_types = flee_types

    def get_my_predators(self, world):
        all_prey = world.get_agents_by_types(self.flee_types)
        # Just in case I am in won prey list, remove myself
        return [p for p in all_prey if p.id != self.id]

    def move(self, grid_width: int, grid_height: int, all_agents: list):

        all_agents = world.get_all_agents()
        all_predators = self.get_my_predators(world)

        # If there are no predators, default to random movement
        if len(all_predators) <= 0:
            super().move(world)
            return

        # Get location of all predators
        predator_locations = [p.get_location() for p in all_predators]

        # Get the location of the predators that are the closest
        predator_locations_closest = util.find_closest_coords_to_target_coord(self.get_location(), predator_locations)

        if len(predator_locations_closest) < 1: return

        # Choose a random predators from among the closest predators
        target_prey_location = random.choice(predator_locations_closest)

        # Get the positions that we can legally move to
        viable_coords = super().get_positions_to_move_on_board(world)

        # Take the move that brings us furthest away from our predators
        best_coords = util.find_furthest_coords_to_target_coord(target_prey_location, viable_coords)

        if len(best_coords) > 0:
            chosen_best_coord = random.choice(best_coords)
            self.set_location(chosen_best_coord)
    
    def eat(self, world):
        pass
