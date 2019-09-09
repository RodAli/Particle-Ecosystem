from agent import Agent
import util
import random


class FleeAgent(Agent):

    def __init__(self, id, x, y, colour, type):
        Agent.__init__(self, id, x, y, colour, type)

    def get_viable_positions_to_move(self, world):
        viable_positions = [self.get_location()]

        if self.x > 0:
            viable_positions.append((self.x - 1, self.y))
        if self.x < world.grid_width - 1:
            viable_positions.append((self.x + 1, self.y))
        if self.y > 0:
            viable_positions.append((self.x, self.y - 1))
        if self.y < world.grid_height - 1:
            viable_positions.append((self.x, self.y + 1))
        
        # Cannot move on top of another predator
        positions_of_all_other_prey = [p.get_location() for p in world.get_prey() if p.id != self.id]
        viable_positions = [p for p in viable_positions if p not in positions_of_all_other_prey]

        return viable_positions

    def move(self, world):

        # If there are no predators, default to random movement
        if len(world.chase_agents) <= 0:
            Agent.move(self, world)
            return
        
        # Get location of all predators
        predator_locations = [p.get_location() for p in world.chase_agents]

        # Get the location of the predators that are the closest
        closest_predator_locations = util.find_closest_coords_to_target_coord(self.get_location(), predator_locations)
        
        if len(closest_predator_locations) < 1: return
        
        # Choose a random prey from among the closest particles
        target_predator_location = random.choice(closest_predator_locations)
        
        # Get the positions that we can legally move to
        viable_coords = self.get_viable_positions_to_move(world)
        
        # Take the move that brings us furthest to the nearsest predator
        best_coords = util.find_furthest_coords_to_target_coord(target_predator_location, viable_coords)
        
        if len(best_coords) > 0:
            chosen_best_coord = random.choice(best_coords)
            self.x = chosen_best_coord[0]
            self.y = chosen_best_coord[1]
    
    def eat(self, world):
        pass
