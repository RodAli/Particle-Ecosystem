from agent import Agent
from typing import List, Tuple
import random


class RandomAgent(Agent):

    def __init__(self, id: str, x: int, y: int, colour: Tuple[int, int, int], agent_type: str):
        super().__init__(id, x, y, colour, agent_type)

    def move(self, grid_width: int, grid_height: int, all_agents: List[Agent]):
        moves_on_board = super().get_positions_to_move_on_board(grid_width, grid_height)

        # Cannot move on top of another agent
        positions_of_all_other_agents = [a.get_location() for a in all_agents if a.id != self.id]
        viable_positions = [p for p in moves_on_board if p not in positions_of_all_other_agents]

        if len(viable_positions) > 0:
            selected_position = random.choice(viable_positions)
            self.set_location(selected_position)
    
    def eat(self, all_agents: List[Agent]) -> List[Agent]:
        return all_agents
