import util
from randomAgent import RandomAgent
from chaseAgent import ChaseAgent
from fleeAgent import FleeAgent
from agent import Agent
from colours import Colours
from typing import List, Tuple


class WorldState:

    def __init__(self, grid_width: int, grid_height: int):
        self.grid_width: int = grid_width
        self.grid_height: int = grid_height
        self.agents: List[Agent] = []
        self.agent_counter: int = 0
        self.isRunning: bool = True

    def get_all_agents(self):
        return self.agents

    def get_agents_by_types(self, types: List[str]):
        return [a for a in self.agents if types.__contains__(a.type)]

    def move_all_agents(self):
        for e in self.agents:
            e.move(self.grid_width, self.grid_height, self.agents)
            self.agents = e.eat(self.agents)

    def remove_agents(self, ids: List[int]):
        self.agents = [a for a in self.agents if not ids.__contains__(a.id)]

    def create_random_agents(self, number_of_agents: int, agent_type: str):
        for _ in range(number_of_agents):
            random_position = util.find_random_position(self.grid_width, self.grid_height)
            self.create_random_agent(random_position, agent_type)

    def create_random_agent(self, location: Tuple[int, int], agent_type: str):
        agent_name = 'Random-Agent-' + str(self.agent_counter)
        self.agents.append(
                RandomAgent(
                    id=agent_name,
                    x=location[0],
                    y=location[1],
                    colour=Colours.GREEN.value,
                    agent_type=agent_type
                )
            )
        self.agent_counter += 1

    def create_chase_agents(self, number_of_chase_agents: int, agent_type: str, chase_types: List[str]):
        for _ in range(number_of_chase_agents):
            random_position = util.find_random_position(self.grid_width, self.grid_height)
            self.create_chase_agent(random_position, agent_type, chase_types)

    def create_chase_agent(self, location: Tuple[int, int], agent_type: str, chase_types: List[str]):
        chase_agent_name = 'Chase-Agent-' + str(self.agent_counter)
        self.agents.append(
            ChaseAgent(
                id=chase_agent_name,
                x=location[0],
                y=location[1],
                colour=Colours.RED.value,
                agent_type=agent_type,
                chase_types=chase_types
            )
        )
        self.agent_counter += 1

    def create_flee_agents(self, number_of_flee_agents: int, agent_type: str, flee_types: List[str]):
        for _ in range(number_of_flee_agents):
            random_position = util.find_random_position(self.grid_width, self.grid_height)
            self.create_flee_agent(random_position, agent_type, flee_types)

    def create_flee_agent(self, location: Tuple[int, int], agent_type: str, flee_types: List[str]):
        flee_agent_name = 'Flee-Agent-' + str(self.agent_counter)
        self.agents.append(
            FleeAgent(
                id=flee_agent_name,
                x=location[0],
                y=location[1],
                colour=Colours.BLUE.value,
                agent_type=agent_type,
                flee_types=flee_types
            )
        )
        self.agent_counter += 1
