from definitions import Agent
import numpy as np
import heapq
from scipy.spatial import distance
import random

class RandAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.
        Args:
            env: A reference to an environment.
        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self, env)

        # Get initial percepts
        self.percepts = env.initial_percepts()

        # Initializes the frontier with the initial postion
        self.frontier = [[self.percepts['current_position']]]

        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)

        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path}
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room
        self.percepts = self.env.signal(action)

        # Add visited node
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet

        viable_neighbors = self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors:
            # Select random neighbor
            visit = viable_neighbors[np.random.randint(0, len(viable_neighbors))]

            # Append neighbor to the path and add it to the frontier
            self.frontier = [path + [visit]] + self.frontier

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])

class DFSAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.
        Args:
            env: A reference to an environment.
        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self, env)

        # Get initial percepts
        self.percepts = env.initial_percepts()

        # Initializes the frontier with the initial postion
        self.frontier = [[self.percepts['current_position']]]

        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)

        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path}
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room
        self.percepts = self.env.signal(action)

        # Add visited node
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet

        viable_neighbors = self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors:
            # para cada vizinho, na lista de caminhos viaveis, pega o vizinho retirado
            for neighbors in viable_neighbors:
                # checa os ciclos
                cycle = False
                for p in path:
                    if (neighbors == p).all():
                        cycle = True
                        break

                # checa visitados
                visited = False
                for p in self.visited:
                    if (neighbors == p).all():
                        visited = True

                if not cycle and not visited:
                    self.frontier = [path + [neighbors]] + self.frontier

                # Append neighbor to the path and add it to the frontier

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])

class BFSAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.
        Args:
            env: A reference to an environment.
        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self, env)

        # Get initial percepts
        self.percepts = env.initial_percepts()

        # Initializes the frontier with the initial postion
        self.frontier = [[self.percepts['current_position']]]

        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """
        # Select a path from the frontier
        path = self.frontier.pop(0)

        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path}
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room
        self.percepts = self.env.signal(action)

        # Add visited node
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet

        viable_neighbors = self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors:
            # para cada vizinho, na lista de caminhos viaveis, pega o vizinho retirado
            for neighbors in viable_neighbors:
                cycle = False
                for p in path:
                    if (neighbors == p).all():
                        cycle = True
                        break
                # checa visitados
                visited = False
                for p in self.visited:
                    if (neighbors == p).all():
                        visited = True
                if not cycle and not visited:
                    self.frontier = self.frontier + [path + [neighbors]]  # adciona no fim da fronteira.

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])

class AStarAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """
    def __init__(self, env):
        """Connects to the next available port.
        Args:
            env: A reference to an environment.
        """
        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self, env)

        # Get initial percepts
        self.percepts = env.initial_percepts()

        # Initializes the frontier with the initial postion
        self.frontier = [[self.percepts['current_position']]]

        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """
        # Select a path from the frontier
        self.path = self.frontier.pop(0)
        # Visit the last node in the path
        action = {'visit_position': self.path[-1], 'path': self.path}
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room
        self.percepts = self.env.signal(action)
        # Add visited node
        self.visited.append(self.path[-1])
        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        viable_neighbors = self.percepts['neighbors']
        # If the agent is not stuck
        if viable_neighbors:
            dist = []
            for neighbor in viable_neighbors:
                dist.append(distance.euclidean(neighbor, self.percepts['target']))
            for neigbor in viable_neighbors:
                pos = dist.index(max(dist))
                insertF = True
                for aux in self.frontier:
                    if (viable_neighbors[pos] == aux).all():
                        insertF= False
                if insertF == True:
                    self.frontier = [self.path + [viable_neighbors[pos]]]+ self.frontier
                print(dist[pos])
                dist[pos] = -1
            # Append neighbor to the path and add it to the frontier
    def run(self):
        """Keeps the agent acting until it finds the target
        """
        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])
        print(self.path)

class GreedyAgent():
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.
        Args:
            env: A reference to an environment.
        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self, env)

        # Get initial percepts
        self.percepts = env.initial_percepts()

        # Initializes the frontier with the initial postion
        self.frontier = [[self.percepts['current_position']]]

        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)

        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path}
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room
        self.percepts = self.env.signal(action)

        # Add visited node
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet

        viable_neighbors = self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors:

            self.frontier = path + [viable_neighbors]+ self.frontier


            # Append neighbor to the path and add it to the frontier


    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])

