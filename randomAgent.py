from agent import Agent
from typing import List, Tuple
import random


class RandomAgent(Agent):

    def __init__(self, id: str, x: int, y: int, colour: Tuple[int, int, int], agent_type: str):
        super().__init__(id, x, y, colour, agent_type)

    def move(self, grid_width: int, grid_height: int, all_agents: List[Agent]):
        viable_coords = super().get_positions_to_move_on_board(grid_width, grid_height)

        # Make sure that this chase agent cannot move on top of another same type agent
        own_types = [a.get_location() for a in all_agents if a.type == self.type and a.id != self.id]
        viable_coords = [c for c in viable_coords if c not in own_types]

        if len(viable_coords) > 0:
            selected_position = random.choice(viable_coords)
            self.set_location(selected_position)
    
    def eat(self, all_agents: List[Agent]) -> List[Agent]:
        return all_agents
