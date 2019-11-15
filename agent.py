from typing import List, Tuple


class Agent:

    def __init__(self, id: str, x: int, y: int, colour: Tuple[int, int, int], agent_type: str):
        self.id: str = id
        self.x: int = x
        self.y: int = y
        self.colour = colour
        self.type = agent_type

    def get_location(self):
        return self.x, self.y

    def set_location(self, coord: Tuple[int, int]):
        self.x = coord[0]
        self.y = coord[1]
    
    def get_positions_to_move_on_board(self, grid_width: int, grid_height: int):
        viable_positions = [self.get_location()]

        if self.x > 0:
            viable_positions.append((self.x - 1, self.y))
        if self.x < grid_width - 1:
            viable_positions.append((self.x + 1, self.y))
        if self.y > 0:
            viable_positions.append((self.x, self.y - 1))
        if self.y < grid_height - 1:
            viable_positions.append((self.x, self.y + 1))

        return viable_positions

    def move(self, grid_width: int, grid_height: int, all_agents: List):
        pass
    
    def eat(self, all_agents: List) -> List:
        return all_agents
