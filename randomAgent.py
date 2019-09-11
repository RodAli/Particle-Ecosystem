from agent import Agent
import random


class RandomAgent(Agent):

    def __init__(self, id: int, x: int, y: int, colour: tuple, type: str):
        super().__init__(id, x, y, colour, type)

    def move(self, world):
        moves_on_board = super().get_positions_to_move_on_board(world)

        # Cannot move on top of another prey
        positions_of_all_other_agents = [a.get_location() for a in world.get_all_agents() if a.id != self.id]
        viable_positions = [p for p in moves_on_board if p not in positions_of_all_other_agents]

        if len(viable_positions) > 0:
            selected_position = random.choice(viable_positions)
            self.set_location(selected_position)
    
    def eat(self, world):
        pass
