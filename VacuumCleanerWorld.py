#Write pseudocode for a performance-measuring environment simulator and simple reflex agent for the vacuum-cleaner world. Your pseudocode should be modular so that the sensors, actuators, and environment characteristics (size, shape, dirt placement, etc.) can be changed easily.

'''
# Generate a random position within the locations
def random_position_in_grid(width, height):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return (x, y)

# VacuumEnvironment sets up the vacuum world environment
class VacuumEnvironment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.agent_location = random_position_in_grid(self.width, self.height)
        self.grid = [[False for _ in range(height)] for _ in range(width)]
        self.performance_score = 0

    # Placing dirt
    def place_dirt(self, dirt_locations):
        self.grid = [[False for _ in range(self.height)] for _ in range(self.width)] 
            x, y = location
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[x][y] = True  # Set the location to True to indicate dirt is present

    # Move the agent
    def move_agent(self, action):
        x, y = self.agent_location
        if action == "right" and x < self.width - 1:
            self.agent_location = (x + 1, y)
        elif action == "left" and x > 0:
            self.agent_location = (x - 1, y)
        elif action == "up" and y < self.height - 1:
            self.agent_location = (x, y + 1)
        elif action == "down" and y > 0:
            self.agent_location = (x, y - 1)

    # Clean if dirt is present
    def clean(self):
        x, y = self.agent_location
        if self.grid[x][y]:  # If location is dirty
            self.grid[x][y] = False
            self.performance_score += 10  # Add 10 to performance is cleaned successfully

    # Percept: perceiving the location and the presence of dirt
    def percept(self):
        x, y = self.agent_location
        return (self.grid[x][y], self.agent_location)

    # Run the agent and record the performance
    def run_agent(self, agent, iterations=1):
        total_score = 0
        for _ in range(iterations):
            self.performance_score = 0
            self.agent_location = random_position_in_grid(self.width, self.height)  # Random start location

            # Keep running the agent 
            while True:
                percept = self.percept()
                action = agent(percept)  

                if action == "do_nothing":
                    break

                if action == "clean":
                    self.clean()
                else:
                    self.move_agent(action)

            total_score += self.performance_score

        return total_score / iterations  # Return the average 


# Define a simple reflex agent
def simple_reflex_agent(percept):
    dirt, _ = percept
    if dirt:
        return "clean"  # Clean if dirt is present
    else:
        return "do_nothing"  # Do nothing if the current location is clean

'''

## Implement a simple reflex agent for the vacuum environment implemented in 4. Run the environment with this agent for all possible initial dirt configurations and agent locations. Record the performance score for each configuration.

import random

# Generate a random position within the locations
def random_position_in_grid(width, height):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return (x, y)

# VacuumEnvironment sets up the vacuum world environment
class VacuumEnvironment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.agent_location = random_position_in_grid(self.width, self.height)
        self.grid = [[False for _ in range(height)] for _ in range(width)]
        self.performance_score = 0

    # Placing dirt
    def place_dirt(self, dirt_locations):
        self.grid = [[False for _ in range(self.height)] for _ in range(self.width)]  
        for location in dirt_locations:
            x, y = location
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[x][y] = True  # Set the location to True to indicate dirt is present

    # Move the agent 
    def move_agent(self, action):
        x, y = self.agent_location
        if action == "right" and x < self.width - 1:
            self.agent_location = (x + 1, y)
        elif action == "left" and x > 0:
            self.agent_location = (x - 1, y)
        elif action == "up" and y < self.height - 1:
            self.agent_location = (x, y + 1)
        elif action == "down" and y > 0:
            self.agent_location = (x, y - 1)

    # Clean if dirt is present
    def clean(self):
        x, y = self.agent_location
        if self.grid[x][y]:  
            self.grid[x][y] = False
            self.performance_score += 10  # Add 10 to performance is cleaned successfully

    # Percept: perceiving the location and the presence of dirt
    def percept(self):
        x, y = self.agent_location
        return (self.grid[x][y], self.agent_location)

    # Run the agent and record the performance
    def run_agent(self, agent, iterations=1):
        total_score = 0
        for _ in range(iterations):
            self.performance_score = 0
            self.agent_location = random_position_in_grid(self.width, self.height)  # Random start location

            # Keep running the agent
            while True:
                percept = self.percept()
                action = agent(percept)  

                if action == "do_nothing":
                    break

                if action == "clean":
                    self.clean()
                else:
                    self.move_agent(action)

            total_score += self.performance_score

        return total_score / iterations  # Return the average 


# Define a simple reflex agent
def simple_reflex_agent(percept):
    dirt, _ = percept
    if dirt:
        return "clean"  # Clean if dirt is present
    else:
        return "do_nothing"  # Do nothing if the current location is clean

# Set up the environment 
width = 2
height = 2
dirt_configurations = [
    [],
    [(0, 0)],
    [(1, 0)],
    [(0, 1)],
    [(1, 1)],
    [(0, 0), (1, 1)],
    [(0, 1), (1, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

# Create the environment
environment = VacuumEnvironment(width, height)

# Run the environment with diverse configurations
total_score = 0
total_configurations = len(dirt_configurations)

for dirt_configuration in dirt_configurations:
    environment.place_dirt(dirt_configuration)
    score = environment.run_agent(simple_reflex_agent)
    print("Dirt Configuration:", dirt_configuration)
    print("Performance Score:", score)
    print("---------------")
    total_score += score

average_score = total_score / total_configurations
print("Overall Average Score:", average_score)

