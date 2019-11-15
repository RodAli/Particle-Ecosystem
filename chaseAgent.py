from randomAgent import RandomAgent
from agent import Agent
import util
from typing import List, Tuple
import random

# Cannot move on top of another predator
# positionsOfAllOtherPredators = [p.getLocation() for p in world.predators if p.id != self.id]
# viablePositions = [p for p in viablePositions if p not in positionsOfAllOtherPredators]


class ChaseAgent(RandomAgent):

    def __init__(self, id: str, x: int, y: int, colour: Tuple[int, int, int], agent_type: str, chase_types: List[str]):
        super().__init__(id, x, y, colour, agent_type)
        self.chase_types = chase_types
        self.eat_count = 0

    def move(self, grid_width: int, grid_height: int, all_agents: List[Agent]):
        # Get me all my prey
        all_prey = [a for a in all_agents if self.chase_types.__contains__(a.type) and a.id != self.id]

        # If there are no prey, default to random movement
        if len(all_prey) <= 0:
            super().move(grid_width, grid_height, all_agents)
            return

        # Get the location of the prey that is the closest
        target_prey_location = \
            min(all_prey, key=lambda prey: util.get_manhattan_distance(prey.get_location(), self.get_location()))
        
        # Get the positions that we can legally move to
        viable_coords = super().get_positions_to_move_on_board(grid_width, grid_height)

        # Make sure that this chase agent cannot move on top of another same type agent
        own_types = [a.get_location() for a in all_agents if a.type == self.type and a.id != self.id]
        viable_coords = [c for c in viable_coords if c not in own_types]
        
        # Take the move that brings us closest to our prey
        best_coord = util.find_closest_coord_to_target_coord(target_prey_location.get_location(), viable_coords)

        self.set_location(best_coord)

    def eat(self, all_agents: List[Agent]) -> List[Agent]:
        # Get me all my prey
        all_prey = [a for a in all_agents if self.chase_types.__contains__(a.type) and a.id != self.id]
        agent_ids_to_remove = [a.id for a in all_prey if a.get_location() == self.get_location()]
        self.eat_count += len(agent_ids_to_remove)
        return [a for a in all_agents if not agent_ids_to_remove.__contains__(a.id)]
