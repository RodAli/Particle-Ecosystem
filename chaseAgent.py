from randomAgent import RandomAgent
import util
import random

# Cannot move on top of another predator
# positionsOfAllOtherPredators = [p.getLocation() for p in world.predators if p.id != self.id]
# viablePositions = [p for p in viablePositions if p not in positionsOfAllOtherPredators]


class ChaseAgent(RandomAgent):

    def __init__(self, id: str, x: int, y: int, colour: tuple, type: str, chase_types: list):
        super().__init__(id, x, y, colour, type)
        self.chase_types = chase_types
        self.eat_count = 0

    def get_my_prey(self, world):
        all_prey = world.get_agents_by_types(self.chase_types)
        # Just in case I am in won prey list, remove myselfs
        return [p for p in all_prey if p.id != self.id]

    def move(self, world):
        all_prey = self.get_my_prey(world)

        # If there are no prey, default to random movement
        if len(all_prey) <= 0:
            super().move(world)
            return
        
        # Get location of all prey
        prey_locations = [p.get_location() for p in all_prey]

        # Get the location of the prey that are the closest
        prey_locations = util.find_closest_coords_to_target_coord(self.get_location(), prey_locations)
        
        if len(prey_locations) < 1: return
        
        # Choose a random prey from among the closest prey
        target_prey_location = random.choice(prey_locations)
        
        # Get the positions that we can legally move to
        viable_coords = super().get_positions_to_move_on_board(world)
        
        # Take the move that brings us closest to our prey
        best_coords = util.find_closest_coords_to_target_coord(target_prey_location, viable_coords)
        
        if len(best_coords) > 0:
            chosen_best_coord = random.choice(best_coords)
            self.set_location(chosen_best_coord)

    def eat(self, world):
        all_prey = self.get_my_prey(world)
        agent_ids_to_remove = [a.id for a in all_prey if a.get_location() == self.get_location()]
        self.eat_count += len(agent_ids_to_remove)
        world.remove_agents(agent_ids_to_remove)
