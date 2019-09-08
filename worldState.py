import util
from randomAgent import RandomAgent
from chaseAgent import ChaseAgent
from fleeAgent import FleeAgent
from colours import Colours


class WorldState:

    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.random_agents = []
        self.chase_agents = []
        self.flee_agents = []
        self.random_agent_counter = 0
        self.chase_agent_counter = 0
        self.flee_agent_counter = 0
        self.isRunning = True
    
    def move_entities(self):
        for e in self.get_entities():
            e.move(self)
            e.eat(self)
    
    def get_entities(self):
        return self.random_agents + self.chase_agents + self.flee_agents
    
    def get_prey(self):
        return self.random_agents + self.flee_agents

    def create_random_agents(self, number_of_agents):
        for _ in range(number_of_agents):
            random_position = util.find_random_position(self.grid_width, self.grid_height)
            self.create_random_agent(random_position)
            
    def create_random_agent(self, location):
        agent_name = 'Random-Agent-' + str(self.random_agent_counter)
        self.random_agents.append(
                RandomAgent(
                    id=agent_name,
                    x=location[0], 
                    y=location[1],
                    colour=Colours.GREEN.value
                )
            )
        self.random_agent_counter += 1

    def create_chase_agents(self, number_of_chase_agents):
        for _ in range(number_of_chase_agents):
            random_position = util.find_random_position(self.grid_width, self.grid_height)
            self.create_chase_agent(random_position)
    
    def create_chase_agent(self, location):
        chase_agent_name = 'Chase-Agent-' + str(self.chase_agent_counter)
        self.chase_agents.append(
            ChaseAgent(
                id=chase_agent_name,
                x=location[0], 
                y=location[1],
                colour=Colours.RED.value
            )
        )
        self.chase_agent_counter += 1

    def create_flee_agents(self, number_of_flee_agents):
        for _ in range(number_of_flee_agents):
            random_position = util.find_random_position(self.grid_width, self.grid_height)
            print(random_position)
            self.create_flee_agent(random_position)
    
    def create_flee_agent(self, location):
        flee_agent_name = 'Flee-Agent-' + str(self.flee_agent_counter)
        self.flee_agents.append(
            FleeAgent(
                id=flee_agent_name,
                x=location[0], 
                y=location[1],
                colour=Colours.BLUE.value
            )
        )
        self.flee_agent_counter += 1
