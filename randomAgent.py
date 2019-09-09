from agent import Agent
import random


class RandomAgent(Agent):

    def __init__(self, id: int, x: int, y: int, colour: tuple, type: str):
        super().__init__(id, x, y, colour, type)
    
    # Cannot move on top of another prey
    # positionsOfAllOtherPrey = [p.getLocation() for p in world.getPrey() if p.id != self.id]
    # viablePositions = [p for p in viablePositions if p not in positionsOfAllOtherPrey]

    def move(self, world):
        viable_positions = super().get_positions_to_move_on_board(world)

        if len(viable_positions) > 0:
            selected_position = random.choice(viable_positions)
            self.set_location(selected_position)
    
    def eat(self, world):
        pass
