class Agent:

    def __init__(self, id, x, y, colour):
        self.id = id
        self.x = x
        self.y = y
        self.colour = colour

    def get_location(self):
        return self.x, self.y

    def set_location(self, coord):
        self.x = coord[0]
        self.y = coord[1]
    
    def get_positions_to_move_on_board(self, world):
        viable_positions = [self.get_location()]

        if self.x > 0:
            viable_positions.append((self.x - 1, self.y))
        if self.x < world.grid_width - 1:
            viable_positions.append((self.x + 1, self.y))
        if self.y > 0:
            viable_positions.append((self.x, self.y - 1))
        if self.y < world.grid_height - 1:
            viable_positions.append((self.x, self.y + 1))

        return viable_positions

    def move(self, world):
        pass
    
    def eat(self, world):
        pass
