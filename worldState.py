import util
from randomAgent import RandomAgent
from chaseAgent import ChaseAgent
from fleeAgent import FleeAgent
from colours import Colours


class WorldState:

    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.agents = []
        self.agent_counter = 0
        self.isRunning = True

    def get_all_agents(self):
        return self.agents

    def get_agents_by_types(self, types: list):
        return [a for a in self.agents if types.__contains__(a.type)]

    def move_all_agents(self):
        for e in self.agents:
            e.move(self)
            e.eat(self)

    def remove_agents(self, ids: list):
        self.agents = [a for a in self.agents if not ids.__contains__(a.id)]

    def create_random_agents(self, number_of_agents: int, type: str):
        for _ in range(number_of_agents):
            random_position = util.find_random_position(self.grid_width, self.grid_height)
            self.create_random_agent(random_position, type)

    def create_random_agent(self, location: tuple, type: str):
        agent_name = 'Random-Agent-' + str(self.agent_counter)
        self.agents.append(
                RandomAgent(
                    id=agent_name,
                    x=location[0],
                    y=location[1],
                    colour=Colours.GREEN.value,
                    type=type
                )
            )
        self.agent_counter += 1

    def create_chase_agents(self, number_of_chase_agents: int, type: str, chase_types: list):
        for _ in range(number_of_chase_agents):
            random_position = util.find_random_position(self.grid_width, self.grid_height)
            self.create_chase_agent(random_position, type, chase_types)

    def create_chase_agent(self, location: tuple, type: str, chase_types: list):
        chase_agent_name = 'Chase-Agent-' + str(self.agent_counter)
        self.agents.append(
            ChaseAgent(
                id=chase_agent_name,
                x=location[0],
                y=location[1],
                colour=Colours.RED.value,
                type=type,
                chase_types=chase_types
            )
        )
        self.agent_counter += 1

    def create_flee_agents(self, number_of_flee_agents: int, type: str, flee_types: list):
        for _ in range(number_of_flee_agents):
            random_position = util.find_random_position(self.grid_width, self.grid_height)
            print(random_position)
            self.create_flee_agent(random_position, type, flee_types)

    def create_flee_agent(self, location: tuple, type: str, flee_types: list):
        flee_agent_name = 'Flee-Agent-' + str(self.agent_counter)
        self.agents.append(
            FleeAgent(
                id=flee_agent_name,
                x=location[0],
                y=location[1],
                colour=Colours.BLUE.value,
                type=type,
                flee_types=flee_types
            )
        )
        self.agent_counter += 1
